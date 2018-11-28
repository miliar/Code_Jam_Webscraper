#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<map>
//#pragma GCC optimize("O2") 
#define pb push_back
#define mp make_pair
#define IOS ios_base::sync_with_stdio(false)
using namespace std;
int n; 
const int move[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
void read(int &x)
{
	char ch=getchar();x=0;
	for(;ch<'0'||ch>'9';ch=getchar());
	for(;ch>='0' && ch<='9';ch=getchar())x=x*10+ch-'0';
}
bool v[110][110];
int a[110][110];
char ch[110][110];
int r,c,z,ans;
void dfs(int x,int y,int z,int dep)
{
	if(v[x][y])
		return;
	v[x][y]=true;
	int x1,y1;
	x1=x+move[z][0];
	y1=y+move[z][1];
	while(x1>0 && x1<=r && y1>0 && y1<=c && a[x1][y1]==-1){
		x1=x1+move[z][0];
		y1=y1+move[z][1];
	}
	
	if(x1>0 && x1<=r && y1>0 && y1<=c){

		dfs(x1,y1,a[x1][y1],dep+1);
	}else{
		if(dep==1){
			bool ok=false;
			for(int i=0;i<=3;i++){
				x1=x+move[i][0];
				y1=y+move[i][1];
				while(x1>0 && x1<=r && y1>0 && y1<=c && a[x1][y1]==-1){
					x1=x1+move[i][0];
					y1=y1+move[i][1];
				}
				if(x1>0 && x1<=r && y1>0 && y1<=c && a[x1][y1]>=0){
					a[x][y]=i;
					ans++;
					ok=true;
					dfs(x1,y1,a[x1][y1],dep+1);
					break;
				}
				
			}
			if(!ok)ans=1000000000;
		}
		else{
			for(int i=0;i<=3;i++){
				x1=x+move[i][0];
				y1=y+move[i][1];
				while(x1>0 && x1<=r && y1>0 && y1<=c && a[x1][y1]==-1){
					x1=x1+move[i][0];
					y1=y1+move[i][1];
				}
				if(x1>0 && x1<=r && y1>0 && y1<=c && v[x1][y1]){
					a[x][y]=i;
					ans++;
					break;
				}
			}
		}
	}
}
					
		
void task()
{
	cin>>r>>c;
	ans=0;
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++){
			cin>>ch[i][j];
			if(ch[i][j]=='.')z=-1;
			if(ch[i][j]=='>')z=0;
			if(ch[i][j]=='<')z=1;
			if(ch[i][j]=='v')z=2;
			if(ch[i][j]=='^')z=3;
		 	a[i][j]=z; 
		}
	}
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++)
		if(ch[i][j]!='.'){
			memset(v,0,sizeof(v));
		
			dfs(i,j,a[i][j],1);
		}
	}
	if(ans<100000) cout<<ans<<endl;
	else cout<<"IMPOSSIBLE"<<endl;
		
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	IOS;
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		cout<<"Case #"<<i<<": ";
		task();
	}
}


