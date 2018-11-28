#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	freopen("D://B-large.in","r",stdin);
	freopen("D://output.txt","w",stdout);
	int i, j, k, l, M, N, t;
	cin >> l;
	vector<vector<int> > x;
	for(k=1;k<=l;k++)
	{
		printf("Case #%d: ",k);
		cin >> N >> M;
		x.resize(N);
		for(i=0;i<N;i++)
		{
			x[i].resize(M);
		}
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				scanf("%d",&x[i][j]);
			}
		}
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				for(t=0;t<N;t++)
				{
					if(x[t][j]>x[i][j])
					{
						break;
					}
				}
				if(t==N)
				{
					continue;
				}
				for(t=0;t<M;t++)
				{
					if(x[i][t]>x[i][j])
					{
						break;
					}
				}
				if(t!=M)
				{
					break;
				}
			}
			if(j!=M)
			{
				break;
			}
		}
		if(i!=N)
		{
			cout << "NO\n";
		}
		else
		{
			cout << "YES\n";
		}
	}
	return 0;
}