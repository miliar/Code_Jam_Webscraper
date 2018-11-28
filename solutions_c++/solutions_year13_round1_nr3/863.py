#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<ctime>

using namespace std;

map<int,int> v;
int R,N,M,K;
void solv()
{
	for(int i=2;i<=M;i++)
		for(int j=i;j<=M;j++)
			for(int k=j;k<=M;k++)
			{
				vector<int> a;
				if(N>=1)
					a.push_back(i);
				if(N>=2)
					a.push_back(j);
				if(N>=3)
					a.push_back(k);
				int cnt = 0;
				map<int,int> vv = v;
				for(int c=0;c<(1<<a.size());c++)
				{
					int rs = 1;

					for(int z=0;z<a.size();z++)
					{
						if( (1<<z) & c )
							rs*=a[z];
					}
					if( vv[rs] )
					{
						vv[rs] = 0;
						cnt++;
					}
				}
				if(cnt >= v.size() )
				{
					for(int i=0;i<a.size();i++)
						printf("%d",a[i]);
					printf("\n");
					return ;
				}

			}
		for(int i=0;i<N;i++)
			printf("2");
		printf("\n");
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out_C.txt","wt",stdout);
	int TC;
	scanf("%d",&TC);
	int kk,x;
	for(int tc =1; tc<=TC;tc++)
	{
		scanf("%d %d %d %d",&R,&N,&M,&K);
		printf("Case #1:\n");
		for(int r=0;r<R;r++)
		{
			v.clear();
			for(int i=0;i<K;i++)
			{
				scanf("%d",&x);
				
				v[x] = true;
			}
			solv();
		}
	}
	return 0;
}