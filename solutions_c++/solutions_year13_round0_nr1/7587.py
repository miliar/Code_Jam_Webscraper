/********************************************
Author: Yinthewind
Sat Apr 13 17:53:43 CST 2013
********************************************/
#include<cstdio>
#include<vector>
#include<iostream>
#include<cstring>
using namespace std;

char s[22];
bool check(char x)
{
	bool flag;
	for(int i=0;i<4;i++)
	{
		flag=true;
		for(int j=0;j<4;j++) if(s[4*i+j]!=x&&s[4*i+j]!='T') flag=false;
		if(flag) return true;
		flag=true;
		for(int j=0;j<4;j++) if(s[i+4*j]!=x&&s[i+4*j]!='T') flag=false;
		if(flag) return true;
	}
	flag=true;
	for(int i=1;i<=4;i++) if(s[3*i]!=x&&s[3*i]!='T') flag=false;
	if(flag) return true;
	flag=true;
	for(int i=0;i<4;i++) if(s[5*i]!=x&&s[5*i]!='T') flag=false;
	if(flag) return true;

	return false;
}
int main()
{
	int T;
	cin>>T;
	int t=0;
	while(T--)
	{
		bool flag=false;
		char ch;
		for(int i=0;i<16;i++) 
		{
			while((ch=getchar())!='X'&&ch!='.'&&ch!='T'&&ch!='O');
			s[i]=ch;
			if(ch=='.') flag=true;
		}
		cout<<"Case #"<<++t<<": ";
		if(check('X')) cout<<"X won"<<endl;
		else if(check('O')) cout<<"O won"<<endl;
		else if(flag) cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	}
	return 0;
}
