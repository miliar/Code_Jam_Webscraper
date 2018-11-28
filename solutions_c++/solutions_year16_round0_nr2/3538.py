#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 1001
#define ll long long
#define llu unsigned long long 
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
char str[N],temp[N];
int main()
{
	int t,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		int i,j,cnt1=0,cnt2=0,cnt,flag=0,fin_l,fin_r,e,maxi=0,ans=0;
		scanf("%s",str);
		int l=strlen(str);
		for(i=0;i<l;i++)
		{
			if(str[i]=='+')
			  cnt1++;
			else
			  cnt2++;
		}
		if(cnt1==l)
		  ans=0;
		else if(cnt2==l)
		  ans=1;
		else
		{
			int flag=1;
			cnt=1;
			e=l-1;
		    while(1)
		    {
		    	cnt1=0,cnt2=0;
		    	for(i=e;i>=0;i--)
			    {
				  if(str[i]=='-')
				    break;
			    }
			    e=i;
			    if(e<0)
			      break;
			      cnt=0;
		       for(i=0;i<=e;i++)
		       {
		       	if(str[i]=='-')
		       	  break;
		       	 cnt++; 
		       }
		       for(j=i;j<=e;j++)
		       {
		       	if(str[j]=='+')
		       	  break;
		       	cnt++;  
		       }
		       	   fin_r=i-1;
		       j=0;
		       for(i=fin_r;i>=0;i--)
		       {
		       	   if(str[i]=='+')
		       	     temp[j]='-';
		       	   else
		       	     temp[j]='+';
		       	   j++;
		       	   cnt1++;
		       }
		       if(cnt1>0)
		         ans++;
		       for(i=fin_r+1;i<=e;i++)
		         temp[i]=str[i];
		       j=0;  
		       for(i=e;i>=0;i--)
		       {
		           if(temp[i]=='+')
		            str[j]='-';
		           else
		             str[j]='+';
		           j++;  
		           cnt2++;
		       }      
		       if(cnt2>0)
		         ans++;
		    }
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}	