/*input
5
-
-+
+-
+++
--+-
*/

#include <iostream>
#include <set>
using namespace std;

int main(int argc, char const *argv[])
{
	int test;
	cin>>test;
	int casen=0;
	while(test--)
	{
		casen++;
		string s;
		cin>>s;
		int ans = 0;
		int count = 0;
		int pos=0;
		bool flag = true;
		while(flag)
		{
			flag = false;
			pos = -1;
			for (int i = 0; i < s.size(); ++i)
			{
				if(s[i]=='-')
				{
					pos = i;
					// flag = true;
				}
			}
			
			if(pos!=-1)
			{
				ans++;
				s[pos]='+';
				for (int i = pos-1; i >= 0; --i)
				{
					if(s[i]=='-')
						s[i]='+';
					else
						s[i]='-';
						
				}
			}
			for (int i = 0; i < s.size(); ++i)
			{
				if(s[i]=='-')
				{
					flag = true;
					break;
				}
			}
			
			
		}
	cout<<"Case #"<<casen<<": "<<ans<<endl;

	}
	return 0;
}