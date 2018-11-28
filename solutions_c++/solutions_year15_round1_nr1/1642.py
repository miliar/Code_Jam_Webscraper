#include<iostream>
using namespace std;
int T,N,m[10010];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int y,z,maxz;
	scanf("%d",&T);
	for(int k=1;k<=T;k++)
	{
		y=z=maxz=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%d",&m[i]);
		for(int i=0;i<N-1;i++)
		{
			if(m[i]-m[i+1]>0)
				y+=m[i]-m[i+1];
			if(m[i]-m[i+1]>maxz)
				maxz=m[i]-m[i+1];
		}
		for(int i=0;i<N-1;i++)
		{
			if(m[i]<maxz)
				z+=m[i];
			else z+=maxz;
		}
		printf("Case #%d: %d %d\n",k,y,z);

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}