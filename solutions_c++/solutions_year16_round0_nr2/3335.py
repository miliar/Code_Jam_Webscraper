#include <bits/stdc++.h>
#define f first
#define s second
#define ll long long
#define pii  pair<int,int>
#define pli pair<ll,int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define mod 1000000007

using namespace std;
int read()
{
    int  x;
    scanf("%d",&x);
    return x;
}
bool cmp(pair <int, pii > a, pair <int, pii > b)
{
    return a.f > b.f;
}

int string_num(string s)
{
    int ans =s[0]-'0';
    for(int i=1;i<s.length();i++)
    {
        ans*=10;
        ans +=(s[i]-'0');

    }
    return ans;
}

void add_set(int a, set<int> &q)
{
    while(a)
    {
        int rem = a%10;
        q.insert(rem);
        a/=10;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t = read();
    for(int x=1;x<=t;x++)
    {
        string s;
        cin >> s;
        int n = s.length();
        stack<pii > a;
        int pl =0;

        if(s[0]=='+')
        {
            pl++;
            a.push(mp(1,pl));

        }
        else a.push(mp(0,pl));
        for(int i=1;i<n;i++)
        {
            if(s[i]=='+') pl++;
            int b = a.top().f;
            int y = (s[i]=='+'?1:0);
            if(b==y) continue;
            a.push(mp(y,pl));
        }
        int ans =0;
        while(!a.empty())
        {
            pii b = a.top();
            if(b.f==0 && b.s!=0) ans+=2;
            else if(b.f==0 && b.s==0) ans+=1;
            a.pop();
        }

        printf("Case #%d: %d\n",x,ans);
    }
    return 0;
}
