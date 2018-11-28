/*While alive CODE*/

					/*War will happen and code will follow*/

#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pii pair<int,int>
#define ll long long
#define pb push_back
#define mk make_pair
#define pi 3.1415926535897932384626433832795

#define slld(x) scanf("%lld",&x)
#define sd(x) scanf("%d",&x)
#define sld(x) scanf("%ld",&x)
#define ss(x)  scanf("%s",x)

void debug(int* a, int n){
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << '\n';
}


ll readline() {
        ll c = getchar();
        while (c < 33)
                c = getchar();
        int k=0;
        while (c > 32) {
                k = k*10 + (ll)c-48;
                c = getchar();
        }
        return k;
}
void print(ll x) {
     static char c[30];
     ll len = 0;
     if (x == 0) {
             c[0] = '0';
             len = 1;
     }
     while (x > 0) {
             int y = x / 10;
             c[len++] = (x - y * 10) + '0';
             x = y;
     }
     while (len > 0) {
             --len;
             putchar(c[len]);
     }
}



#define mod 1000000007
ll power(ll b, ll e) {
ll x = 1, y = b;
    while(e > 0) {
        if(e%2 == 1) {
            x=(x*y);
            if(x>mod) x%=mod;
        }
        y = (y*y);
        if(y>mod) y%=mod;
        e /= 2;
    }
    return x;
}

long long md(long long x)
{if(x==0)
return 0;
    if(x>0)
    {long long j=x/mod;
    x=x-j*mod;
    return x;}
    else
    {long long j=(-1*x)/mod;
    if((-1*x)%mod==0)
        return 0;

    x=x+(j+1)*mod;
    return x;


    }



}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Output.txt", "w", stdout);

ll n;
int arr[10];

long long int t;
cin>>t;
//t=1;
for(int y=0;y<t;y++)
		{
            cin>>n;
            memset(arr,0,sizeof(arr));
            if(n==0){cout<<"Case #"<<y+1<<": INSOMNIA\n";
                        continue;

            }
            int coun=0;
           ll add=n;
            ll cur=n;
            ll temp=n;
            while(coun<10){temp=cur;
            while(cur){
                if(arr[cur%10]==0){
                    arr[cur%10]=1;
                    coun++;
                }
                cur/=10;



            }
            cur=temp;
            if(coun<10){
                cur+=add;

            }
            else
                break;






            }



            cout<<"Case #"<<y+1<<": "<<cur<<"\n";











}




return 0;}

