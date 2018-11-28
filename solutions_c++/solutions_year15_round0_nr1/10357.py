#include <iostream>
#include<string>
using namespace std;
string audience;
	
int maxCap(int Smax)
{
	
	int count=0;
	int sum=0;
	for(int i=0;i<=Smax;i++)
	{
		if(sum<i)
		{
			count+=i-sum;
			sum=i;
		}
		
		sum+=audience[i]-'0';
	}
	//cout<<sum<<endl;
	return count;
}
int main() {
	// your code goes here
	int ntc;
	int Smax;
	
	
	cin>>ntc;
	
	int t=ntc;
	while(ntc--)
	{
		cin>>Smax;
		
			cin>>audience;
	//		cout<<" audience "<<audience<<endl;
		
		cout<<"Case #"<<t-ntc<<": "<<maxCap(Smax)<<endl;
	}
	return 0;
}
