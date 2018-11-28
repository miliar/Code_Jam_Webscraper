#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
	int n;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>n;
	int i;
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		string s="";
		char temp[2000];
		scanf("%s",temp);
		int j=0;
		for(j=0;j<strlen(temp);j++)
		{
			string s1,s2;
			s1+=temp[j];
			s1+=s;
			s2+=s;
			s2+=temp[j];
			if(s1>s2)s=s1;
			else s=s2;
		}
		cout<<s<<endl;
	}
	return 0;
	
}
