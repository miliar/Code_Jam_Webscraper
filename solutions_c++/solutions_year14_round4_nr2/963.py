
#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;



template<class T>void debug(vector<T>v)
{
    for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;
}

int A[1003];
int dp[1003][1003];
int L[1003],R[1003],P[1003];
int n;

int go(int p,int l)
{


   // cout<<p<<" "<<l<<" "<<n<<endl;
    int &ret=dp[p][l];
    if(ret!=-1)return ret;



    if(p==n)
    {
        return ret=0;
    }


    //put the current on left

    int v1=go(p+1,l+1);
    int c1=L[P[p]]; // tar shamne tar theke koto gula boro ase

    //cout<<P[p]<<" "<<c1<<"**"<<endl;
    v1+=c1;

    //put the current on right

    int v2=go(p+1,l);
    int c2=R[P[p]];// tar pichone tar theke koto gula boro ase
    v2+=c2;

    ret=min(v1,v2);



    return ret;
}

int main()
{

    freopen("B-large.in","r",stdin);
   // freopen("b1.txt","w",stdout);
    int T,i,j,k,ks=0;
    cin>>T;

    while(T--)
    {
        ks++;
        cin>>n;
        vi v;
        for(i=0;i<n;i++)
        {
            cin>>A[i];
            v.pb( A[i] );
        }

        SORT(v);



        map<int,int>M;



        for(i=0;i<v.size();i++)M[v[i]]=(i);

        for(i=0;i<n;i++)
        {
            A[i]=M[A[i]];
            P[A[i]]=i;
        }

       // for(i=0;i<n;i++)cout<<A[i]<<" ";cout<<endl;
        SET(L,0);
        SET(R,0);


        for(i=0;i<n;i++)
        {
            for(j=0;j<i;j++)if(A[j]>A[i])L[i]++;
            for(j=i+1;j<n;j++)if(A[j]>A[i])R[i]++;
        }

       /* cout<<endl;
        for(i=0;i<n;i++)cout<<A[i]<<" ";cout<<endl;
        for(i=0;i<n;i++)cout<<L[i]<<" ";cout<<endl;
        for(i=0;i<n;i++)cout<<R[i]<<" ";cout<<endl;
        cout<<endl;
*/
        SET(dp,-1);



        int ans=go( 0,0 );


        printf("Case #%d: %d\n",ks,ans);








    }
    return 0;
}












