#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <typeinfo>
#include <set>
#include <cctype>
#include <locale>
#include <utility>
#include <map>
#include <iterator>
#include <valarray>
#include <complex>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <numeric>
#include <cstring>
using namespace std;

#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sqr(a) (a)*(a)
#define mp make_pair

typedef long long i64;

//////////////////////////////////////////////////////

const int INF = ~(1 << 31);

double xst = 1, yst = 1;
int n = 2;

double func(double x1, double x2){
	return (x1*x1 - x2)*(x1*x1 - x2) + (x1 - 1)*(x1 - 1);
}

double val(pair<double, double> cur, int i, int j, double len){
	if(i == j){
		if(j == 1) return cur.first + ((sqrt(n + 1.0) + n - 1) / (n * sqrt(2.0)))*len;
		if(j == 2) return cur.second + ((sqrt(n + 1.0) + n - 1) / (n * sqrt(2.0)))*len;
	}else{
		if(j == 1) return cur.first + ((sqrt(n + 1.0) - 1) / (n * sqrt(2.0)))*len;
		if(j == 2) return cur.second + ((sqrt(n + 1.0) - 1) / (n * sqrt(2.0)))*len;
	}
}

bool cmp(pair<double, double> a, pair<double, double> b){
	return func(a.first, a.second) < func(b.first, b.second);
}

bool ispal(long long n){
	string s;
	while(n){
		s += n % 10;
		n /= 10;
	}
	int l = s.size() / 2;
	for(int i = 0; i < l; i++){
		if(s[i] != s[s.size() - i - 1]) return false;
	}
	return true;
}

int main(){
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	vector<long long> v;
	int n = (int)(1e7)+5;
	for(int i = 1; i < n; i++){
		if(ispal(i) && ispal((i64)i*i)) v.pb((i64)i*i);
	}
	long long a, b;
	for(int t = 1; t <= tt; t++){
		cin >> a >> b;
		int res = int(lower_bound(v.begin(), v.end(), b) - lower_bound(v.begin(), v.end(), a));
		if(lower_bound(v.begin(), v.end(), b) != v.end() && (*lower_bound(v.begin(), v.end(), b)) == b) res++;
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}