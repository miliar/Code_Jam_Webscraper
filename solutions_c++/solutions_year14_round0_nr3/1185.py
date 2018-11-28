#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <climits>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9

using namespace std;
int r,c;
char v[10][10];bool vis[10][10];
int dx[8]={1,-1,0,0,1,-1,1,-1};
int dy[8]={0,0,1,-1,1,-1,-1,1};
void fill(){
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(v[i][j]!='.')continue;
			int cnt=0;
			for(int k=0;k<8;k++){
				int x=i+dx[k],y=j+dy[k];
				if(x<0 || y<0 || x>=r || y>=c)continue;
				cnt+=(v[x][y]=='*');
			}
			v[i][j]=char(cnt+'0');
		}
	}
}
void check(int x,int y){
	if(vis[x][y])return;
	vis[x][y]=1;
	for(int i=0;i<8;i++){
		int a=x+dx[i],b=y+dy[i];
		if(a<0 || b<0 || a>=r || y>=c)continue;
		if(v[a][b]=='*')continue;
		if(v[a][b]=='0')check(a,b);
		vis[a][b]=1;
	}
}
void disp(int x,int y){
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(i==x && j==y)cout<<'c';
			else{
				if(v[i][j]=='*')cout<<'*';
				else cout<<'.';
			}
		}
		cout<<endl;
	}
}
int main()
{
	freopen("C-small-attempt6.in","r",stdin);
	freopen("C-small-attempt6.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		int m;cin>>r>>c>>m;int n=r*c;
		cout<<"Case #"<<++cs<<":"<<endl;
		if(m==n-1){
			bool check=true;
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					if(check)cout<<'c',check=false;
					else cout<<'*';
				}
				cout<<endl;
			}
			continue;
		}
		for(int mask=0;mask<(1<<(n));mask++){
			if(__builtin_popcount(mask)!=m)continue;
			int ind=0;
			for(int i=0;i<r;i++)for(int j=0;j<c;j++){if(mask & (1<<ind))v[i][j]='*';else v[i][j]='.';ind++;}
			fill();
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					if(v[i][j]!='0')continue;
					memset(vis,0,sizeof(vis));
					check(i,j);bool ok=true;
					for(int a=0;a<r;a++){
						for(int b=0;b<c;b++){
							if(v[a][b]!='*' && !vis[a][b]){
								ok=false;break;
							}
						}
						if(!ok)break;
					}
					if(ok){disp(i,j);goto end;}
				}
			}
		}
		cout<<"Impossible"<<endl;
		end:;
	}
	return 0;
}
