#include<iostream>
using namespace std;
int main()
{
	int test_cases;
	cin>>test_cases;
	for(int r = 1; r<= test_cases; r++)
	{
		cout<<"Case #"<<r<<": ";
		int max;
		cin>>max;
		int ans = 0;
		int extra = 0;
		string s;
		cin>>s;
		for( int i=0; i<s.size(); i++) 
		{
			extra--;
			extra+=(s[i]-'0');
			if(extra <  0 )
			{
				ans++;
				extra=0;
			}
		}
		cout<<ans<<endl;
	}
}
