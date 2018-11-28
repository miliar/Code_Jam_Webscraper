#include <iostream>
using namespace std;

int main (void)
{
	int test;
	cin>>test;

	for(int j=1;j<=test;j++)
	{

		string s;
		cin>>s;

		for(int i=0;i<s.length();i++)
		{
			if (s[i]=='+')
				s[i]=1;
			else
				s[i]=0;
		}

		int count=0;
		//cout<<s.length()-1;
		for (int i=s.length()-1;i>=0;i--)
		{
			if((s[i]+count)%2 == 0)
			{
				// increment count
				s[i]='1';
				count++;

			}
		}

		//if (j>1)
			//break;
		cout<<"Case #"<<j<<": "<<count<<endl;




	}

	
	

	return 0;
}