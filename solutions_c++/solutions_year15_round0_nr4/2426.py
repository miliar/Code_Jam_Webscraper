#include <iostream>
using namespace std;

int main() {
	int T,X,R,C,flag=0;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		flag=0;
		cin>>X>>R>>C;
		if(X==1)
		{
			flag=1;
		}
		else if(X==2)
		{
			if((R*C)%2==0)
			{
				flag=1;
			}
		}
		else if(X==3)
		{
			if(((R*C)%3==0)&&(R*C>3))
			flag=1;
		}
		else 
		{
			if((((R*C)%4)==0)&&(R*C>8))
			flag=1;
		}
		if(flag==1)
		{
			cout<<"Case #"<<i<<": GABRIEL"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": RICHARD"<<endl;
		}
	}
	// your code goes here
	return 0;
}