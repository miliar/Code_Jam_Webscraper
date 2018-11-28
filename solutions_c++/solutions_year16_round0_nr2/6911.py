#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int changed = 0;
		int n = s.length();
		// cout<<n;
		n--;
		while(n >= 0)
		{
			 // cout<<s[n]<<"  ";
			if(s[n] == '+')
			{
				// cout<<"current sign + "<<endl;
				if(changed % 2 == 1)
				{
					changed += 1;
					// cout<<"in + ";
				}
			}
			else
			{
				// cout<<"current sign - "<<endl;
				if(changed % 2 == 0)
				{
					changed += 1;
					// cout<<"in - ";
				}
			}
			n--;
		}
		cout<<"Case #"<<i+1<<": "<<changed<<endl;
	}
}