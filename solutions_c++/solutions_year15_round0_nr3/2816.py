/*
author : lifecodemohit
*/
 
#include <bits/stdc++.h>
using namespace std;
 
#define ll long long int
#define MOD 1000000007
#define sn(n) scanf("%lld",&n)
#define pn(n) printf("%lld\n",n)
#define ss(str) scanf("%s",str)
#define ps(str) printf("%s\n",str)
#define rep(i,s,e) for(i=s;i<=e;i++)
#define reprev(i,s,e) for(i=s;i>=e;i--)
#define reps(b,e,g,str) for(b=str,e=&str[g-1];b<=e;b++) 
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define dis(arr,s,e) for(i=s;i<=e;i++) printf("%lld ",arr[i]); printf("\n"); 

int main()
{
	ll T;
	ll r=1;
	sn(T);
	while(T--)
	{
		ll g,x,flag,ans[100010],last,last1,i,j,k;
		char str[100010],*b,*e;
		ll res;
		sn(g);
		sn(x);
		ss(str);
		map<pair<ll,ll>,ll> k1;
		k1[make_pair(1,1)]=1;
		k1[make_pair(1,105)]=105;
		k1[make_pair(1,106)]=106;
		k1[make_pair(1,107)]=107;

		k1[make_pair(105,1)]=105;
		k1[make_pair(105,105)]=-1;
		k1[make_pair(105,106)]=107;
		k1[make_pair(105,107)]=-106;

		k1[make_pair(106,1)]=106;
		k1[make_pair(106,105)]=-107;
		k1[make_pair(106,106)]=-1;
		k1[make_pair(106,107)]=105;
		
		k1[make_pair(107,1)]=107;
		k1[make_pair(107,105)]=106;
		k1[make_pair(107,106)]=-105;
		k1[make_pair(107,107)]=-1;
		
		i=0;
		last=1;
		while(x--)
		{
			reps(b,e,g,str)
			{
				res=(int)*b;
				
					if(last<0)
					{
						last1=-1*last;
						ans[i]=-1*k1[make_pair(last1,res)];
						last=ans[i];
					}
					else
					{
						last1=last;
						ans[i]=k1[make_pair(last1,res)];
						last=ans[i];
					}
				i++;
			}
		}
		flag=0;
		if(ans[i-1]==-1)
		{
			reprev(j,i-2,1)
			{
				if(ans[j]==107)
				{
					reprev(k,j-1,0)
					{
						if(ans[k]==105)
						{
							flag=1;
							break;
						}
					}
					break;
				}
			}
			if(flag==1)
				printf("Case #%lld: YES\n",r);
			else
				printf("Case #%lld: NO\n",r);
		}
		else
			printf("Case #%lld: NO\n",r);
		r++;
	}
	return 0;
}