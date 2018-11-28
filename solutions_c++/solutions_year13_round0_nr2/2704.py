#include<cstdio>
#include<cstring>

int n,m;
int v[111][111];
bool hor[111],ver[111];

int main(){
	int T;scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&v[i][j]);
		bool ans=true;
		for(int i=0;i<100&&ans;i++){
			memset(hor,true,sizeof hor);
			memset(ver,true,sizeof ver);
			for(int j=0;j<n;j++)
				for(int k=0;k<m;k++)
					if(v[j][k]>i)
						hor[j]=ver[k]=false;
			for(int j=0;j<n;j++)
				for(int k=0;k<m;k++)
					if(v[j][k]<=i&&!hor[j]&&!ver[k])
						ans=false;
		}
		printf("Case #%d: %s\n",_,ans?"YES":"NO");
	}

	return 0;
}