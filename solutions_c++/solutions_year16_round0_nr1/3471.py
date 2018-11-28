#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 100005
#define ll long long
#define llu unsigned long long 
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
int cou[20];
int main()
{
	int t,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		ll n,i,d,cnt=0,temp,ans;
		scanf("%lld",&n);
        for(i=0;i<10;i++)
          cou[i]=0;
        i=1;
        if(n==0)
        {
        	printf("Case #%d: INSOMNIA\n",k);
        }
		else
		{
			while(1)
			{
			temp=i*n;
			while(temp>0)
			{
			    d=temp%10;
			    if(cou[d]==0)
			    {
			      cnt++;
			      cou[d]++;
			    }  
				temp=temp/10;
			}
			if(cnt==10)
			  break;
			 i++; 
			} 
			ans=i*n;
	       printf("Case #%d: %lld\n",k,ans);
		}
	}
	return 0;
}	