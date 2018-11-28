#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	int T, Smax;
	string crowd;
	
	cin>>T;
	
	for(int i = 1; i <= T; ++i)
	{
		cin>>Smax>>crowd;
		
		int sum = 0;
		int prev = crowd[0] - '0';
		crowd += '0';
		for(int j = 1; j < crowd.length(); ++j)
		{
			if((prev < j) && ((crowd[j] - '0') > 0)) 
			{
				sum += (j - prev);
				prev += (j - prev);
			}
			prev += crowd[j] - '0';
			//cout<<crowd[j]<<": "<<prev<<", "<<sum<<endl;
		}
		
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
}
