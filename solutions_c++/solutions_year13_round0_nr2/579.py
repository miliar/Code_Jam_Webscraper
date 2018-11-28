#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

int h,w;
int a[100][100];

bool cut[100][100];

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	rep(i,t){
		memset(cut,false,sizeof(cut));
		cin>>h>>w;
		set<int> s;
		rep(y,h)rep(x,w)cin>>a[y][x],s.insert(a[y][x]);
		while(!s.empty()){
			int c=*s.begin();
			s.erase(s.begin());
			rep(i,h){
				bool ok=true;
				rep(j,w){
					if(c<a[i][j]){
						ok=false;
						break;
					}
				}
				if(ok)rep(j,w)if(a[i][j]==c)cut[i][j]=true;
			}
			rep(i,w){
				bool ok=true;
				rep(j,h){
					if(c<a[j][i]){
						ok=false;
						break;
					}
				}
				if(ok)rep(j,h)if(a[j][i]==c)cut[j][i]=true;
			}
		}
		char *ans="YES";
		rep(y,h)rep(x,w)if(!cut[y][x])ans="NO";
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}