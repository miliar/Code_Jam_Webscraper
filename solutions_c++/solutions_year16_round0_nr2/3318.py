#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
	long long int cases,caseno=1;
	cin>>cases;
	while(cases--)
	{
		long long int len,count=0;
	string s;
	cin>>s;
	len=s.size();
	for(long long int i=0;i<len-1;i++)
	{
		if(s[i]!=s[i+1])
			count++;
	}
	if(s[len-1]=='-')
		count++;
	cout << "Case #" << caseno++ << ": " << count << "\n";
	}
	return 0;
}
