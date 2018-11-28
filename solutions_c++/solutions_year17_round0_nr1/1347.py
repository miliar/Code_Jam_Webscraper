#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000
string str;
int ar[100000];
int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	int tcase,t,n,i,len,j,k,ans;
	bool f;
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
		f = 1;
       cin>>str>>k;
       len = str.size();
       for(i=0;i<len;i++)
       if(str[i]=='+')
       ar[i] = 1;
       else
       ar[i] = 0;
       ans = 0;
       for(i=0;i<len;i++)
       {
       	if(ar[i]==0 and i+k-1<=len-1)
       	{
       	  ans++;
			 for(j=i;j<=i+k-1;j++)
			 {
			   if(ar[j]==1)
			   ar[j] = 0;
			   else
			   ar[j] = 1;	
			 }	
		}
	   }
	   for(i=0;i<len;i++)
	   {
	   	 if(ar[i]==0)
	   	 f = 0;
	   }
	   printf("Case #%d: ",t);
	   if(f)
	   {
	   	printf("%d\n",ans);
	   }
	   else
	   {
	   	printf("IMPOSSIBLE\n");
	   }
	}
}

