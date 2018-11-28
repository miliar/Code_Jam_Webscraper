#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int port[5][5][5];
	port[1][1][1]=2;
	port[1][1][2]=2;
	port[1][1][3]=2;
	port[1][1][4]=2;
	port[1][2][1]=2;
	port[1][2][2]=2;
	port[1][2][3]=2;
	port[1][2][4]=2;
	port[1][3][1]=2;
	port[1][3][2]=2;
	port[1][3][3]=2;
	port[1][3][4]=2;
	port[1][4][1]=2;
	port[1][4][2]=2;
	port[1][4][3]=2;
	port[1][4][4]=2;
	
	
	port[2][1][1]=1;
	port[2][1][2]=2;
	port[2][1][3]=1;
	port[2][1][4]=2;
	port[2][2][1]=2;
	port[2][2][2]=2;
	port[2][2][3]=2;
	port[2][2][4]=2;
	port[2][3][1]=1;
	port[2][3][2]=2;
	port[2][3][3]=1;
	port[2][3][4]=2;
	port[2][4][1]=2;
	port[2][4][2]=2;
	port[2][4][3]=2;
	port[2][4][4]=2;
	
	port[3][1][1]=1;
	port[3][1][2]=1;
	port[3][1][3]=1;
	port[3][1][4]=1;
	port[3][2][1]=1;
	port[3][2][2]=1;
	port[3][2][3]=2;
	port[3][2][4]=1;
	port[3][3][1]=1;
	port[3][3][2]=2;
	port[3][3][3]=2;
	port[3][3][4]=2;
	port[3][4][1]=1;
	port[3][4][2]=1;
	port[3][4][3]=2;
	port[3][4][4]=1;
	
	port[4][1][1]=1;
	port[4][1][2]=1;
	port[4][1][3]=1;
	port[4][1][4]=1;
	port[4][2][1]=1;
	port[4][2][2]=1;
	port[4][2][3]=1;
	port[4][2][4]=1;
	port[4][3][1]=1;
	port[4][3][2]=1;
	port[4][3][3]=1;
	port[4][3][4]=2;
	port[4][4][1]=1;
	port[4][4][2]=1;
	port[4][4][3]=2;
	port[4][4][4]=2;
	int test,ans[100];
	cin>>test;
	for(int i=0;i<test;i++)
	{
		
			int x,r,c;
			cin>>x;
			cin>>r;
			cin>>c;
			
			ans[i]=port[x][r][c];
	}
	for(int a=0;a<test;a++)
	{
		if(ans[a]==1)
		{
			cout<<"Case #"<<a+1<<": RICHARD"<<endl;
		}
		else
		{
			cout<<"Case #"<<a+1<<": GABRIEL"<<endl;
		}
	}
	return 0;
}