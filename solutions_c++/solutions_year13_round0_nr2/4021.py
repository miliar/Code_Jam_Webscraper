#include<iostream>
#define MAXH 100
#define MAXN 100
#define MAXM 100
using namespace std;
int main()
{
	int T,i,j,k,now[MAXN][MAXM],map[MAXN][MAXM],N,M,maxh;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	cin>>T;
	for (i=0;i<T;i++)
	{
		cin>>N>>M;
		maxh=0;
		for (j=0;j<N;j++)
			for (k=0;k<M;k++)
			{
				cin>>map[j][k];
				if (map[j][k]>maxh) maxh=map[j][k];
			}
		cout<<"Case #"<<i+1<<": ";
		for (j=0;j<N;j++)
			for (k=0;k<M;k++)
				now[j][k]=maxh;
		for (;maxh>=0;maxh--)
		{
			for (j=0;j<N;j++)
			{
				for (k=0;k<M;k++)
					if (map[j][k]>maxh) break;
				if (k==M)
					for (k=0;k<M;k++)
						now[j][k]=maxh;
			}
			for (j=0;j<M;j++)
			{
				for (k=0;k<N;k++)
					if (map[k][j]>maxh) break;
				if (k==N)
					for (k=0;k<N;k++)
						now[k][j]=maxh;
			}
		}
		for (j=0;j<N*M;j++)
			if (now[j/M][j%M]!=map[j/M][j%M]) break;
		if (j==N*M) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}