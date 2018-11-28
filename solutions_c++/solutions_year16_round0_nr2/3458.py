#include<bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	string s;
	cin>>test;
	int Case=1;
	while(test--)
	{
		cin>>s;
		int l=s.length();
		int flips=0;
		for(int i=l-1;i>=0;--i)
		{
			if(s[i]=='-' && flips%2==0)
			{
				flips++;
			}
			else if(s[i]=='+' && flips%2==1)
			{
				flips++;
			}
		}
		cout<<"Case #"<<Case<<": "<<flips<<endl;
		Case++;
	}
}
