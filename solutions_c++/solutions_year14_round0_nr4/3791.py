#include <iostream>  
#include <algorithm>  
#include <cmath>  
#include <vector>  
#include <string>  
#include <ctime>
#include <iomanip>
using namespace std;  

double m,k,q,s,a[1010],b[1010];
int i,j,w,v,n,x,y;
int war(),deceitful_war();

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;
	v=w;
	while(w--)
	{
		cin>>n;
		for(i=1;i<=n;i++)
			cin>>a[i];
		for(i=1;i<=n;i++)
			cin>>b[i];
		
		sort(a+1,a+1+n);
		sort(b+1,b+1+n);
		 
		x=war();
		y=deceitful_war();
		cout<<"Case #"<<v-w<<": "<<y<<" "<<x<<endl;
	}
	return 0;
}

int war()
{
		int x=0,i=0,j=0;
		bool markwar[1010];

		for(i=1;i<=1000;i++)
			markwar[i]=0;

		for(i=1;i<=n;i++)
		{
			if(markwar[n]==1 || j==n+1)
			{
				x++;
				continue;
			}
			for(j=1;j<=n;j++)
			{
				if(a[i]<b[j] && markwar[j]==0)
				{
					markwar[j]=1;
					break;
				}
			}
			if(j==n+1)
				x++;
		}
		return x;
}
int deceitful_war()
{
	int i=1,j=1,x=0;
	while(i<=n)
	{
		if(a[i]>b[j])
		{
			j++;
			x++;
		}
		i++;
	}
	return x;
}
