#include <bits/stdc++.h>
using namespace std;
int prime[100000];

void sieve()
{
	prime[0]=prime[1]=0;
	long long int i,j;
	for(i=2;i<100000;i++)
	prime[i]=1;
	for(i=2;i<=sqrt(100000);i++)
	{
		if(prime[i])
		{
			for(j=2*i;j<100000;j=j+i)
			prime[j]=0;
		}
	}
}
int main() {
	// your code goes here
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	sieve();
	freopen("input3.txt","r",stdin);
	freopen("ans3.txt","w",stdout);
	long long int t,z;
	long long int powe[21],power[15][20];
	for(z=0;z<11;z++)
	{
		power[z][0]=1;
	}
	for(z=0;z<11;z++)
	{
		for(t=1;t<18;t++)
		{
			power[z][t]=power[z][t-1]*z;
		}
	}
	powe[0]=1;
	for(z=1;z<=18;z++)
	{
		powe[z]=powe[z-1]*2;
	}
	cin>>t;
	for(z=1;z<=t;z++)
	{
		long long int n,j,i,k,l,m,x=0,dec,rem,ans,c,d,flag=0;
		cin>>n>>j;
		long long int a[20]={0},b[20]={0};
		for(i=32768;i<=65535 && x<j;i++)
		{
			for(c=0;c<20;c++)
				{
					a[c]=0;
					b[c]=0;
				}
				dec=i;
				k=n-1;
				do
	    		{
	        		rem=dec%2;
	        		a[k--]=rem;
	        		dec=dec/2;
	    		}while(dec>0);
	    		if(a[0]==1 && a[n-1]==1)
	    		{
		    		for(c=2;c<11;c++)
		    		{
		    			ans=0;
		    			for(k=n-1;k>=0;k--)
		    			{
		    				ans=ans+a[k]*power[c][n-1-k];
		    			}
		    			b[c]=ans;
		    		}
		    		for(c=2;c<11;c++)
		    		{
		    			if(b[c]<100000)
		    			{
		    				if(prime[b[c]])
		    				break;
		    			}
		    			else
		    			{
		    				
		    				long long int  cbr = pow(b[c],(1.0/3.0));
		    				cbr=cbr+10;
								for (d = 2; d <=cbr; d++)
								{
									if (b[c] % d == 0)
									{
										break;
									}
								}
								if(d>cbr)
								{
									long temp = sqrt(b[c]);
									if(temp*temp!=b[c])
										break;
								}
		    			}
		    		}
		    		if(c==11)
		    		{
		    			if(flag==0)
		    			{
		    				cout<<"Case #"<<z<<":"<<endl;
		    				flag=1;
		    			}
		    			for(c=0;c<n;c++)
		    			cout<<a[c];
		    			cout<<" ";
		    			for(d=2;d<11;d++)
		    			{
		    				for(c=2;c<=sqrt(b[d]);c++)
		    				{
		    					if(prime[c]==1)
		    					{
		    						if(b[d]%c==0)
		    						{
		    							cout<<c<<" ";
		    							break;
		    						}
		    					}
		    				}
		    			}	
	    			cout<<endl;
	    			x++;
		   		}
	    	}
		}
	}
	return 0;
}