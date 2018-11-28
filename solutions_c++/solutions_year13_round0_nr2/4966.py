#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	freopen("2input.txt","r",stdin);
	freopen("2output.txt","w",stdout);
	int t,i,j,n,m,in,a[100][100],rmin[100],rcol[100],min1;
	for(in = 1, scanf("%d",&t);t--;in++)
	{
		scanf("%d%d",&n, &m);
		memset(a,0,sizeof(a));
		for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		scanf("%d",&a[i][j]);
		printf("Case #%d: ",in);
		for(i=0;i<n;i++)
		{
			min1 = -1;
			for(j=0;j<m;j++)if(a[i][j]>min1)min1 = a[i][j];
			rmin[i] = min1;
		}
		for(i=0;i<m;i++)
		{
			min1 = -1;
			for(j=0;j<n;j++)if(a[j][i]>min1)min1 = a[j][i];
			rcol[i] = min1;
		}
		bool f = false;
		for(i=0;i<n;i++)
		{for(j=0;j<m;j++)
		{
			if(a[i][j]!=rcol[j]&&a[i][j]!=rmin[i]){
				f = true;
				break;
			}
		}
		if(f)break;
		}
		if(f)cout <<"NO\n";
		else cout << "YES\n";
	}
}
