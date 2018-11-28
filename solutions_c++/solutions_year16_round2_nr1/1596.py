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

bool cmp(char a, char b)
{
    return a<b;
}
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int  t = read();
        for(int x=1;x<=t;x++)
    {
        string s;
        cin >> s;
        int n = s.length();
       // cout << n << endl;
        vector<int> f(26,0);
        for(int i=0;i<n;i++) f[s[i]-'A']++;

        string ans="";

        if(f['Z'-'A'])
        {

            int temp = f['Z'-'A'];
            for(int i=0;i<temp;i++) ans+="0";
            f['Z'-'A']-= temp;
            f['E'-'A']-=temp;
            f['R'-'A']-=temp;
            f['O'-'A']-=temp;
        }

        if(f['W'-'A'])
        {

            int temp = f['W'-'A'];
            for(int i=0;i<temp;i++) ans+="2";
            f['T'-'A']-= temp;
            f['W'-'A']-=temp;
            f['O'-'A']-=temp;

        }

        if(f['U'-'A'])
        {

            int temp = f['U'-'A'];
            for(int i=0;i<temp;i++) ans+="4";
            f['F'-'A']-= temp;
            f['O'-'A']-=temp;
            f['U'-'A']-=temp;
            f['R'-'A']-=temp;
        }

        if(f['X'-'A'])
        {

            int temp = f['X'-'A'];
            for(int i=0;i<temp;i++) ans+="6";
            f['S'-'A']-= temp;
            f['I'-'A']-=temp;
            f['X'-'A']-=temp;

        }

        if(f['G'-'A'])
        {

            int temp = f['G'-'A'];
            for(int i=0;i<temp;i++) ans+="8";
            f['E'-'A']-= temp;
            f['I'-'A']-=temp;
            f['G'-'A']-=temp;
            f['H'-'A']-=temp;
            f['T'-'A']-=temp;
        }

        if(f['O'-'A'])
        {

            int temp = f['O'-'A'];
            for(int i=0;i<temp;i++) ans+="1";
            f['O'-'A']-= temp;
            f['N'-'A']-=temp;
            f['E'-'A']-=temp;

        }

        if(f['R'-'A'])
        {

            int temp = f['R'-'A'];
            for(int i=0;i<temp;i++) ans+="3";
            f['T'-'A']-= temp;
            f['H'-'A']-=temp;
            f['R'-'A']-=temp;
            f['E'-'A']-=temp;
            f['E'-'A']-=temp;
        }
        if(f['F'-'A'])
        {

            int temp = f['F'-'A'];
            for(int i=0;i<temp;i++) ans+="5";
            f['F'-'A']-= temp;
            f['I'-'A']-=temp;
            f['V'-'A']-=temp;
            f['E'-'A']-=temp;

        }

        if(f['S'-'A'])
        {

            int temp = f['S'-'A'];
            for(int i=0;i<temp;i++) ans+="7";
            f['S'-'A']-= temp;
            f['E'-'A']-=temp;
            f['V'-'A']-=temp;
            f['E'-'A']-=temp;
            f['N'-'A']-=temp;
        }

        if(f['E'-'A'])
        {

            int temp = f['E'-'A'];
            for(int i=0;i<temp;i++) ans+="9";
            f['N'-'A']-= temp;
            f['I'-'A']-=temp;
            f['N'-'A']-=temp;
            f['E'-'A']-=temp;

        }

        sort(ans.begin(),ans.end(),cmp);

        cout << "Case #" << x << ": " << ans << endl;

    }
    return 0;
}
