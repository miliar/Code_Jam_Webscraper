#include <iostream>
using namespace std;

int main()
{
	int T;

	cin>>T;

	for(int counter=0;counter<T;counter++)
	{
		int smax;
		char str[1005];

		cin>>smax>>str;	
		//cout<<smax<<str<<endl;
		int ans=0,sum=0,diff;
		for(int sc=0;sc<smax+1;sc++)
		{
			if(str[sc] != '0')
			{
				if(sum < sc)
				{
					diff= sc - sum;
					ans+=diff;
					sum +=diff;
				}
				sum += str[sc] - '0';
			}
		}
		cout<<"Case #"<<counter+1<<": "<<ans<<endl;
	}

	return 0;
}
