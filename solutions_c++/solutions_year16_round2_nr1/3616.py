#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define F first
#define S second
#define maxs 100045
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)

using namespace std;
   char z[30];
vector<int>v;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    CASET{

        int c,d,e,f,g,h,i,j,k,p,q;

        cout<<"Case #"<<case_n++<<": ";

        v.clear();
        memset(z,0,sizeof(z));
        string s;
        cin>>s;
        //b=strlen(s);
        for(int j=0;j<s.length();j++)
        {
            z[s[j]-'A']++;
        }
        for(int i=0;i<=9;i++)
        {
            if(i==9)
            {
                c=z['N'-'A']/2;
                d=z['I'-'A'];
                e=z['E'-'A'];
                f=min(c,d);
                f=min(e,f);
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['N'-'A']-=2*f;
                z['I'-'A']-=f;
                z['E'-'A']-=f;


            }
            else if(i==8)
            {   c=z['H'-'A'];
                f=z['G'-'A'];
                d=z['I'-'A'];
                e=z['E'-'A'];
                g=z['T'-'A'];
                h=min(c,d);
                h=min(h,e);
                h=min(h,f);
                h=min(h,g);
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['H'-'A']-=h;
                z['G'-'A']-=h;
                z['I'-'A']-=h;
                z['E'-'A']-=h;
                z['T'-'A']-=h;

            }
            else if(i==7)
            {
                c=z['E'-'A']/2;
                d=z['S'-'A'];
                e=z['V'-'A'];
                f=z['N'-'A'];
                g=min(c,d);
                g=min(g,e);
                g=min(g,f);
                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['E'-'A']-=g*2;
                z['S'-'A']-=g;
                z['V'-'A']-=g;
                z['N'-'A']-=g;

            }
            else if(i==6)
            {
                c=z['S'-'A'];
                d=z['I'-'A'];
                e=z['X'-'A'];
                f=min(c,d);
                f=min(f,e);
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['I'-'A']-=f;
                z['X'-'A']-=f;
                z['S'-'A']-=f;

            }
            else if(i==5)
            {
                c=z['F'-'A'];
                d=z['I'-'A'];
                e=z['V'-'A'];
                f=z['E'-'A'];
                g=min(c,d);
                g=min(g,e);
                g=min(g,f);
                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['F'-'A']-=g;
                z['I'-'A']-=g;
                z['V'-'A']-=g;
                z['E'-'A']-=g;

            }
            else if(i==4)
            {
                c=z['F'-'A'];
                d=z['O'-'A'];
                e=z['U'-'A'];
                f=z['R'-'A'];
                g=min(c,d);
                g=min(g,e);
                g=min(g,f);
                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['F'-'A']-=g;
                z['O'-'A']-=g;
                z['U'-'A']-=g;
                z['R'-'A']-=g;
            }
            else if(i==3)
            {
                c=z['E'-'A']/2;
                d=z['H'-'A'];
                e=z['T'-'A'];
                f=z['R'-'A'];
                g=min(c,d);
                g=min(g,e);
                g=min(g,f);
                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['E'-'A']-=g*2;
                z['H'-'A']-=g;
                z['T'-'A']-=g;
                z['R'-'A']-=g;
            }
            else if(i==2)
            {
                c=z['T'-'A'];
                d=z['W'-'A'];
                e=z['O'-'A'];
                f=min(c,d);
                f=min(f,e);
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['T'-'A']-=f;
                z['W'-'A']-=f;
                z['O'-'A']-=f;
            }
            else if(i==1)
            {
                c=z['O'-'A'];
                d=z['N'-'A'];
                e=z['E'-'A'];
                f=min(c,d);
                f=min(f,e);
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['O'-'A']-=f;
                z['N'-'A']-=f;
                z['E'-'A']-=f;
            }
            else if(i==0)
            {
                c=z['Z'-'A'];
                d=z['E'-'A'];
                e=z['R'-'A'];
                f=z['O'-'A'];
                g=min(c,d);
                g=min(g,e);
                g=min(g,f);
                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['Z'-'A']-=g;
                z['E'-'A']-=g;
                z['R'-'A']-=g;
                z['O'-'A']-=g;
            }
        }
        for(i=0;i<v.size();i++)
            cout<<v[i];
        cout<<endl;
    }
}
