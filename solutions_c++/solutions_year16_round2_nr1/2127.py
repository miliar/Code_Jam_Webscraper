#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define fr(i,beg,end) for(i=beg;i<end;i++)
#define itfr(it,stl) for(it=stl.begin();it!=stl.end();it++)
#define PII pair<int,int>
#define init(x,val) memset(x,val,sizeof(x))
#define fst first
#define snd second
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,T,i,j;
    string s;
    int cnt[10];
    int alp[26];
    cin>>t;
    fr(T,1,t+1)
    {
        cin>>s;
        fr(i,0,10)
            cnt[i]=0;
        fr(i,0,26)
            alp[i]=0;
        fr(i,0,s.length())
            alp[s[i]-'A']++;
        cnt[0]+=alp[25];
        alp['E'-'A']-=alp[25];
        alp['R'-'A']-=alp[25];
        alp['O'-'A']-=alp[25];
        alp[25]=0;
        cnt[8]+=alp['G'-'A'];
        alp['E'-'A']-=alp['G'-'A'];
        alp['I'-'A']-=alp['G'-'A'];
        alp['H'-'A']-=alp['G'-'A'];
        alp['T'-'A']-=alp['G'-'A'];
        alp['G'-'A']-=alp['G'-'A'];
        cnt[6]+=alp['X'-'A'];
        alp['S'-'A']-=alp['X'-'A'];
        alp['I'-'A']-=alp['X'-'A'];
        alp['X'-'A']-=alp['X'-'A'];
        cnt[7]+=alp['S'-'A'];
        alp['E'-'A']-=alp['S'-'A'];
        alp['V'-'A']-=alp['S'-'A'];
        alp['E'-'A']-=alp['S'-'A'];
        alp['N'-'A']-=alp['S'-'A'];
        alp['S'-'A']-=alp['S'-'A'];
        cnt[5]+=alp['V'-'A'];
        alp['F'-'A']-=alp['V'-'A'];
        alp['I'-'A']-=alp['V'-'A'];
        alp['E'-'A']-=alp['V'-'A'];
        alp['V'-'A']-=alp['V'-'A'];
        cnt[4]+=alp['F'-'A'];
        alp['O'-'A']-=alp['F'-'A'];
        alp['U'-'A']-=alp['F'-'A'];
        alp['R'-'A']-=alp['F'-'A'];
        alp['F'-'A']-=alp['F'-'A'];
        cnt[2]+=alp['W'-'A'];
        alp['T'-'A']-=alp['W'-'A'];
        alp['O'-'A']-=alp['W'-'A'];
        alp['W'-'A']-=alp['W'-'A'];
        cnt[3]+=alp['T'-'A'];
        alp['H'-'A']-=alp['T'-'A'];
        alp['R'-'A']-=alp['T'-'A'];
        alp['E'-'A']-=alp['T'-'A'];
        alp['E'-'A']-=alp['T'-'A'];
        alp['T'-'A']-=alp['T'-'A'];
        cnt[9]+=alp['I'-'A'];
        alp['N'-'A']-=alp['I'-'A'];
        alp['N'-'A']-=alp['I'-'A'];
        alp['E'-'A']-=alp['I'-'A'];
        alp['I'-'A']-=alp['I'-'A'];
        cnt[1]+=alp['N'-'A'];
        cout<<"Case #"<<T<<": ";
        fr(i,0,10)
        {
            fr(j,0,cnt[i])
                cout<<i;
        }
        cout<<endl;
    }

    return 0;
}

