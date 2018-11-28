#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main()
{
	int j,t,k,c,ans1,ar1[5][5],i,el,ans2,ar2[5][5];
	freopen("x.txt","rt",stdin);
	cin>>t;
for(i=1;i<=t;i++)
{
	c=0;
	cin>>ans1;
	for(j=1;j<=4;j++)
	{
		for(k=1;k<=4;k++)
		{
			cin>>ar1[j][k];
		}
	}
	cin>>ans2;
	for(j=1;j<=4;j++)
	{
		for(k=1;k<=4;k++)
		{
			cin>>ar2[j][k];
		}
	}
	for(j=1;j<=4;j++)
	{
		for(k=1;k<=4;k++)
		{
			if(ar1[ans1][j]==ar2[ans2][k])
			{
				el=ar1[ans1][j];
				c++;		
			}
		}
	}
	if(c==0)
	cout<<"Case #"<<i<<": "<<"Volunteer cheated!\n";
	else if(c==1)
	cout<<"Case #"<<i<<": "<<el<<endl;
	else
	cout<<"Case #"<<i<<": "<<"Bad magician!\n";
			
}
	return 0;
}

