#include<cstdio>
#include<iostream>
using namespace std;
int make()
{
	char b[5][5];
	int x;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>b[i][j];
	for(int i=0;i<4;i++)
	{
		x=0;
		for(int j=0;j<4;j++)
			if(b[i][j]=='X' || b[i][j]=='T') x++;
		if(x==4) return 1;
	}
	for(int j=0;j<4;j++)
	{
		x=0;
		for(int i=0;i<4;i++)
			if(b[i][j]=='X' || b[i][j]=='T') x++;
		if(x==4) return 1;
	}
	x=0;
	for(int i=0;i<4;i++)
		if(b[i][i]=='X' || b[i][i]=='T') x++;
	if(x==4) return 1;
	x=0;
	for(int i=0;i<4;i++)
		if(b[3-i][i]=='X' || b[3-i][i]=='T') x++;
	if(x==4) return 1;
	for(int i=0;i<4;i++)
	{
		x=0;
		for(int j=0;j<4;j++)
			if(b[i][j]=='O' || b[i][j]=='T') x++;
		if(x==4) return 2;
	}
	for(int j=0;j<4;j++)
	{
		x=0;
		for(int i=0;i<4;i++)
			if(b[i][j]=='O' || b[i][j]=='T') x++;
		if(x==4) return 2;
	}
	x=0;
	for(int i=0;i<4;i++)
		if(b[i][i]=='O' || b[i][i]=='T') x++;
	if(x==4) return 2;
	x=0;
	for(int i=0;i<4;i++)
		if(b[3-i][i]=='O' || b[3-i][i]=='T') x++;
	if(x==4) return 2;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(b[i][j]=='.') return 4;
	return 3;
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int f=make();
		cout<<"Case #"<<i<<": ";
		if(f==1) cout<<"X won";
		if(f==2) cout<<"O won";
		if(f==3) cout<<"Draw";
		if(f==4) cout<<"Game has not completed";
		cout<<endl;
	}
	//system("pause");
	return 0;
}


	