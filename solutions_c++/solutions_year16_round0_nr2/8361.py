#include <iostream>
#include <string>

using namespace std;

void flip(string& s,int n)
{
	for(int i = 0; i < n; i++)
	{
		if(s[i] == '+') s[i] = '-';
		else if(s[i] == '-') s[i] = '+';
	}
}


int main()
{
	int t,nf;
	string s;
	
	cin>>t;
	for(int i = 0; i < t; i++)
	{
		nf = 0;
		cin>>s;
		
		for(unsigned int j = 0; j < s.size(); j++)
		{
			//if(s[j] == '+');
			if(s[j] == '-')
			{
				while(s[j] == '-' && j < s.size())
					j++;
				
				//cout<<j<<endl;
				flip(s,j);
				//cout<<s<<endl;
				nf++;
				j = -1;
			}
		}
		
		cout<<"Case #"<<i+1<<": "<<nf<<endl;
	}
	
	return 0;
}