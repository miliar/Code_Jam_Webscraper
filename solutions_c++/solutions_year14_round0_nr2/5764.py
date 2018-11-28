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
#include<iomanip>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        double c,f,x,cs=2;
        double cu=0;
        double s=0;
        double m=100000;
        cin>>c>>f>>x;
        forn(i,x)
        {
            m=min(m,s+x/cs);
            s+=c/cs;
            cs+=f;
        }
        cout<<setprecision(10)<<fixed<<"Case #"<<t+1<<": "<<m<<endl;
    }
}

