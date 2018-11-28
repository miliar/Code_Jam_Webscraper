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
#include<queue>
#include<sys/time.h>
#include<fstream>
#include<bitset>
#include<cstring>
#include<iomanip>
#include <unistd.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

typedef long long int tint;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A2.out","w",stdout);
    int T;
    cin>>T;
    forn(t,T)
    {
        int n;
        tint p;
        cin>>n>>p;
        tint r1=(1LL<<n)-1,r2=(1LL<<n)-1,pp=p;
        vector<int>vp;
        forn(i,n+1)
        {
            vp.pb(pp%2);
            pp/=2;
        }
        reverse(all(vp));
        //forn(i,n+1)cerr<<vp[i]<<" ";cerr<<endl;
        if(vp[0]==0)
        {
            int j=1;
            while(vp[j]==0)j++;
            r2=(1LL<<n)-(1LL<<j);
            vp.clear();
            pp=p-1;
            forn(i,n+1)
            {
                vp.pb(pp%2);
                pp/=2;
            }
            reverse(all(vp));
            j=1;
            while(vp[j]==1)j++;
            //cerr<<j<<endl;
            r1=(1LL<<j)-2;
        }
        /*forn(i,(1LL<<n))
        {
            //mas ganadas
            int mg=log2((1LL<<n)-i+1e-9);
            //cerr<<mg<<endl;
            //mas perdidas
            int mp=log2(i+1+1e-9);
            vector<int>rg,rp;
            rg.pb(0);rp.pb(0);
            forn(i,mg)rg.pb(0);
            while(rg.size()<n+1)rg.pb(1);
            forn(i,mp)rp.pb(1);
            while(rp.size()<n+1)rp.pb(0);
            if(rg<vp)r2=i;
            if(rp>=vp)r1=min(r1,(tint)i)-1;
        }*/
        cout<<"Case #"<<t+1<<": "<<r1<<" "<<r2<<endl;
    }
}
