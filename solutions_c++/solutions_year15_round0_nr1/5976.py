#include<iostream>
#include <string>

using namespace std;

int main()
{

	int t;
	cin>>t;
	int smax;
	string s;
	int invite = 0;
	int audiencecount = 0;
	for(int i = 0 ; i < t ; i ++)
	{
		cin>>smax>>s;
		
		if(smax==0)
		{
			cout<<"Case #"<<i+1<<": "<<invite<<endl;
		}		
		else
		{
			int temp = 0;
			for(int j = 0 ; j < s.size() ; j++)
			{
				temp = audiencecount + invite;

				if(j > temp)
				{
					invite += (j - temp);
				}
				audiencecount += s[j]-'0';
				
			}
			cout<<"Case #"<<i+1<<": "<<invite<<endl;
		}
		
		invite = 0;
		audiencecount = 0;
				
	}
	

}




