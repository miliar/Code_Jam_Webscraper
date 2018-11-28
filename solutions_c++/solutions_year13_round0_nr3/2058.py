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
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

typedef long long int tint;

vector<tint> lista;

tint refl(tint x)
{
    stringstream ss,tt;
    string s,t;
    ss<<x;
    ss>>s;
    t=s;
    reverse(all(t));
    tt<<(s+t);
    tt>>x;
    return x;    
}

tint refl2(tint x)
{
    stringstream ss,tt;
    string s,t;
    ss<<x;
    ss>>s;
    t=s;
    reverse(all(t));
    t=t.substr(1,t.size()-1);
    tt<<(s+t);
    tt>>x;
    return x;    
}

bool ispal(tint x)
{
    stringstream ss;
    string s,t;
    ss<<x;
    ss>>s;
    t=s;
    reverse(all(t));
    return s==t;
}

void generar()
{
    set<tint> v;
    forn(i,10000)
    {
        tint x=refl(i),y=refl2(i);
        if(ispal(x*x) && v.find(x*x)==v.end())
        {
            v.insert(x*x);
            lista.pb(x*x);
        }
        if(ispal(y*y) && v.find(y*y)==v.end())
        {
            v.insert(y*y);
            lista.pb(y*y);
        }
    }
    sort(all(lista));
}

int main()
{
    int T;
    cin>>T;
    generar();
    //forn(i,lista.size())cout<<lista[i]<<endl;
    //cout<<lista.size()<<endl;
    forn(t,T)
    {
        tint a,b;
        cin>>a>>b;
        int res=0;
        forn(i,lista.size())if(lista[i]>=a and lista[i]<=b)res++;
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
