#include <bits/stdc++.h>

using namespace std;
#define ll long long

bool Miller(ll p)
{
    for(ll i=2;i*i<=p;i++)
	{
		 if(p%i==0)
		  return false;
	}   
    return true;
}
ll conv(ll v[],ll n ,ll base)
{
	  ll ret=0;
	  for(int i=0;i<n;i++)
	  {
	  	 ret += ( v[i] * (ll)pow(base,i) );
	  }
	  return ret;
}
int main()
{
	long long n,t,J;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
	
	scanf("%lld",&t);
	int tst=0;
	
	while(t--)
	{
		tst++;	
		scanf("%lld %lld",&n,&J);
		
		printf("Case #%d:\n",tst);
		ll v[n+2];
		v[0]=1;v[n-1]=1;
		for(long long i=0; i<(1<<(n-2)) ; i++)
		{
			for(int k=0;k<n-2;k++)
			{
				 if( i  & (1<<k) )
				 {
				 	v[k+1]=1;
				 }
				 else v[k+1]=0;
		    }
		    int cou=0;
			for(ll  j=2;j<=10;j++)
			{
			  ll num = conv(v,n,j);
			  
			  if(!Miller(num))
			  {
			  	//cout << num << " " << "p\n"  ;
			  	cou++;
			  }
			  //else cout << num << " " << "np\n"  ;
			  //cout << num << endl;	
			}
			if(cou==9)
			{
				for(int j=n-1;j>=0;j--)
				 printf("%lld",v[j]);
                printf(" ");
    			J--;
			    //cou++;
			   
			   for(ll  j=2;j<=10;j++)
			   {
			      ll num = conv(v,n,j);
			      //cout << num << endl; 
			      for(ll aa=2;aa*aa<=num;aa++)
				  {
				    if(num%aa==0)
					{
					  printf("%lld ",aa);break;
				    }
				  }	
			   }
			   printf("\n");	
			}
			if(J==0)
			 break;
		}
	}
	return 0;
}

