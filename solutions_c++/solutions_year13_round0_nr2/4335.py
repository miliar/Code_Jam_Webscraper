#include<stdio.h>
int w[110][110],n,m,i,TC,T,t,j,k,M;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&TC);
	while(T<TC){
		printf("Case #%d: ",++T);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)for(j=0;j<m;j++)scanf("%d",&w[i][j]);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				M=0;
				t=100;
				for(k=0;k<m;k++)if(M<w[i][k])M=w[i][k];
				if(t>M)t=M;
				M=0;
				for(k=0;k<n;k++)if(M<w[k][j])M=w[k][j];
				if(t>M)t=M;
				if(t!=w[i][j])break;
			}
			if(j!=m)break;
		}
		if(i!=n)printf("NO\n");
		else printf("YES\n");
	}
}