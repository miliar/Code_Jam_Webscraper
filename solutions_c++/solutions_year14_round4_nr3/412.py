#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

bool r[111][555];
const int dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
int w,h;
inline int convert(int i,int j,int k){
	return (i-1)*h+(j-1)+(k==0?0:w*h);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ti,b,i,j,k,x0,y0,x1,y1,nx,ny,here,there,l,len,tmp,ans;
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		scanf("%d%d%d",&w,&h,&b);
		vector<vector<int>> c(w*h*2);
		for(i=1;i<=w;i++){
			for(j=1;j<=h;j++){
				r[i][j]=0;
			}
		}
		for(i=1;i<=w;i++){
			r[i][0]=1;
			r[i][h+1]=1;
		}
		for(i=1;i<=h;i++){
			r[0][i]=1;
			r[w+1][i]=1;
		}
		for(k=0;k<b;k++){
			scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
			x0++; y0++; x1++; y1++;
			for(i=x0;i<=x1;i++){
				for(j=y0;j<=y1;j++){
					r[i][j]=1;
				}
			}
		}
		for(i=1;i<=w;i++){
			for(j=1;j<=h;j++){
				if(r[i][j]==0){
					c[convert(i,j,0)].push_back(convert(i,j,1));
					here=convert(i,j,1);
					for(k=0;k<4;k++){
						nx=i+dx[k]; ny=j+dy[k];
						if(r[nx][ny]==0){
							there = convert(nx,ny,0);
							c[here].push_back(there);
						}
					}
				}
			}
		}

		ans=0;
		for(l=1;l<=w;l++){
			queue<int> q;
			vector<int> parent(w*h*2,-1);
			q.push(convert(l,1,0));
			while(!q.empty()){
				here = q.front();
				if(here%h==h-1) break;
				q.pop();
				len = c[here].size();
				for(i=0;i<len;i++){
					there=c[here][i];
					if(parent[there]==-1){
						q.push(there);
						parent[there]=here;
					}
				}
			}
			if(q.empty()) continue;
			for(tmp=here;tmp%h>0;tmp=parent[tmp]){
				here = parent[tmp];
				there = tmp;
				len = c[here].size();
				for(i=0;i<len;i++){
					if(c[here][i]==there){
						c[here].erase(c[here].begin()+i);
						c[there].push_back(here);
						break;
					}
				}
			}
			ans++;
		}
		printf("Case #%d: %d\n",ti,ans);
	}
}