#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t,n,i,j,len;
	cin >> t;
	char str[2000];
	for(i=1;i<=t;i++)
	{
		cin >> n;
		cin >> str;
		len=strlen(str);
		int ans=0;
		int sum=0;
		sum+=str[0]-'0';
		for(j=1;j<len;j++)
		{
               if(sum<j && str[j]!='0')
               {
               	  ans+=j-sum;
               	  sum=j;
               	  sum+=str[j]-'0';
               } 
               else
               	sum+=str[j]-'0';
		}

		cout << "Case #" << i << ": "  << ans << endl;
	}
	return 0;
}