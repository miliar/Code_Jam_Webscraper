#include <iostream>
using namespace std;

int main()
{
	int i,t;
	int s,req,curr;
	string str;

	cin>>t;
	for(int cases=1; cases<=t; cases++)
	{
		cin>>s;
		cin>>str;
		req=0;
		curr=0;
		for(i=0; i<str.length(); i++)
		{
			if(curr<i)
			{
				req+=i - curr;
				curr=i;
			}
			curr+=str[i]-'0';
		}
		cout<<"Case #"<<cases<<": "<<req<<endl;
	}
	return 0;
}
