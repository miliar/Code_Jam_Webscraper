#include<iostream>
using namespace std;
int a[5][5];
int func(int c,int b)
{
	if(c>0&&b>0)
		return a[c][b];
	else if(c>0&&b<0)
		return -1*a[c][-1*b];
	else if(c<0&&b>0)
		return -1*a[-1*c][b];
	else if(c<0&&b<0)
		return a[-1*c][-1*b];
}
int call(char c)
{
	if(c=='i')
		return 2;
	else if(c=='j')
		return 3;
	else if(c=='k')
		return 4;
}
int main()
{
	int t;
	cin>>t;
	a[1][2]=2;
	a[1][3]=3;
	a[1][4]=4;
	a[4][1]=4;
	a[3][1]=3;
	a[2][1]=2;
	a[2][2]=-1;
	a[2][3]=4;
	a[2][4]=-3;
	a[3][2]=-4;
	a[3][3]=-1;
	a[3][4]=2;
	a[4][2]=3;
	a[4][3]=-2;
	a[4][4]=-1;
	for(int k=1;k<=t;k++)
	{
		int i,j,n,r;
		char b[10000];
		cin>>n;
		cin>>r;
		cin>>b;
		int tempr=r,tempi=n;
		int prev=1;
		int flag1=0,flag2=0,flag3=0;
		for(j=0;j<r;j++)
		{
			for(i=0;i<n;i++)
			{
				if(prev==2)
				{
					flag1=1;
					tempr=j;
					tempi=i;
					prev=1;
					break;
				}

				prev=func(prev,call(b[i]));
			}

			if(flag1==1)
				break;
		}
		prev=1;
		for(j=tempr;j<r;j++)
		{
			for(i=tempi;i<n;i++)
			{
				if(prev==3)
				{
					flag2=1;
					tempr=j;
					tempi=i;
					prev=1;
					break;
				}
				prev=func(prev,call(b[i]));
			
			}
			if(flag2==1)
				break;
			tempi=0;
			tempr=0;
		}
		for(j=tempr;j<r;j++)
		{
			for(i=tempi;i<n;i++)
			{
				prev=func(prev,call(b[i]));
			}
			tempi=0;
			tempr=0;
		}
		if(prev==4)
			flag3=1;
		if(flag1&&flag2&&flag3)
		cout<<"Case #"<<k<<": YES"<<endl;
		else
		cout<<"Case #"<<k<<": NO"<<endl;
	}
return 0;
}
