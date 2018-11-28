#include<iostream>
using namespace std;
int main()
{
	int test,people,pneed;
	int s_max;
	string input;
		cin>>test;
	for(int t=1; t<=test; t++)
	{
		people=0;
		pneed=0;
		cin>>s_max;
		cin>>input;
		people=people+(int)input[0]-48;
		for(int i=1; i<=s_max; i++)
		{
			if(i<=people)
				people=people+(int)input[i]-48;
			else
			{
				if(((int)input[i]-48)!=0)
				{
					pneed=pneed+(i-people);
					people=i+(int)input[i]-48;
				}	
			}
		}
		if(t==1)
			cout<<"Case #"<<t<<": "<<pneed;
		else
			cout<<"\nCase #"<<t<<": "<<pneed;
	}
	return 0;
}
