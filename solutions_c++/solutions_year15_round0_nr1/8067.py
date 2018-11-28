#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t,maxs,test=1;
	string str;
	cin>>t;
	while(t--)	
	{
		cin>>maxs>>str;
		int how_many_standing=str[0]-'0';
		int bring_in=0;
		for(int i=1;i<=maxs;i++)
		{
			if((str[i]-'0')!=0)
			{
				if(i<=how_many_standing)
				{
					how_many_standing+=(str[i]-'0');
				}
				else
				{
					bring_in+=(i-how_many_standing);
					how_many_standing+=(i-how_many_standing)+(str[i]-'0');
				}
			}
		}
		cout<<"Case #"<<test++<<": "<<bring_in<<endl;
	}
	return 0;
}
