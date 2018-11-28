#include<stdio.h>
#include<queue>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<int,int> > g[5000];
int ijk[5000];
int v[5000];
int x0[5000];
int x1[5000];
int y0[5000];
int y1[5000];
int X[5000];
int Y[5000];
inline int ABS(int a){return max(a,-a);}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		for(int i=0;i<5000;i++){
			g[i].clear();
			v[i]=0;
			ijk[i]=999999999;
		}
		for(int i=0;i<c;i++){
			scanf("%d%d%d%d",x0+i,y0+i,x1+i,y1+i);
			x1[i]++;y1[i]++;
		}
		for(int i=0;i<c;i++){
			X[i*4]=x0[i];
			Y[i*4]=y0[i];
			X[i*4+1]=x0[i];
			Y[i*4+1]=y1[i];
			X[i*4+2]=x1[i];
			Y[i*4+2]=y0[i];
			X[i*4+3]=x1[i];
			Y[i*4+3]=y1[i];
		}
		for(int i=0;i<c;i++){
			for(int j=i+1;j<c;j++){
				int d=999999999;
				for(int k=0;k<4;k++){
					if(X[j*4+k]>=x1[i]){
						if(Y[j*4+k]>y1[i])d=min(d,max(ABS(x1[i]-X[j*4+k]),ABS(y1[i]-Y[j*4+k])));
						else if(Y[j*4+k]<y0[i])d=min(d,max(ABS(x1[i]-X[j*4+k]),ABS(y0[i]-Y[j*4+k])));
						else d=min(d,ABS(x1[i]-X[j*4+k]));
					}else if(X[j*4+k]<=x0[i]){
						if(Y[j*4+k]>y1[i])d=min(d,max(ABS(x0[i]-X[j*4+k]),ABS(y1[i]-Y[j*4+k])));
						else if(Y[j*4+k]<y0[i])d=min(d,max(ABS(x0[i]-X[j*4+k]),ABS(y0[i]-Y[j*4+k])));
						else d=min(d,ABS(x0[i]-X[j*4+k]));
					}else{
						if(Y[j*4+k]>=y1[i])d=min(d,ABS(y1[i]-Y[j*4+k]));
						else if(Y[j*4+k]<=y0[i])d=min(d,ABS(y0[i]-Y[j*4+k]));
					}
				}
				for(int k=0;k<4;k++){
					if(X[i*4+k]>=x1[j]){
						if(Y[i*4+k]>y1[j])d=min(d,max(ABS(x1[j]-X[i*4+k]),ABS(y1[j]-Y[i*4+k])));
						else if(Y[i*4+k]<y0[j])d=min(d,max(ABS(x1[j]-X[i*4+k]),ABS(y0[j]-Y[i*4+k])));
						else d=min(d,ABS(x1[j]-X[i*4+k]));
					}else if(X[i*4+k]<=x0[j]){
						if(Y[i*4+k]>y1[j])d=min(d,max(ABS(x0[j]-X[i*4+k]),ABS(y1[j]-Y[i*4+k])));
						else if(Y[i*4+k]<y0[j])d=min(d,max(ABS(x0[j]-X[i*4+k]),ABS(y0[j]-Y[i*4+k])));
						else d=min(d,ABS(x0[j]-X[i*4+k]));
					}else{
						if(Y[i*4+k]>=y1[j])d=min(d,ABS(y1[j]-Y[i*4+k]));
						else if(Y[i*4+k]<=y0[j])d=min(d,ABS(y0[j]-Y[i*4+k]));
					}
				}
				if(d>1000)continue;
				g[i].push_back(make_pair(j,d));
				g[j].push_back(make_pair(i,d));
			}
		}
		for(int i=0;i<c;i++){
			g[c].push_back(make_pair(i,x0[i]));
			g[i].push_back(make_pair(c+1,a-x1[i]));
		}
		g[c].push_back(make_pair(c+1,a));
		priority_queue<pair<int,int> > Q;
		ijk[c]=0;
		Q.push(make_pair(0,c));
		while(Q.size()){
			int at=Q.top().second;
			int cost=-Q.top().first;
			Q.pop();
			if(v[at])continue;
			v[at]=1;
			for(int i=0;i<g[at].size();i++){
				if(!v[g[at][i].first]&&ijk[g[at][i].first]>cost+g[at][i].second){
					ijk[g[at][i].first]=cost+g[at][i].second;
					Q.push(make_pair(-ijk[g[at][i].first],g[at][i].first));
				}
			}
		}
	//	for(int i=0;i<n+2;i++)printf("(%d,%d): %d\n",X[i],Y[i],ijk[i]);
		printf("Case #%d: %d\n",t+1,ijk[c+1]);
	}
}