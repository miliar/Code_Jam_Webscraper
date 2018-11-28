#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int f=1;f<=t;f++)
	{
		int smax;
		string s;
		cin>>smax>>s;
		int extra =0;
		int till_now = 0;
		till_now += s[0] - '0';
		for(int i=1;i<s.size();i++)
		{
			int diff = i-till_now;
			if(diff > 0)
			{
				extra += diff;
				till_now += diff;
			}
			till_now += s[i] - '0' ;
		}
		cout<<"Case #"<<f<<": "<<extra<<endl;
	}
}