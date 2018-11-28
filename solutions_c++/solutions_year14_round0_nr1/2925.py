#include<iostream>
#include<cstdio>
#include<conio.h>
#include<stdlib.h>
using namespace std;
int main()
{freopen("A-small-attempt3.in","r",stdin);
freopen("out.txt","w",stdout);
	int t,n1,n2,arr1[5][5],arr2[5][5],i,j,a1[5],a2[5],save,p;
	cin>>t;
	for(p=1;p<=t;p++)
	{int c=0;
		cin>>n1;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>arr1[i][j];
			}
		}
		for(i=1;i<=4;i++)
		{
			a1[i]=arr1[n1][i];
		}
		cin>>n2;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>arr2[i][j];
			}
		}
		for(i=1;i<=4;i++)
		{
			a2[i]=arr2[n2][i];
		}
		for(i=1;i<=4;i++)	
		{
			for(j=1;j<=4;j++)
			{if(a1[i]==a2[j])
			{
				c++;
				save=a1[i];
			}
			}
		}
		if(c==1)
			cout<<"Case #"<<p<<	": "<<save<<"\n";
		else if(c==0)	
			cout<<"Case #"<<p<<	": "<<"Volunteer cheated!\n";
		else if(c>1)
			cout<<"Case #"<<p<<	": "<<"Bad magician!\n";
	}
	getch();
	return 0;
}