#include <bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
int main()
{
	f_in("input1.txt");
	f_out("output1.txt");
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		int X,R,C;
		cin>>X>>R>>C;
		cout<<"Case #"<<t<<": ";
		int R1=max(R,C);
		int C1=min(R,C);
		if(R1==1 && C1==1)
		{
			if(X==1)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else if((R1==2 && C1==1) || (R1==2 && C1==2))
		{
			if(X==1 || X==2)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;			
		}
		else if(R1==3 && C1==1)
		{
			if(X==1)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else if(R1==3 && C1==2)
		{
			if(X==4)
				cout<<"RICHARD"<<endl;
			else
				cout<<"GABRIEL"<<endl;
		}
		else if(R1==3 && C1==3)
		{
			if(X==1 || X==3)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else if(R1==4 && (C1==2 || C1==1))
		{
			if(X==1 || X==2)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else if(R1==4 && C1==3)
		{
			cout<<"GABRIEL"<<endl;
		}
		else if(R1==4 && C1==4)
		{
			if(X==1 || X==2 || X==4)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}