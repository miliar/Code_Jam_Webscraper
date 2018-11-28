#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	int n,m,t,x;
	
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
	scanf("%d",&t);
	for (x=1;x<=t;++x)
	{
		int a[103][104];
		scanf("%d %d",&n,&m);
		int i,j;
		vector <pair<int,int> > v[109];
		for (i=1;i<=n;++i)
			for (j=1;j<=m;++j)
			{
				scanf("%d",&a[i][j]);
				v[a[i][j]].push_back(make_pair(i,j));
			}
		int ok=1;	
		for (int val=1;val<101 && ok;++val)
			for (vector<pair<int,int> >::iterator it=v[val].begin();it!=v[val].end();++it)
				if (a[(*it).first][(*it).second]==val)
				{
					int l=(*it).first,c=(*it).second;
					for (i=1;i<=n;++i)
						if (a[i][c]>val) 
							break;
					if (i>n)
					{
						for (i=1;i<=n;++i)
							a[i][c]=0;
						continue;
					}
					for (j=1;j<=m;++j)
						if (a[l][j]>val)
							break;
					if (j>m)
					{
						for (j=1;j<=m;++j)
							a[l][j]=0;
						continue;
					}
					ok=0;
				}
			
		if (!ok)		
			printf("Case #%d: NO\n",x); 	else
				printf("Case #%d: YES\n",x);
	}
return 0;
}
				
				
						
						
				
		
		