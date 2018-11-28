#include<iostream>
#include<stdio.h>
#include<string>
#include<cstdio>
#include <sstream>
#include <cmath>
using namespace std;

void draw(int r,int c,int u[5][5])
{
	if(r>c)
	{
		for(int rr=0;rr<r;rr++)
	{
		cout<<endl;
		for(int cc=0;cc<c;cc++)
		{
			if(u[cc][rr]==0)
				cout<<"*";
			else if(u[cc][rr]==1)
				cout<<".";
			else
				cout<<"c";
			
		}
		
	}
	}
	else{
	for(int rr=0;rr<r;rr++)
	{
		cout<<endl;
		for(int cc=0;cc<c;cc++)
		{
			if(u[rr][cc]==0)
				cout<<"*";
			else if(u[rr][cc]==1)
				cout<<".";
			else
				cout<<"c";
			
		}
		
	}
	}
	cout<<endl;

}
void main()
{
	freopen("C-small-attempt5.in", "r", stdin);
	freopen("C-small-5.out", "w", stdout);
	int t;cin>>t;
	for(int ti=1;ti<=t;++ti)
	{
		int r0,c0,m;
		cin>>r0>>c0>>m;
		int r,c;
		if(r0>c0)
		{
			r=c0;
			c=r0;
		}
		else
		{
			r=r0;
			c=c0;}

		int u[5][5]={0};
		int possible=0;
		int empty=r*c-m;
		if(empty==1)
		{	u[0][0]=2;
		possible=1;
		}

		
		else if(empty==0)
			possible=0;
		else if(r==1)
		{
			possible=1;
			u[0][0]=2;
			for(int j=1;j<empty;j++)
				u[0][j]=1;
		}
		else if(empty>=4&&empty%2==0&&empty<=2*c)
		{
			possible=1;
			for(int j=0;j<empty/2;j++)
			{u[0][j]=1;u[1][j]=1;}
			u[0][0]=2;
		}
		else if(empty>=9&&empty%3==0&&empty<=3*c&&r>=3)
		{
			possible=1;
			for(int j=0;j<empty/3;j++)
			{u[0][j]=1;u[1][j]=1;u[2][j]=1;}
			u[0][0]=2;
		}
		else if(empty>=16&&empty%4==0&&empty<=4*c)
		{
			possible=1;
			for(int j=0;j<empty/4;j++)
			{u[0][j]=1;u[1][j]=1;u[2][j]=1;u[3][j]=1;}
			u[0][0]=2;
		}
		else if(empty==25)
		{
			possible=1;
			for(int j=0;j<5;j++)
			{u[0][j]=1;u[1][j]=1;u[2][j]=1;u[3][j]=1;u[4][j]=1;}
			u[0][0]=2;
			
		}
		else if(empty==8)
		{
			possible=1;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
					u[i][j]=1;
			}
			u[2][2]=0;
			u[0][0]=2;
		}
		else if(empty==10)
		{
			possible=1;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<4;j++)
					u[i][j]=1;
			}
			u[2][3]=0;
			u[2][2]=0;
			u[0][1]=2;
		}
		else if(empty==11)
		{
			possible=1;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<4;j++)
					u[i][j]=1;
			}
			u[2][3]=0;
			u[1][1]=2;
		}
		else if(empty==13&&c==5)
		{
			possible=1;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<5;j++)
					u[i][j]=1;
			}
			u[2][3]=0;
			u[2][4]=0;
			u[1][1]=2;
		}
		else if(empty==13&&c==4)
		{
			possible=1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					u[i][j]=1;
			}
			u[3][3]=0;
			u[3][2]=0;
			u[2][3]=0;
			u[1][1]=2;
		}

		else if(empty==14&&c==5)
		{
			possible=1;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<5;j++)
					u[i][j]=1;
			}
			u[2][4]=0;
			u[1][2]=2;
		}
		else if(empty==14&&c==4)
		{
			possible=1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					u[i][j]=1;
			}
			u[3][3]=0;
			u[2][3]=0;
			u[1][1]=2;
		}
			else if(empty==15&&c==4)
		{
			possible=1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					u[i][j]=1;
			}
			u[3][3]=0;
			u[1][1]=2;
		}
		else if(empty>=17&&empty<=19)
		{
			possible=1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<5;j++)
					u[i][j]=1;
			}
			for(int i=0;i<20-empty;i++)
				u[3][4-i]=0;

			u[0][1]=2;
		}
		else if(empty==21)
		{
			possible=1;
			
			for(int i=0;i<5;i++)
			{
				for(int j=0;j<5;j++)
					u[i][j]=1;
			}
			u[4][4]=0;
			u[4][3]=0;
			u[3][4]=0;
			u[3][3]=0;
			u[1][1]=2;
		}
		else if(empty>21)
		{
			possible=1;
			
			for(int i=0;i<5;i++)
			{
				for(int j=0;j<5;j++)
					u[i][j]=1;
			}
			
			for(int i=0;i<25-empty;i++)
				u[4][4-i]=0;
			u[0][0]=2;
		}












		

		

		cout<<"Case #"<<ti<<":";
		//cout<<r0<<"¡¡"<<c0<<"  "<<m;
		if(possible==1)
		{
	
			draw(r0,c0,u);
		}
		else if(possible==0)
		{cout<<endl;cout<<"Impossible"<<endl;}
	
	}
}
