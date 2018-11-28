#include<stdio.h>
#include<iostream>
using namespace std;
int T,X,R,C;
int main()
{
	cin>>T;
	int i,j,k;
	for(i=0;i<T;i++)
	{
		
		cin>>X;
		cin>>R;
		cin>>C;
		cout<<"Case #"<<i+1<<": ";
		int max,min;
		(R>=C)?(max=R):(max=C);
		(max==R)?(min=C):(min=R);
		if((max*min)%X==0)
		{
			if(min>X/2 || (X==2 && min==1) || (X==1))
			{
				if(max>=X)
					cout<<"GABRIEL\n";
				else
					cout<<"RICHARD\n";
			}
			else
					cout<<"RICHARD\n";
		}
			else
			{
				cout<<"RICHARD\n";
			}
	}
}
