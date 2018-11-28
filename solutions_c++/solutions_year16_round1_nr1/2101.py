#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
int main()
{
	string curr, rem;
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		rem="";
		cout<<"Case #";
		cout<<(i+1)<<": ";
		cin>>curr;
		rem=curr[0];
		for(int k=1;k<curr.length();k++)
		{
			if(rem[0]>curr[k])
			{
				//cout << rem << "2" << endl;
				rem=rem+curr[k];
				//cout << rem << "1" << endl;
			}
			else
			{
				//cout << rem << "3" << endl;
				rem=curr[k]+rem;
				//cout << rem << "4" << endl;
			}
		}
		cout<<rem<<endl;
	}
	return 0;
}
