#include <bits/stdc++.h>
#define sflld(n) scanf("%lld",&n)
#define sfulld(n) scanf("%llu",&n)
#define sfd(n) scanf("%d",&n)
#define sfld(n) scanf("%ld",&n)
#define sfs(n) scanf("%s",&n)
#define ll long long
#define s(t) int t; while(t--)
#define ull unsigned long long int
#define pflld(n) printf("%lld\n",n)
#define pfd(n) printf("%d\n",n)
#define pfld(n) printf("%ld\n",n)
#define lt 2*idx
#define rt 2*idx+1
#define f(i,k,n) for(i=k;i<n;i++)
#define MAXN 0

using namespace std;

int a[26],dig[10];
int main()
{
    int t,ts=0,i;
    string s;
    sfd(t);
    f(ts,0,t)
    {
        cin>>s;
        memset(dig,0,sizeof(dig));
        memset(a,0,sizeof(a));

        int len=s.length();
        f(i,0,len)
        {
            a[s[i]-'A']++;
        }
        if(a['Z'-'A'])
        {
            dig[0]+=a['Z'-'A'];
            a['E'-'A']-=a['Z'-'A'];
            a['R'-'A']-=a['Z'-'A'];
            a['O'-'A']-=a['Z'-'A'];
            a['Z'-'A']=0;
        }
        if(a['W'-'A'])
        {
            dig[2]+=a['W'-'A'];
            a['T'-'A']-=a['W'-'A'];
            a['O'-'A']-=a['W'-'A'];
            a['W'-'A']=0;
        }
        if(a['U'-'A'])
        {
            dig[4]+=a['U'-'A'];
            a['F'-'A']-=a['U'-'A'];
            a['R'-'A']-=a['U'-'A'];
            a['O'-'A']-=a['U'-'A'];
            a['U'-'A']=0;
        }
        if(a['X'-'A'])
        {
            dig[6]+=a['X'-'A'];
            a['S'-'A']-=a['X'-'A'];
            a['I'-'A']-=a['X'-'A'];
            a['X'-'A']=0;
        }
        if(a['G'-'A'])
        {
            dig[8]+=a['G'-'A'];
            a['E'-'A']-=a['G'-'A'];
            a['I'-'A']-=a['G'-'A'];
            a['H'-'A']-=a['G'-'A'];
            a['T'-'A']-=a['G'-'A'];
            a['G'-'A']=0;
        }
        if(a['S'-'A'])
        {
            dig[7]+=a['S'-'A'];
            a['E'-'A']-=2*a['S'-'A'];
            a['V'-'A']-=a['S'-'A'];
            a['N'-'A']-=a['S'-'A'];
            a['S'-'A']=0;
        }
        if(a['F'-'A'])
        {
            dig[5]+=a['F'-'A'];
            a['I'-'A']-=a['F'-'A'];
            a['V'-'A']-=a['F'-'A'];
            a['E'-'A']-=a['F'-'A'];
            a['F'-'A']=0;
        }
        if(a['T'-'A'])
        {
            dig[3]+=a['T'-'A'];
            a['E'-'A']-=2*a['T'-'A'];
            a['R'-'A']-=a['T'-'A'];
            a['H'-'A']-=a['T'-'A'];
            a['T'-'A']=0;
        }
        if(a['I'-'A'])
        {
            dig[9]+=a['I'-'A'];
            a['N'-'A']-=2*a['I'-'A'];
            a['E'-'A']-=a['I'-'A'];
            a['I'-'A']=0;
        }
          if(a['O'-'A'])
        {
            dig[1]+=a['O'-'A'];
            a['E'-'A']-=a['O'-'A'];
            a['N'-'A']-=a['O'-'A'];
            a['O'-'A']=0;
        }
        cout<<"Case #"<<ts+1<<": ";
        f(i,0,10)
        {
            if(dig[i])
            {
                while(dig[i])
                    {
                        cout<<i;
                        dig[i]--;
                    }
            }
        }
        cout<<endl;
    }
    return 0;
}
