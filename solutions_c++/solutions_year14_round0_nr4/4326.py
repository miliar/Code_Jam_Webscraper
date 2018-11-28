#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>

using namespace std;


#define FRO freopen("in.txt","r",stdin);
#define FRU freopen("out.txt","w",stdout);

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define i64 long long
//#define i64 __int64
#define pb push_back
#define mp make_pair
#define ff first
#define ss second



#define infinity 2147483647
#define pi 3.14159265358979323846
#define eps 1e-9



#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define all(a) (a).begin(),(a).end()
#define in(n,a,b) ( n>=a && n<=b )



template< class T > T sqr(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T Max(T a, T b) { return a>b?a:b; }
template< class T > T Min(T a, T b) { return a<b?a:b; }
template< class T > T abs(T a) { return a>0?a:-a; }

//int biton(int N,int pos){return N=N  bitwise_or (1<<pos);}
int bitoff(int N,int pos){return N= N & ~(1<<pos);}
bool bitcheck(int N,int pos){return (bool)(N & (1<<pos));}

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,  0,  0,  1};
//const int col[]={ 0, -1,  1,  0};

#define MOD 1000000009
#define Limit 100005

int n,m;

// optimal strategy: for each mass, ken searches a mass immediately greater than that.

int main()
{
    FRO
    FRU
    int tc,t=1,i,j,k,b,c,d;
    double a;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        vector<double>naomi,ken,ken1;
        cin>>n;
        for(i=0;i<n;i++){cin>>a;naomi.pb(a);}
        for(i=0;i<n;i++){cin>>a;ken.pb(a);}
        sort(all(naomi));
        sort(all(ken));
        ken1=ken;

        int war=0,dwar=0;
        //for dwar try to waste ken's larger massess with give aways
        //kotogular theke soto unused element exist kore
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(naomi[i]>ken[j])
                {
                    dwar++;
                    ken[j]=1.1;
                    break;
                }
            }
        }

        //normally ken koyta jite
        for(i=0;i<n;i++)
        {
            int flg=0;
            for(j=0;j<n;j++)
            {
                if(naomi[i]<ken1[j])
                {
                    flg=1;
                    ken1[j]=-1;
                    break;
                }
            }
            if(!flg)war++;
        }
        printf("Case #%d: %d %d\n",t,dwar,war);

    }
    return 0;
}

