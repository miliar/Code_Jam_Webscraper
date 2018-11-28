#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

int ijk_table[4][4] = {
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4}};

int mul_ijk(int a, int b){
	int sign = ((a>>2)^(b>>2))<<2;
	a &= 3; b &= 3;
	return sign^ijk_table[a][b];
}

int calc(string &s){
	int res = 0;
	for(int i = 0; i < s.size(); i++) res = mul_ijk(res, s[i]-'i'+1);
	return res;
}

int pow_ijk(int a, ll n){
	int res = 0;
	while(n){
		if(n&1) res = mul_ijk(res, a);
		a = mul_ijk(a, a);
		n >>= 1;
	}
	return res;
}

bool check(string &s, ll m){
	int n = s.size();
	int r = 0;
	bool ok = false;
	ll pi, pj;
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < n; j++){
			r = mul_ijk(r, s[j]-'i'+1);
			if((r&3)==1){
				ok = true;
				pi = i;
				pj = j;
				i = 3;
				break;
			}
		}
	if(ok) cerr<<"ok2"<<endl;
	if(!ok || pi>=m) return false;
	r = 0;
	for(int i = m-1; i >= m-3 ; i--)
		for(int j = n-1; j >= 0; j--){
			r = mul_ijk(s[j]-'i'+1, r);
			if((r&3)==3){
				if(i<0 || i<pi || (i==pi && j<=pj)) return false;
				return true;
			}
		}
	return false;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		ll n, m;
		cin>>n>>m;
		string s;
		cin>>s;
		bool ok = check(s, m);
		if(ok) cerr<<"ok"<<endl;
		printf("Case #%d: %s\n", Case, (ok && pow_ijk(calc(s), m)==4)?"YES":"NO");
	}
	return 0;
}

