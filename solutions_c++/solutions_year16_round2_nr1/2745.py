//Bismillahir Rahmanir Rahim
//Opu-1204026
#include<bits/stdc++.h>
using namespace std;
#define sf      scanf
#define pf      printf
#define pb      push_back
#define _       ios_base::sync_with_stdio(false);
#define ct      cin.tie(NULL);
#define ll      long long
#define eps     1e-10
#define ms(n,i) memset(n,i,sizeof n)
#define pi      2*acos(0)
#define inf     1<<30
#define fr(i,n) for(i=0;i<n;i++)
#define fr1(i,n)for(i=1;i<=n;i++)
#define nl cout<<"\n"
#define abs(x)  ((x<0)?-(x):x)
#define MAX 30005
#define sp(i)      cout<<fixed<<setprecision(i)
//STL
typedef      vector<int> vi;
typedef      vector<ll> vl;
typedef      pair<int,int>ii;
typedef      vector<ii> vii;
#define mp      make_pair
#define ft      first
#define sd      second
#define IT      iterator
#define pr(c,x) ((c).find(x)!=(c).end())
#define all(c)  c.begin(), c.end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=c.end();i++)
#define vpresent(c,x) (find(all(c),x)!=(c).end())

int a[27];
vi v;

int main()
{
  //  freopen("F:\\Coding\\in.txt","r",stdin);
   // freopen("F:\\Coding\\out.txt","w",stdout);
    int t,z,i,n,m;
    string s;
    cin>>t;
    fr1(z,t)
    {
        cin>>s;
        ms(a,0);
        v.clear();
        fr(i,s.length())a[s[i]-'A']++;
        if(a[25]>0)
        {
            fr(i,a[25])v.pb(0);
            a[4]-=a[25];
            a[17]-=a[25];
            a[14]-=a[25];
            a[25]=0;
        }
        if(a[22]>0)
        {
            fr(i,a[22])v.pb(2);
            a[19]-=a[22];
            a[14]-=a[22];
            a[22]=0;
        }
        if(a[20]>0)
        {
            fr(i,a[20])v.pb(4);
            a[5]-=a[20];
            a[14]-=a[20];
            a[17]-=a[20];
            a[20]=0;

        }
        if(a[23]>0)
        {
            fr(i,a[23])v.pb(6);
            a[18]-=a[23];
            a[8]-=a[23];
            a[23]=0;
        }
        if(a[6]>0)
        {
            fr(i,a[6])v.pb(8);
            a[4]-=a[6];
            a[8]-=a[6];
            a[7]-=a[6];
            a[19]-=a[6];
            a[6]=0;
        }
        if(a[18]>0)
        {
            fr(i,a[18])v.pb(7);
            a[4]-=a[18]*2;
            a[21]-=a[18];
            a[13]-=a[18];
            a[18]=0;
        }
        if(a[7]>0)
        {
            fr(i,a[7])v.pb(3);
            a[19]-=a[7];
            a[17]-=a[7];
            a[4]-=a[7]*2;
            a[7]=0;

        }
        if(a[21]>0)
        {
            fr(i,a[21])v.pb(5);
            a[5]-=a[21];
            a[8]-=a[21];
            a[4]-=a[21];
            a[21]=0;
        }
        if(a[14]>0)
        {
            fr(i,a[14])v.pb(1);
            a[13]-=a[14];
            a[4]-=a[14];
            a[14]=0;
        }
        if(a[13]>0)
        {
            fr(i,a[13]/2)v.pb(9);
        }
        sort(all(v));
        pf("Case #%d: ",z);
        fr(i,v.size())
        {
            pf("%d",v[i]);
        }
        pf("\n");

    }

    return 0;
}
