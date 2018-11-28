#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;

	int X,R,C;
	string result;
	int total ;
	for(int t=1;t<=T;++t)
	{
		cin>>X>>R>>C;
		result="RICHARD";
		total=R*C;
		if(X==1)
			result = "GABRIEL";
		else if (X==2)
		{
			if(total%2==0)
				result="GABRIEL";
		}
		else if (X==3)
		{
			if(total%3==0 && total>5)
				result="GABRIEL";
		}
		else if (X==4)
		{
			if(total==12 || total==16)
				result="GABRIEL";
		}
		cout<<"Case #"<<t<<": "<<result<<endl;
	}
}