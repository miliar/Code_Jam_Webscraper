#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;x++)
	{
		int smax;
		string val;
		scanf("%d",&smax);
		cin>>val;

		int pos_last_non_zero=0,ans=0;
		for(int i=0;i<val.length();i++)
		{
			if(val[i] != '0')
				pos_last_non_zero = i;
		}

		int no_of_standing=(int)val[0]-48;
		for(int i=1;i<=pos_last_non_zero;i++)
		{
			if(no_of_standing < i && val[i] != '0')
			{
				ans += i - no_of_standing; 
				no_of_standing += ans;
				//cout<<ans<<" ";
			}
			no_of_standing += (int)val[i]-48;
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}

	return 0;
}