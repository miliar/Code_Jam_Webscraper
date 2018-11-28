#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1001001001
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

int tab[10][10];
int odwr[10];

void pre()
{
    tab[1][1]=1;
    tab[1][2]=2;
    tab[1][3]=3;
    tab[1][4]=4;

    tab[2][1]=2;
    tab[2][2]=-1;
    tab[2][3]=4;
    tab[2][4]=-3;

    tab[3][1]=3;
    tab[3][2]=-4;
    tab[3][3]=-1;
    tab[3][4]=2;

    tab[4][1]=4;
    tab[4][2]=3;
    tab[4][3]=-2;
    tab[4][4]=-1;

    odwr[1] = 1;
    odwr[2] = -2;
    odwr[3] = -3;
    odwr[4] = -4;
}


int wej[10042], val[10042];

int abs(int x)
{
    if(x>=0)return x;
    return -x;
}

int sol(int a, int c)
{
    int minus=0;
    if(a<0)minus=1;
    a=abs(a);
    int aodw=odwr[a];
    if(aodw<0)minus=(minus+1)%2;
    aodw=abs(aodw);
    if(c<0)minus=(minus+1)%2;
    c = abs(c);
    int b = tab[aodw][c];
    if(minus)b*=-1;
    return b;
}

void solve(int test)
{
    cout<<"Case #"<<test<<": ";
    int l,x;
    cin>>l>>x;
    string s;
    cin>>s;
    for(int i=0;i<x;i++)
    {
        for(int j=0; j<l; j++)
        {
            if(s[j] == 'i')wej[l*i+j]=2;
            if(s[j] == 'j')wej[l*i+j]=3;
            if(s[j] == 'k')wej[l*i+j]=4;
        }
    }
    int n=l*x;
    val[0]=wej[0];
    //cout<<val[0]<<" ";
    for(int i=1;i<n;i++)
    {
        val[i] = tab[ abs(val[i-1]) ][ wej[i] ];
        if(val[i-1]<0)val[i]*=-1;
        //cout<<val[i]<<" ";
    }
    //cout<<endl;
    for(int i=0; i<n; i++)
    {
        for(int j=i+1; j<n; j++)
        {

            if(val[i]!=2)continue;
            //cout<<"1 i j "<<i<<"  "<<j<<endl;
            int c = val[j];
            int a = val[i];
            if(sol(a,c)!=3)continue;
            //cout<<"2 i j "<<i<<"  "<<j<<endl;
            c = val[n-1];
            a = val[j];
            //cout<<"2 c a "<<c<<" "<<a<<endl;
            if(sol(a,c)!=4)continue;
            //cout<<"3 i j "<<i<<"  "<<j<<endl;
            cout<<"YES\n";
            return;
        }
    }
    cout<<"NO\n";
}

int main()
{
    pre();
    IOS
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)solve(i);
    return 0;
}
