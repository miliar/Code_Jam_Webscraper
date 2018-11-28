#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define rep(i,n) for (int i=0; i<n; i++)
#define ll long long

using namespace std;

const int INF=~(1<<31);
const double EPS=1;
const double PI=3.141592653589793;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	rep(t,T) {
		ll a,b,k,ans=0;
		cin>>a>>b>>k;
		rep(i,a) {
			rep(j,b) {
				if ((i&j)<k) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}