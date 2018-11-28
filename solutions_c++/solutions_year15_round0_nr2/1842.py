#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<list>
#include<bitset>
#include<ctime>
using namespace std;

typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi=acos(-1.0);

int a[10009];

int main() {
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(t_,1,t) {
        int n;cin>>n;
        FOR(i,1,n) cin>>a[i];
        int ans=inf;
        FOR(h, 1, 1000) {
            int f=0;

            FOR(i,1,n) {
                f+=(a[i]+h-1)/h-1;
            }

            ans=min(ans, f+h);
        }
        cout<<"Case #"<<t_<<": "<<ans<<endl;
	}
}
