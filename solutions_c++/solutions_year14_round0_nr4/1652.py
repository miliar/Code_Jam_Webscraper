#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr)
#define X first
#define Y second
#define PB push_back
#define MP make_pair
double a[1111],b[1111];
bool vis[1111];
int main() {
	int Z,n;
	cin>>Z;
	rep(z,Z){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(vis,false,sizeof(vis));
		cin>>n;
		rep(i,n)cin>>a[i];
		rep(i,n)cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: ", z+1);
		int res=0,zuo=0,you=n-1;
		rep(i,n){
			if(a[i]>b[zuo]){
				++zuo;
				++res;
			}else{
				--you;
			}
		}
		printf("%d", res);
		res=0,zuo=0;
		rep(i,n){
			double t=a[i];
			bool fla=true;
			rep(j,n){
				if(t<b[j]&&!vis[j]){
					vis[j]=true;
					fla=false;
					break;
				}
			}
			if(fla){
				++res;
				while(vis[zuo])++zuo;
				vis[++zuo]=true;
			}
		}
		printf(" %d\n", res);
	}
 	return 0;
}
