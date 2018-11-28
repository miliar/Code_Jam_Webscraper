#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
	long long int cases,count=1;
	cin>>cases;
	while(cases--)
	{
		string s;
	cin>>s;
	long long int len=s.size(),lindex=len-1,rindex=len-1;
	char c[2*len-1];

	c[len-1]=s[0];
	for(long long int i=1;i<=len-1;i++)
	{
		if(s[i]-'A'>=c[lindex]-'A')
		{
			lindex--;
			c[lindex]=s[i];
		}
		else
		{
			rindex++;
			c[rindex]=s[i];
		}
	}

	cout << "Case #" << count++ << ": ";

	for(long long int i=lindex;i<=rindex;i++)
		cout << c[i];

	cout << "\n";
	}

	return 0;
}
