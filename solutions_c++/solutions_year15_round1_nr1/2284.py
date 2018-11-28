#include <bits/stdc++.h>
#define ll long long
#define eps 1e-9
#define PI 2 * acos (0.0)
#define mod 1000000007
using namespace std;

int bs(int *st,int *en,int val,char c) // en = size+1
{
    int k;
    //first element not less than val,else returns last
    if(c=='l') k=lower_bound(st,en,val)-st;
    //first element greater than val,else returns last
    if(c=='u') k=upper_bound(st,en,val)-st;
    return k;
}

int prime[78500];
int sieve() // RETURNS ACTUAL SIZE!!! NOT SIZE+1!!!! REMEMBER WELL!! >_<
{
    int a,b,c;
    c=0; prime[c]=2;
    bool *m=(bool *)calloc(1000006,sizeof(bool));
    for(a=3;a<=1000000;a=a+2)
    {
        if(!m[a])
        {
            prime[++c]=a;
            for(b=2*a;b<=1000000;b=b+a) m[b]=true;
        }
    }
    free(m);
    return c;
}

// inverse mod of i%prime = bigmod(i,prime-2)
ll bigmod(ll i,ll pow)
{
	if(pow<1) return 1;
	if(pow==1) return i%mod;
	ll j;
	if(pow%2)
	{
		j=(i*bigmod(i,pow-1))%mod;
	}
	else
	{
		j=bigmod(i,pow/2);
		j=(j*j)%mod;
	}
	return j;
}

int ar[100005];

int main()
{

    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    /*
    cout << fixed << setprecision(4);
    std::ios::sync_with_stdio(false);

	*/

	int a,b,c,d,e,x,y,z,t,te,n;

	scanf("%d",&te);

	for(t=1;t<=te;t++)
	{
	    printf("Case #%d: ",t);
	    scanf("%d",&n);
	    d=0;
	    for(a=0;a<n;a++) {  scanf("%d",&ar[a]); d=d+ar[a]; }

	    for(a=1;a<n;a++) if(ar[a]!=ar[a-1]) break;

	    z=0;
	    for(a=1;a<n;a++)
	    {
	        if(ar[a]<ar[a-1]) z=z+ar[a-1]-ar[a];
	    }

	    d=0;
	    for(a=1;a<n;a++)
	    {
	        if(ar[a]<ar[a-1]) d=max(d,ar[a-1]-ar[a]);
	    }
	    y=0;
	    for(a=0;a<n-1;a++)
	    {
	        if(ar[a]>d) y=y+d;
	        else y=y+ar[a];
	    }

	    printf("%d %d\n",z,y);
	}

    return 0;
}
