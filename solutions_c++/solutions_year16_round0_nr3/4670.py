#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 100000001
#define ll long long
#define pb push_back
ll ex(ll a, ll b){
  ll result = 1;
  while (b){
    if (b%2==1){
      result= (result*a);
    }
    b /= 2;
    a= (a*a);
  }
  return result;
}
vector<ll> prime;
bool arr[N+1];
void calprime()
{ int i,j;
  memset(arr,true,sizeof(arr));
	for(i=2;i*i<=N;i++)
	{    if(arr[i]==true)
	   	for(j=2*i;j<=N;j+=i)
		{
			arr[j]=false;
		}
	}
	for(i=2;i<=N;i++)
	 if(arr[i])
	  prime.pb(i);
}
void next(char s[]){
	int i;
	int l=strlen(s);
	for(i=l-2;i>=1;i--)
	{
		if(s[i]=='0'){
		s[i]='1';
		break;
		}
		else if(s[i]=='1')
		s[i]='0';
	}
}
int main() {
    int t,k;
    calprime();
    scanf("%d",&t);
    for(k=1;k<=t;k++){
    	int M,J,cnt=0,i,j;
    	scanf("%d%d",&M,&J);
    	int size=M;
    	char s[size+1];
    	s[size]='\0';
    	for(i=0;i<=size-1;i++)
    	s[i]='0';
    	s[0]='1';s[size-1]='1';
        int f=0;
        vector<int> v;
    	printf("Case #%d:\n",k);
    	while(cnt!=J)
    	{   v.clear();
    	    f=0;
    		for(i=2;i<=10;i++)
    		{
    			ll n=0;
    			for(j=size-1;j>=0;j--)
    			{
    				n=n+((ll)(s[j]-48)*ex(i,((size-1)-j)));
    			}

    			if(n<=99999989)
    			{
    				if(binary_search(prime.begin(),prime.end(),n))
    				{f=1;
    			    v.clear();
    				break;
    				}
    			   else
    			   {
    			   	ll m;
    			   	for(m=2;m*m<=n;m++)
    			   	{if(n%m==0)
    			   	 { v.pb(m);
    			   	  break;
    			    	}
    			   	}
    			   }
    			}
    			else
    			{
    			   if(n%2==0)
    			   {
    			   	v.pb(2);
    			   }
    			   else
    			   {
    			   	ll l;
    			   	int f1=1;
    			   	for(l=3;l*l<=n;l+=2)
    			   	{
    			   		if(n%l==0)
    			   		{
    			   			v.pb(l);
    			   			f1=0;
    			   			break;
    			   		}
    			   	}
    			   	if(f1)
    			   	{v.clear();
    			   	f=1;
    			   	break;
    			   	}
    			   }
    			}
    		}
    			    if(!f){
    			    cnt++;
    			    printf("%s ",s);
    				for(int g=0;g<v.size();g++)
    				printf("%d ",v[g]);
    				printf("\n");
    			    }
    		next(s);
    	}

    }
	return 0;
}
