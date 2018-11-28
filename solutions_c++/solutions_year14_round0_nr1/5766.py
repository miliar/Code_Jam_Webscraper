#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<queue>
#include<complex>
#include<set>
#include<map>
#include<sstream>
#include<string>
#include<deque>
#include<sys/time.h>
#include<fstream>
#include<bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int a[4][4],b[4][4];

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int u,v,ans;
        cin>>u;
        forn(i,4)forn(j,4)cin>>a[i][j];
        cin>>v;
        u--;
        v--;
        forn(i,4)forn(j,4)cin>>b[i][j];
        int s=0;
        forn(k,16)
        {
            bool x1=false,x2=false;
            forn(j,4)if(a[u][j]==k+1)x1=true;
            forn(j,4)if(b[v][j]==k+1)x2=true;
            if(x1 and x2)
            {
                ans=k+1;
                s++;
            }
        }
        if(s==0)
        {
            cout<<"Case #"<<t+1<<": "<<"Volunteer cheated!"<<endl;
        }else if(s>1)
        {
            cout<<"Case #"<<t+1<<": "<<"Bad magician!"<<endl;
        }else
        {
            cout<<"Case #"<<t+1<<": "<<ans<<endl;
        }        
    }
}

