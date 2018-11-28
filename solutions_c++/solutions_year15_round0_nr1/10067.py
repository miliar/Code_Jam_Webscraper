#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
	long int t,S,cnt,j,i,temp,need;
	string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>S;
		cin>>s;
		cnt=s[0]-'0';need=0;
		for(j=1;j<S+1;j++)
		{
			if(cnt>=j&&s[j]!='0')
			{
				cnt+=s[j]-'0';
			}
			else if(cnt<j&&s[j]!='0')
			{
				temp=j-cnt;need+=temp;
				cnt+=temp;
				cnt+=s[j]-'0';
			}
		}
		printf("Case #%ld: %ld\n",i,need);
	}
	return 0;
}