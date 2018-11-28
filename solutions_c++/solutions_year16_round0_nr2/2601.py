#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t,c;
	cin >> t;
	for (c=1;c<=t;c++)
	{
		string s;
		cin >> s;
		int i=s.size() - 1;

		int flag=0;
		int ans=0;
		while(i>=0)
		{
			if (flag==0 && s[i]=='-')
			{
				ans++;
				while(i>=0 && s[i]=='-')
					i--;
				flag=1;
			}

			else if (flag==0 && s[i]=='+')
			{
				while(i>=0 && s[i]=='+')
					i--;
			}

			else if (flag==1 && s[i]=='+')
			{
				ans++;
				while(i>=0 && s[i]=='+')
					i--;
				flag=0;
			}

			else if (flag==1 && s[i]=='-')
			{
				while(i>=0 && s[i]=='-')

					i--;
			}
		}

		cout<<"Case #"<<c<<": "<<ans<<endl;

	}


	return 0;
}