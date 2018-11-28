#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
vector<int> v[27];
int T,r,c,m;
int a[50][50];
bool have[50][50];
int ansi,ansj;
bool got;
int dir[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};

int shuyi(int x){
	int ret=0;
	while(x){
		if(x%2) ret++;
		x/=2;
	}
	return ret;
}
void init(int x){
	memset(a,0,sizeof(a));
	//cout<<"init  :"<<x<<endl;
	for (int i=1;i<=r;i++){
		for (int j=1;j<=c;j++){
			if(x%2) a[i][j]=-1;
			else a[i][j]=0;
			x=x/2;
		}
	}
	for (int i=1;i<=r;i++){
		for (int j=1;j<=c;j++){
			if(a[i][j]!=-1)
			for (int k=0;k<8;k++){
			   if(a[i+dir[k][0]][j+dir[k][1]]==-1) a[i][j]++;
			}
			//cout<<a[i][j]<<' ';
		}
		//cout<<endl;
	}
}
int tol;
void find(int x,int y){
	//cout <<x<<' '<<y<<' '<<tol<<" diyq"<<endl;
	if(tol==r*c-m) {got=true;return;}
	if(x<=0||y<=0||x>r||y>c||a[x][y]==-1||have[x][y]) return ;
	have[x][y]=true;
	if(a[x][y]!=-1)tol++;
	if(tol==r*c-m) {got=true;return;}
	//cout<<x<<' '<<y<<' '<<tol<<endl;
	if(a[x][y]==0)
	for (int i=0;i<8;i++){
		find(x+dir[i][0],y+dir[i][1]);
	}
}
void work(){
	//cout<<"work:  "<<endl;
	for (int i=1;i<=r;i++){
		for (int j=1;j<=c;j++){
			if(a[i][j]==-1) continue;
			ansi=i;ansj=j;
			memset(have,0,sizeof(have));
			tol=0;
			find(i,j);
			//cout<<tol<<endl;
			if(got) return ;
		}
	}
}
int main(){
	for (int i=0;i<25;i++) v[i].clear();
	for (int i=0;i<(1<<25);i++){
		v[shuyi(i)].push_back(i);
	}
	//cout<<"wanle"<<endl;
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d%d%d",&r,&c,&m);
		got=false;
		for (int i=0;i<v[m].size();i++){
			if(v[m][i]>=(1<<r*c)) break;
			init(v[m][i]);
		    work();
			if(got) break;
		}
		printf("Case #%d:\n",ca++);
		if(got){
			for (int i=1;i<=r;i++){
				for (int j=1;j<=c;j++){
					if(i==ansi&&j==ansj)printf("c");
					else {
						if(a[i][j]>=0) printf(".");
						else printf("*");
					}
				}
				cout<<endl;
			}
		}
		else {
			printf("Impossible\n");
		}
	}
	return 0;
}
