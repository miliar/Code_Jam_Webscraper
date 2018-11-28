#include<cstdio>
#include<set>
#include<iostream>
#include<map>
#include<cstring>
using namespace std;
const int maxn = 20;
int x,y;
int a[maxn][maxn];
int b[maxn][maxn];
int c[maxn];
void run(){
	map<int,int>s;
	int ans=-1;
	memset(c,0,sizeof(c));
	int i;
	--x,--y;
	for(i=0;i<4;++i){
		c[a[x][i]]++;
		c[b[y][i]]++;
		if(c[a[x][i]]==2)
		  ans=a[x][i];
		if(c[b[y][i]]==2)
		  ans=b[y][i];
	}
	int sz=0;
	for(i=0;i<20;++i){
		if(c[i])
		  ++sz;
	}
	//cout<<sz<<endl;
	if(sz<7){
		cout<<" Bad magician!"<<endl;
	}else if(sz>7){
		cout<<" Volunteer cheated!"<<endl;;
	}else{
		cout<<" "<<ans<<endl;
	}
}
int main(){
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int T;
	cin>>T;
	for(int cas=1;cas<=T;++cas){
		cin>>x;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin>>a[i][j];
			}
		}
		cin>>y;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin>>b[i][j];
			}
		}
		cout<<"Case #"<<cas<<":";
		run();
	}
	return 0;
}
