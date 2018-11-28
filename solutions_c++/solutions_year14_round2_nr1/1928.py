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
		bool br=0;
		int n;
		cin>>n;
		string s,S="";
		vector<vector<int> >v(n);
		cin>>s;
		v[0].pb(1);
		S+=s[0];
		rep(j,s.sz-1) {
			if (s[j]==s[j+1]) v[0][v[0].sz-1]++;
			else {
				v[0].pb(1);
				S+=s[j+1];
			}
		}
		rep(i,n-1) {
			cin>>s;
			if (S[0]!=s[0]) {
				br=1;
				break;
			}
			v[i+1].pb(1);
			rep(j,s.sz-1) {
				if (s[j]==s[j+1]) v[i+1][v[i+1].sz-1]++;
				else {
					v[i+1].pb(1);
					if (v[i+1].sz>S.sz || s[j+1]!=S[v[i+1].sz-1]) {
						br=1;
						break;
					}
				}
			}
			if (v[i+1].sz!=S.sz) br=1;
			if (br) break;
		}
		if (br) printf("Case #%d: Fegla Won\n",t+1);
		else {
			int ans=0;
			rep(i,v[0].sz) {
				int a=0,b=INF;
				rep(j,n) {
					a=max(v[j][i],a);
				}
				for(int l=1; l<=a; l++) {
					int bb=0;
					rep(j,n) {
						bb+=abs(v[j][i]-l);
					}
					b=min(b,bb);
				}
				ans+=b;
			}
			printf("Case #%d: %d\n",t+1,ans);
		}
	}
	return 0;
}