#include<iostream>
using namespace std;
int main()
{
	long long int t;
	cin >>t;
	for (int t1=1;t1<=t;t1++)
	{
		string s;
		cin>>s;
		int ans = 0;
		for (int i = s.length()-1; i >=0; i--)
		{
			if (s[i]=='-')
			{
				ans+=1;
				for (int j = 0; j <=i;j++)
				{
					if (s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
				// cout << s << endl;
			}
		}
		cout<<"Case #"<<t1<<": "<<ans<<endl;
	}
	return 0;
}
