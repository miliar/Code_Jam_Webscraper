#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int ta;
	cin>>ta;
	for (int tz=1;tz<=ta;tz++)
	{
		string s;
		cin>>s;
		s+='+';
		int len=s.size();
		int count=0;
		for (int i=0;i<len-1;i++)
			if (s[i]!=s[i+1])
				count++;
		printf("Case #%d: %d\n",tz,count);
	}
}
