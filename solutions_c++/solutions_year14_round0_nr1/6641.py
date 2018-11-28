#include<bits/stdc++.h>

using namespace std;

typedef long long LL;

#define REP(i,n) FOR(i,0,n)
#define REPR(i,n) FORR(i,n,0)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORR(i,a,b) for(int i=a;i>=0;i--)
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define inf mod

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-small-attempt0.in","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    ios_base::sync_with_stdio(false);
    int t,r1,r2,temp,a1[4],a2[4];
    cin>>t;
    REP(i,t)
    {
        cout<<"Case #"<<i+1<<": ";
        cin>>r1;
        REP(j,(r1-1)*4)
            cin>>temp;
        REP(j,4)
            cin>>a1[j];
        REP(j,16-r1*4)
            cin>>temp;
        cin>>r2;
        REP(j,(r2-1)*4)
            cin>>temp;
        REP(j,4)
            cin>>a2[j];
        REP(j,16-r2*4)
            cin>>temp;
        sort(a1,a1+4);
        sort(a2,a2+4);
        int c=0,an;
//        REP(j,4)
//        {
//            cout<<a1[j]<<' '<<a2[j]<<endl;
//        }
        REP(j,4)
        {
            REP(k,4)
            {
                if(a1[j]==a2[k])
                {
                    c++;
                    an=a1[j];
                }
            }
        }
        if(c==1)
            cout<<an<<endl;
        else if(c==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(c>1)
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
