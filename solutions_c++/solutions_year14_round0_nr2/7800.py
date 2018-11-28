#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>


using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-4
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
#define ALL(n) n.begin(),n.end()
#define pb push_back
#define iFor(i,n) for(typeof(n.begin()) i=n.begin();i!=n.end();i++)

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin >> t;
	int ca = 0;
	while(t--){
		double c, f, x;
		cin >> c >> f >> x;
		double ans = x / 2.0;
		double cost = 0;
		for(int i=1;;i++){
			cost += c / (2 + f * (i - 1));
			double cmp = cost + x / (2 + f * i);
			if(cmp > ans) break;
			ans = cmp;
		}
		printf("Case #%d: %.9lf\n", ++ca, ans);
	}
}