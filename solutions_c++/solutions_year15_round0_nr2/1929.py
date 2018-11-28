/*
    Look at me!
    Look at me!
    Look at how large the monster inside me has become!
*/
#include<fstream>
#include<iostream>
#include<cstdio>
#include<map>
#include<typeinfo>
#include<set>
#define FIT(a,b) for(vector<int >::iterator a=b.begin();a!=b.end();a++)
#define FITP(a,b) for(vector<pair<int,int> >::iterator a=b.begin();a!=b.end();a++)
#define RIT(a,b) for(vector<int>::reverse_iterator a=b.end();a!=b.begin();++a)
#include<stack>
#define ROF(a,b,c) for(int a=b;a>=c;--a)
#include<vector>
#include<algorithm>
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#define REP(a,b) for(register int a=0;a<b;++a)
#include<cstring>
#include<bitset>
#include<cmath>
#include<iomanip>
#define f cin
#define g cout
#include<queue>
#define INF 0x3f3f3f3f
#define debug cerr<<"OK";
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld long double
#define ll long long
#define ull unsigned long long
#define eps 1.e-7
#define BUFMAX 10100100
#define N 2010
#define mod 1000000007
using namespace std;
/*
int dx[]={-1,-1,-1,0,1,1,1,0};
int dy[]={-1,0,1,1,1,0,-1,-1};
*/
priority_queue<int> pq;
int sol,x,n,te,T,y,A[4010],sca,crt;
int main ()
{

    #ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    #endif

    f>>T;
    FOR(t,1,T)
    {
        f>>n;
        sol=1010;
        crt=0;
        while(!pq.empty())
            pq.pop();
        FOR(i,1,n)
        {
           f>>A[i];
        }
        FOR(i,1,1000)
        {
            crt=0;
            FOR(j,1,n)
            {
                crt+=(A[j]+i-1)/i-1;
            }
            sol=min(sol,crt+i);
        }
        g<<"Case #"<<t<<": ";
        g<<sol<<"\n";
    }




    return 0;
}
