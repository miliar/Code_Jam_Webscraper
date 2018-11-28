#include<iostream>
using namespace std;
bool func(int x,int r,int c)
{
	//returning 1 means 2nd player can win
	if(x==1)
	{
		if(r==1 && c==1)return 1;
		if(r==1 && c==2)return 1;
		if(r==1 && c==3)return 1;
		if(r==1 && c==4)return 1;
		if(r==2 && c==1)return 1;
		if(r==2 && c==2)return 1;
		if(r==2 && c==3)return 1;
		if(r==2 && c==4)return 1;
		if(r==3 && c==1)return 1;
		if(r==3 && c==2)return 1;
		if(r==3 && c==3)return 1;
		if(r==3 && c==4)return 1;
		if(r==4 && c==1)return 1;
		if(r==4 && c==2)return 1;
		if(r==4 && c==3)return 1;
		if(r==4 && c==4)return 1;
	}
	if(x==2)
	{
		if(r==1 && c==1)return 0;
		if(r==1 && c==2)return 1;
		if(r==1 && c==3)return 0;
		if(r==1 && c==4)return 1;
		if(r==2 && c==1)return 1;
		if(r==2 && c==2)return 1;
		if(r==2 && c==3)return 1;
		if(r==2 && c==4)return 1;
		if(r==3 && c==1)return 0;
		if(r==3 && c==2)return 1;
		if(r==3 && c==3)return 0;
		if(r==3 && c==4)return 1;
		if(r==4 && c==1)return 1;
		if(r==4 && c==2)return 1;
		if(r==4 && c==3)return 1;
		if(r==4 && c==4)return 1;
	}
	if(x==3)
	{
		if(r==1 && c==1)return 0; 
		if(r==1 && c==2)return 0;
		if(r==1 && c==3)return 0;
		if(r==1 && c==4)return 0;
		if(r==2 && c==1)return 0;
		if(r==2 && c==2)return 0;
		if(r==2 && c==3)return 1;
		if(r==2 && c==4)return 0;
		if(r==3 && c==1)return 0;
		if(r==3 && c==2)return 1;
		if(r==3 && c==3)return 1;
		if(r==3 && c==4)return 1;
		if(r==4 && c==1)return 0;
		if(r==4 && c==2)return 0;
		if(r==4 && c==3)return 1;
		if(r==4 && c==4)return 0;
	}
	if(x==4)
	{
		if(r==1 && c==1)return 0; 
		if(r==1 && c==2)return 0;
		if(r==1 && c==3)return 0;
		if(r==1 && c==4)return 0;
		if(r==2 && c==1)return 0;
		if(r==2 && c==2)return 0;
		if(r==2 && c==3)return 0;
		if(r==2 && c==4)return 0;
		if(r==3 && c==1)return 0;
		if(r==3 && c==2)return 0;
		if(r==3 && c==3)return 0;
		if(r==3 && c==4)return 1;
		if(r==4 && c==1)return 0;
		if(r==4 && c==2)return 0;
		if(r==4 && c==3)return 1;
		if(r==4 && c==4)return 1;
	}
	return 0;
}
int main()
{
	int t,x,r,c;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>x>>r>>c;
		cout<<"Case #"<<tc<<": ";
		if(func(x,r,c)) cout<<"GABRIEL\n";
		else cout<<"RICHARD\n";
	}
}
