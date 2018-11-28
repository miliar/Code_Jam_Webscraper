#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
    freopen("outputbl1.in","w",stdout);
	int m,n,i,j,a[100][100],max1[100],max2[100],f,t;
	cin>>t;
	int r=0;
	while(t)
	{r++;
	cin>>n>>m;
	f=1;
	for(i=0;i<n;i++)
	{	max1[i]=0;
		for(j=0;j<m;j++)
		{
			cin>>a[i][j];
			if(max1[i]<=a[i][j]) max1[i]=a[i][j];
		}
	}
		for(i=0;i<m;i++)
	{	max2[i]=0;
		for(j=0;j<n;j++)
		{	
			if(max2[i]<=a[j][i]) max2[i]=a[j][i];
		}
	}
	
	for(i=0;i<n&&f!=0;i++)
	{
		for(j=0;j<m&&f!=0;j++)
		{		if(a[i][j]<max1[i])
				{
					for(int k=0;k<n;k++)
					{	
						if(a[k][j]>a[i][j]) {f=0; break;					}
					}
				}
		}
	}
	
	for(i=0;i<m&&f!=0;i++)
	{
		for(j=0;j<n&&f!=0;j++)
		{
				if(a[j][i]<max2[i])
				{
					for(int k=0;k<m;k++)
					{
						if(a[j][k]>a[j][i]) { f=0; break;					}
					}
				}
		}
	}
	cout<<"Case #"<<r<<": ";
	if(f==1) cout<<"YES";
	else cout<<"NO";
	cout<<endl;
	t--;}
return 0;}
