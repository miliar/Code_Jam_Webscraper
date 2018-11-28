#include <bits/stdc++.h>
using namespace std;
int a[1000];
int main()
{
	int t,curr,i=0,max=0,min=0;
	string s;
	cin>>t;
	while(i++<t)
	{
		cin>>s;
		cout<<"Case #"<<i<<": ";
		deque<char> a;
		max = int(s[0]);
		min = max;
		a.push_front(s[0]);
		for(int j=1;j<s.length();j++)
		{

			if(int(s[j])>= max)
			{
				a.push_front(s[j]);
				max = int(s[j]);
			}
			else if(int(s[j])< min)
			{
				a.push_back(s[j]);
				min = int(s[j]);
			}
			else
			{
				a.push_back(s[j]);
			}
		}
		for (deque<char>::iterator it = a.begin(); it != a.end(); ++it)
   			cout<< *it;
   		cout<<endl;
	}
	/*i=0;
	while(i++<t)
	{
		cout<<"Case #"<<i<<": ";
	}*/
}