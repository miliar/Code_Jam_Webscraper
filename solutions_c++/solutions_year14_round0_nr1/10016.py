#include<iostream>
using namespace std;
int main ()
{ int a[4][4],T,x=0,p[4],q[4],r1=1,r2=1,y=0,ct=0;
	cin>>T;
	while(x!=T)
	{ ct=0;
		cin>>r1;
		
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
			cin>>a[i][j];
			p[j]=a[r1][j];
			}
		}
		cin>>r2;
		for(int m=1;m<=4;m++)
		{
			for(int n=1;n<=4;n++)
			{
			cin>>a[m][n];
			q[n]=a[r2][n];
			}
		}
		for (int l=1;l<=4;l++)
		{for (int k=1;k<=4;k++)
		{if (p[l]==q[k])
		{y=p[l];
			ct++;}
		}}
			switch(ct)
			{ case 0: cout<<"Case #"<<x+1<<": Volunteer cheated!\n";
				break;
				case 1: cout<<"Case #"<<x+1<<": "<<y<<"\n";
				break;
				default: cout<<"Case #"<<x+1<<": Bad magician!\n";
				
			}
				
	x++;
}
		
			
return 0;
}

