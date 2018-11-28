#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define pli pair<ll,int>
#define f first
#define s second
#define pii pair<int,int>
using namespace std;
int read()
{
    int x;
    scanf("%d",&x);
    return x;
}
ll Power(int a, int b)
{
    ll res =1;
    while(b)
    {
        if(b%2)res = res*(ll)a;
        b/=2;
        a*=a;
    }
    return res;
}

bool match(ll a, string s)
{
    int  n = s.length();
    for(int i=n-1;i>=0;i--)
    {
        if(s[i]=='?')
        {
            a/=10;
            continue;
        }
        if(s[i] - '0' != a%10) return false;

        a/=10;
    }

   // cout << a << endl;
    return true;
}
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int  t = read();
        for(int x=1;x<=t;x++)
    {
        string s1,s2;
        cin >> s1 >> s2;
        int n = s1.length();
        //string ans1="",ans2="";
        //cout << n << endl;
         vector<ll> a,b;
        for(int i=0;i<Power(10,n);i++)
        {
            //cout << i << endl;
            if(match(i,s1))a.pb(i);
            if(match(i,s2)) b.pb(i);
        }
vector<pair<ll,ll > > ans;
        ll Min = 10000;
for(int i=0;i<a.size();i++) for(int j=0;j<b.size();j++)
        {

            //cout << a[i] << ' ' << b[j] << endl;
            if(abs(a[i]-b[j]) < Min)
            {
                ans.clear();
                ans.pb(mp(a[i],b[j]));
                Min = abs(a[i]-b[j]);
            }
            else if(abs(a[i]-b[j])==Min) ans.pb(mp(a[i],b[j]));
        }

        sort(ans.begin(),ans.end());
        string ans1 = "", ans2="";
        for(int i=n-1;i>=0;i--)
        {
            ans1 += (char) (ans[0].f % 10 + '0');
            ans[0].f /=10;
        }
        for(int i=n-1;i>=0;i--)
        {
            ans2 += (char) (ans[0].s % 10 + '0');
            ans[0].s /=10;
        }

        reverse(ans1.begin(),ans1.end());
        reverse(ans2.begin(),ans2.end());
        cout << "Case #" << x << ": " << ans1 <<  ' ' << ans2 << endl;

    }
    return 0;
}
