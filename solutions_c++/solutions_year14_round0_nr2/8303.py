#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <fstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <cmath>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
 
#define FOR(i,f,t) for(int i = f;i<t;i++)
#define For(i, t) for(int i = 0;i<t;i++)
#define ITER(it, a) for(typeof (a.begin()) it = a.begin();it != a.end();it++)
#define range(cont) cont.begin(), cont.end()
#define mp(i,j) make_pair(i,j)
#define pb push_back
#define inf 10737418

using namespace std;
using namespace std::tr1;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

int nc;
double a,b,c;

double prod, now;
double comp(){
	now += a / prod;
	prod += b;
	return now + c/prod;
}

int main(){
	
	cin >> nc;
	cout.precision(10);
	cout<<fixed;

	For(i, nc){
		cin >> a>>b>>c;

		prod = 2, now = 0;
		double ans = c/prod,t;
		while((t = comp()) < ans){
			ans = t; 
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}