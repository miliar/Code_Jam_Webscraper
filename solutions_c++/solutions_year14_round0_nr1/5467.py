#include<iostream>
using namespace std;
int main()
{int ar[4][4];
int a[17];
int t,c1,c2;
cin>>t;
for(int i=0;i<t;i++)
{cin>>c1;
c1--;

for(int j=0;j<4;j++)
	{for(int k=0;k<4;k++)
		{cin>>ar[j][k];
		}
	}
for(int j=0;j<17;j++)
	a[j]=0;
for(int j=0;j<4;j++)
	a[ar[c1][j]]++;

cin>>c1;
c1--;

for(int j=0;j<4;j++)
	{for(int k=0;k<4;k++)
		{cin>>ar[j][k];
		}
	}

for(int j=0;j<4;j++)
	a[ar[c1][j]]++;
int c=0;c2=0;
for(int j=0;j<17;j++)
	{if(a[j]==2)
		{c++;c1=j;}

	}
if(c>1)
	cout<<"Case #"<<i+1<<":"<<" Bad magician!\n";

if(c==0) 
	cout<<"Case #"<<i+1<<":"<<" Volunteer cheated!\n";
if(c==1)
	cout<<"Case #"<<i+1<<":"<<" "<<c1<<endl;

	
}	
}
