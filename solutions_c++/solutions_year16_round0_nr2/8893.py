#include<iostream>
#include<string>

using namespace std;

int main()
{
	int t, o = 0;
	cin >> t;
	while (t--)
	{
		++o;
		cout <<"Case #"<<o<<": ";
		string s;
		cin >> s;
		int n = s.size();
		char c = '-';
		long long ans = 0;
		for ( int i = n-1; i >= 0; ) {
			if(s[i]==c)
			{
				ans+=1;
				while(i>= 0 && s[i]==c)
				i--;
				if(c=='-')
					c = '+';
				else
					c = '-';
			}
			else
				i--;
		}
		cout << ans <<endl;
	}
	
}
