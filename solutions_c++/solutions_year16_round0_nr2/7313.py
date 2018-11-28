#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,i,j,k,count1;
	string str;
	scanf ("%d",&t);
	int e=1;
	while (t--)
	{
		cin>>str;
		n=str.length();
		char pre=str[0];
		count1=0;
		for (i=1;i<n;i++)
		  if (str[i]!=pre)
		  {
		  	count1++;
		  	pre=str[i];
		  }
		  cout<<"Case #"<<e++<<": ";
		  if (pre!='+')
		  count1++;
		  cout<<count1<<endl;
	}
	return 0;
}
		  