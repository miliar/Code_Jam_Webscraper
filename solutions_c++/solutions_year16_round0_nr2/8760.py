#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int i=0; i<t; i++)
	{		
		char s[110];
		//char ss[110];		
		cin>>s;
		cout<<"Case #"<<i+1<<": ";

		int len = strlen(s);
		
		int count = 0;
		if(len==1)
		{
			if(s[0]=='-')
				cout<<"1"<<endl;
			else
				cout<<"0"<<endl;
		}		
		else
		{
			for(int j=1; j<len; j++)
			{
				if(s[j-1]!=s[j])
					count++;
			}	
			if(s[len-1]=='-')
				count++;
			cout<<count<<endl;
		}	
	}
	return 0;
}
