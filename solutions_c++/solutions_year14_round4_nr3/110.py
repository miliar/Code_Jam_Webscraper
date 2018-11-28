#include <cstdio>
#include <algorithm>
using namespace std;
const int NMax=1000;
int W,H,N;
int X0[NMax],Y0[NMax],X1[NMax],Y1[NMax];
int dist[NMax];
int D[NMax][NMax];
int getdist(int j,int k){
	int d1=max(max(X0[k]-X1[j],X0[j]-X1[k])-1,0);
	int d2=max(max(Y0[k]-Y1[j],Y0[j]-Y1[k])-1,0);
	return max(d1,d2);
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		fprintf(stderr,"Case=%d\n",Case);
		scanf("%d%d%d",&W,&H,&N);
		for (int i=0;i<N;i++){
			scanf("%d%d%d%d",X0+i,Y0+i,X1+i,Y1+i);
		}
		//printf("%d\n",getdist(0,1));
		for (int i=0;i<N;i++){
			dist[i]=X0[i];
		}
		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
				D[i][j]=getdist(i,j);
		for (int i=0;i<N;i++){
			for (int j=0;j<N;j++)
				for (int k=0;k<N;k++)
					dist[j]=min(dist[j],dist[k]+D[j][k]);
		}
		int ans=W;
		for (int i=0;i<N;i++)
			ans=min(ans,dist[i]+W-1-X1[i]);
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}

