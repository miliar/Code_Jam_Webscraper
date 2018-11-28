#include<iostream>
#include<string>
#include<cstring>
using namespace std;

//int arr[1010];

unsigned long long Calc(const unsigned long long& Smax,const string& shyness)
{
	unsigned long long sum=0,curr=0;
	
	for(unsigned long long i=0;i<=Smax;i++)
	{
		if(curr<i)
		{
			sum+=i-curr;
			curr=i;
		}
		curr+=shyness[i]-'0';
	}
	return sum;	
}

int main()
{
	int T,Smax;
	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
	cin>>T;
	string shyness;
	for(int i=1;i<=T;i++)
	{
		cin>>Smax>>shyness;
		cout<<"Case #"<<i<<": "<<Calc(Smax,shyness)<<endl;
	}
	return 0;
}