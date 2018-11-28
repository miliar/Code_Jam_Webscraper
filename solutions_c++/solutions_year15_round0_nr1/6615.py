#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int test,n,i,j,len;
	cin >> test;
	char str1[2000];
	for(i=1;i<=test;i++)
	{
		cin >> n;
		cin >> str1;
		len=strlen(str1);
		int ans=0;
		int sum=0;
		sum+=str1[0]-'0';
		for(j=1;j<len;j++)
		{
               if(sum<j && str1[j]!='0')
               {
               	  ans+=j-sum;
               	  sum=j;
               	  sum+=str1[j]-'0';
               } 
               else
               	sum+=str1[j]-'0';
		}

		cout << "Case #" << i << ": "  << ans << endl;
	}
	return 0;
}