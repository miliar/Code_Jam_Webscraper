#include<iostream>
using namespace std;
unsigned long long power(int a,int b)
{
	unsigned long long exp=1;
	for(int i=1;i<=b;i++)
		exp=exp*a;
	return exp;
}
int main()
{
	int t;
	cin>>t;
	for(int it=1;it<=t;it++)
	{
		//cout<<"Case #"<<it<<": ";
		unsigned int K,C,S;
		cin>>K>>C>>S;
		cout<<"Case #"<<it<<": ";
		if(K!=S)
		{
			cout<<"ERROR!\n";
			break;
		}
		unsigned long long r=power(K,C-1);
		for(int jt=1;jt<=S;jt++)
		{
			//unsigned long long r=1+power(K,C-1);
			unsigned long long pr=1+(jt-1)*r;
			cout<<pr<<" ";
		}
		cout<<"\n";
	}
	return 0;
}
