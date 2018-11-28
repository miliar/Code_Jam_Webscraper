#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		int s;
		string sm;
		cin>>s>>sm;
		int count=sm.at(0)-'0';
		//cout<<count<<endl;
		int total=0;
		for(int i=1;i<=s;i++)
		{
			if((i>count)&&(sm.at(i)-'0'>0))
			{
				total+=i-count;
				//cout<<i<<" "<<total<<endl;
				count+=total;
			}
			count+=sm.at(i)-'0';
		}
		cout<<"Case #"<<j+1<<": "<<total<<endl;
	}
	return 0;
}