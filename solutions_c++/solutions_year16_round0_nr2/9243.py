#include <bits/stdc++.h>

#define mset memset
#define ll long long int
#define llu unsigned long long int
#define si(a) scanf("%lld",&a)
#define rep(i,a,n) for(i=(a);i<(n);i++)
#define pii pair<int,int>
#define pb(x) push_back(x)
#define v(x) vector<x>

using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


long long int power(long long int x,long long int y,ll mod)
{
    long long int vari,ty,my;

    if( y == 0)
        return 1;
    vari = power(x, y/2,mod);
    ty=(vari%mod)*(vari%mod);
    if (y%2 == 0)
        {

                return ty%mod;
        }
    else
        {
                my=(x%mod)*(ty%mod);
                return my%mod;
        }
}



long long int maxxi(long long int a,long long int b)
{
        return a>b?a:b;
}

long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}




struct abhi
{
       ll val;
       ll arr1;
};

struct abhi brr[100010];

bool cmp(struct abhi x,struct abhi y)
{
        return x.arr1<y.arr1;
}


ll arr[1000];

int main()
{
    freopen("C:\\Users\\abhishek.gu\\Desktop\\b.in","r",stdin);
    freopen("C:\\Users\\abhishek.gu\\Desktop\\b1.out","w",stdout);

    ll t,n,k,vari,check1,i,c,l,len,tot,sol,j;
    char stri[10010];
    si(t);

    ll tt=t;
    while(t--)
    {
        i=0;
        sol=0;
        cin>>stri;
		len = strlen(stri);

		while(true)
        {
			if(stri[i]=='-')
			{
			    while(stri[i]=='-' && i<len)
				{
					i++;
				}

				if(i!=len)
                {
					sol= sol + 1;
                    mset(stri,'+',sizeof(char)*(i+1));
				}
				else
				{
					sol= sol + 1;
					break;
				}

			}
			else
            {
				while(stri[i]=='+' && i<len)
				{
					i++;
				}

				if(i!=len)
				{
					sol=sol + 1;
					mset(stri,'-',sizeof(char)*(i+1));
                }
				else
                {
					break;
				}

			}
			i=0;
		}
		cout<<"case #"<<tt-t<<": "<<sol<<"\n";
    }

    return 0;
}
