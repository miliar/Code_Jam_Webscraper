#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
using namespace std;
int main()
{

	int t;
	cin>>t;
	int a[t];
	for(int i=0;i<t;i++)
	{
		int m;
		cin>>m;
		string s;
		cin>>s;
		int y=0;
		int sum=0;
		for(int k=0;k<=m;k++)
		{
			sum=sum+s[k]-'0';
			
			if((sum-1)<k)
			{
				y++;
				sum++;
			}

			//cout<<sum<<" ";
		}
		a[i]=y;
	}
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<":"<<" "<<a[i]<<"\n";
	}


	return 0;
}
