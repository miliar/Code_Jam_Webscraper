#include <iostream>
#include<stdio.h>
#include<math.h>
#define ll long long int
using namespace std;
//char s[17];
bool prime[10000000]={false};
ll fact[10000000];
void sieve()
{
    for(ll i=2; i*i<=10000000; i++)
    {
        if(prime[i]==false)
        {
            for(ll j=i*2; j<=10000000; j+=i)
            {
                if(prime[j]!=true) fact[j]=i;
                prime[j]=true;

            }

        }
    }
}
ll isprime(ll n)
{
    for( ll i=2; i*i<=n; i++)
    {
        if(n%i==0)
            return i;
    }
    return -1;
}
ll s[35];
int fact2[11];
void dec2bin(ll num, ll n)
{
	ll i;
	for(i=n-2; i>=1; i--)
	{
		if(num==0)
		{
			s[i]=0;
		}
		else
		{
			s[i]=num%2;
			num/=2;
		}
	}
}

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output2.txt","w",stdout);
    sieve();
    ll t,v,n,j,count,f,h=1,num;
    scanf("%lld",&t);
    //t=1;
    while(t--)
    {
        count=0;
        v=0;
        scanf("%lld%lld",&n,&j);
        printf("Case #%lld:\n",h);
        h++;
        s[0]=1;
        s[n-1]=1;
        f=pow(2,n);
//        cout<<f;
        for(ll i=0; i<f; i++)
        {
            //cout<<"lol";
            //if(i%100==0)cout<<"lol"<<" ";
            dec2bin(i,n);
            for(ll j=2; j<=10; j++)
            {
                //cout<<s[n-1];
                num=0;
                for(ll k=0; k<n; k++)
                {
                    //if(k==0&&s[k]==1) cout<<"lol";
                    if(s[k]==1)
                    {
                      //  if(k==n-1) num++;
                         ll ss=pow(j,n-1-k);
                         num=num+ss;
                        //if(j==10&&k==n-1) cout<<num<<" ";
                        //if(num>10000000) break;

                    }
                }
                //num=num+1;
                //if(j==10&&num%2==0) cout<<"die";
                //if(j==10) cout<<num<<"  ";
                //if(num>10000000) break;
                //cout<<prime[num]<<" ";
                if(num>10000000)
                {
                    ll xx=isprime(num);
                    if(xx==-1)
                    {
                        v=0;
                        break;
                    }
                    else
                    {
                        //if(j==10) cout<<num<<" ";
                        v=1;
                        fact2[j]=xx;
                    }
                }
                /*if(num>10000000)
                {
                    v=0;
                    break;
                }*/

                else
                {
                    if(prime[num]==0)
                    {
                        //cout<<"lol";
                        v=0;
                        break;
                    }
                    else
                    {
                        v=1;
                        fact2[j]=fact[num];
                    }
                }
            }
            if(v==1)
            {
                for(ll i=0; i<n; i++) printf("%lld",s[i]);
                printf(" ");
                for(ll i=2; i<=10; i++) printf("%lld ",fact2[i]);
                printf("\n");
                count++;
                v=0;
            }
            if(count==j) break;
        }


    }
    //cout<<fact[4];
    return 0;
}
