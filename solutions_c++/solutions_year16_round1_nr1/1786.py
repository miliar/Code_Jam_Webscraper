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
	freopen("A-large (1).in", "r", stdin);
	freopen("Output1.txt", "w", stdout);


long long int a,b,c,d,e;
long long int t;

//t=1;
cin>>t;
string s;
int freq[30];
for(int y=0;y<t;y++)
		{cin>>s;
		memset(freq,0,sizeof(freq));
		int l=s.size();

		list<char> ans;

		ans.push_front(s[0]);


		cout<<"Case #"<<y+1<<": ";
		for(int i=1;i<l;i++){if(ans.back()>s[i]){
            ans.push_front(s[i]);

		}
		else
        {ans.push_back(s[i]);

        }

        }
        for(int i=0;i<l;i++){

            cout<<ans.back();
            ans.pop_back();



        }










		cout<<"\n";






}




return 0;}

