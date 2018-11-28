#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <deque>
#include <set>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin); freopen("output.txt","w",stdout);
	int i,N,k,j,n,m,l;
	cin>>N;
	int a[11][11];
	for (k=1; k<=N; k++)
	{
		cout<<"Case #"<<k<<": ";
		cin>>n>>m;
		for (i=0; i<n; i++)
			for (j=0; j<m; j++)
				cin>>a[i][j];
		bool flag=1;
		for (i=0; i<n; i++)
			for (j=0; j<m; j++)
				if (a[i][j]==1 && flag)
				{
					for (l=0; l<m; l++) if (a[i][l]==2) flag=0;
					if (!flag)
					{
						flag=1;
						for (l=0; l<n; l++) if (a[l][j]==2) flag=0;
					}
				}
		if (flag) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}