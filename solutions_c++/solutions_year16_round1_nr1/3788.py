#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	char s[1005],b[2010];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
	   cin>>s;
	   int l=strlen(s);
	   int m=1002,v=1002;
	   b[m]=s[0];
	   for(int j=1;j<l;j++)
	   {
	   	 if(s[j]>=b[m])
	   	 b[--m]=s[j];
	   	 else b[++v]=s[j];
	   }
	   cout<<"Case #"<<i<<": ";
	   for(int j=m;j<=v;j++)
	   printf("%c",b[j]);
	   cout<<endl;
	}
	return 0;
}
