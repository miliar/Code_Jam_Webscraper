#include<iostream>

using namespace std;

int main()
{
	int t;
	int x=1;
	cin>>t;
	int n;
	string s;
	int level=0;
	int res;
	while(x<=t)
	{
		res=0;
		cin>>n;
		cin>>s;
		level = (s[0] - '0');
		for(int i=1;i<s.length();)
		{
			if(level >= i)
			{
				level = level + (s[i]-'0');
				i++;
			}
			else
			{
				level = level + 1;
				res=res+1;
			}
		
		}
		cout<<"Case #"<<x<<": "<<res<<endl;
		x++;
	}
	return 0;
}
