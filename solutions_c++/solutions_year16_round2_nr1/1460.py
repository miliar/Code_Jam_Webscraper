#include<bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%lld",&a)
#define f first
#define sc second
#define pb push_back
#define mp make_pair
#define inf 10e16
#define sd(a) scanf("%lf",&a)

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    ll n,t,i,j,k,l,w,ww,x,y,z;
    s(t);
    for(ll tt=1;tt<=t;tt++) {
        string s;
        cin >> s;
        l = s.length();
        ll a[27]={0};
        ll ans[11]={0};
        for(i=0;i<l;i++) {
            a[s[i]-'A']++;
        }
        ////////////zero////////
        w = a[25];
        ans[0]=w;
        a[25]-=w;
        a[4]-=w;
        a[17]-=w;
        a[14]-=w;
        ///////////two////////
        w = a[22];
        ans[2]=w;
        a[19]-=w;
        a[22]-=w;
        a[14]-=w;
        //////////four//////////
        w = a[20];
        ans[4]=w;
        a[20]-=w;
        a[14]-=w;
        a[5]-=w;
        a[17]-=w;
        ////////////one////////////
        w = a[14];
        ans[1]=w;
        a[14]-=w;
        a[4]-=w;
        a[13]-=w;
        /////////////six/////////
        w=a[23];
        ans[6]=w;
        a[23]-=w;
        a[8]-=w;
        a[18]-=w;
        ///////////eight////////
        w = a[6];
        ans[8]=w;
        a[6]-=w;
        a[4]-=w;
        a[8]-=w;
        a[7]-=w;
        a[19]-=w;
        /////////////three////////
        w = a[17];
        ans[3]=w;
        a[17]-=w;
        a[19]-=w;
        a[7]-=w;
        a[4]-=w;
        a[4]-=w;
        /////////////five////////
        w = a[5];
        ans[5]=w;
        a[5]-=w;
        a[8]-=w;
        a[21]-=w;
        a[4]-=w;
        ///////////////seven/////
        w = a[21];
        ans[7]=w;
        a[18]-=w;
        a[4]-=w;
        a[21]-=w;
        a[4]-=w;
        a[13]-=w;
        ////////////nine/////////
        w = a[8];
        ans[9]=w;
        cout<<"Case #"<<tt<<": ";
        for(i=0;i<=9;i++) {
            for(j=0;j<ans[i];j++) {
                cout<<i;
            }
        }
        cout<<endl;
    }
    return 0;
}
