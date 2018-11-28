/* Vipul Jain */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
//#include <cmath>
//#include <algorithm>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FB(i,a,n) for(int i=(a);i>=(n);--i)
#define FI(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define Sf(x) scanf("%f",&x)
#define Sd(x) scanf("%lf",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define fi first
#define se second

int main()
{
	int t;
	S(t);
	int cases = 0;
	while (t--) {
		cases++;
		string ans = "";
		int x, r, c;
		cin >> x >> r >> c;
		if ((r * c) % x) {
			ans = "RICHARD";
		} else {
			if (x == 1) {
				ans = "GABRIEL";
			} else if (x == 2) {
				ans = "GABRIEL";
			} else if (x == 3) {
				if (r * c == 3) {
					ans = "RICHARD";
				} else {
					ans = "GABRIEL";
				}
			} else {
				if (r * c == 4 || r * c == 8) {
					ans = "RICHARD";
				} else {
					ans = "GABRIEL";
				}
			}
		}
		cout << "Case #" << cases << ": " << ans << endl;
	}
    return 0;
}