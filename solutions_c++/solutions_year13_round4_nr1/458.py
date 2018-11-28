#include<math.h>
#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<time.h>
#include<queue>
#include<deque>
#include<sstream>
#include<stack>
#define Pi 3.1415926535897932384626433832795
#define INF 1000000000ll
#define P 1000002013ll
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define PR 59999999ll
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define E 0.0000000001
#define FFF(x) (x<0ll?x+(1ll<<63):x)
#define FF(x) (FFF(x)%PR)
using namespace std;
const long long NN=1000021;
long long k,m,i,n,j,e,l,r,R,B,I,J,C;
long long N[NN],K[NN],SU;
pair <pair <long long,bool>,long long> a[NN];
    FILE *file1=freopen("A-small-attempt0 (1).in" ,"r",stdin );
    FILE *file2=freopen("T.txt","w",stdout);
map <long long,long long> M;
set <long long> S;
set <long long> ::iterator IT;
long long A;
struct ELE {long long x,n;} TRT;
stack <ELE> ST;
long long DIS (long long x)
{
    return (n*(n+1)/2-(n-x)*(n-x+1)/2)%P;
}
void ADD (long long x,long long c)
{
    TRT.x=x;
    TRT.n=c;
    ST.push(TRT);
}
void DEL (long long x,long long c)
{
    while (c)
    {
        if (c>=ST.top().n) {
                           TRT=ST.top();
                           c-=TRT.n;
                           A+=(DIS(x-TRT.x)*TRT.n)%P;
                           A%=P;
                           ST.pop();
                           }
        else
        {
            TRT=ST.top();
            ST.pop();
            TRT.n-=c;
            A+=(DIS(x-TRT.x)*c)%P;A%=P;
            ST.push(TRT);
            c=0;
        }
    }
}
int main()
{
    long long T,t;
    cin>>T;
    for (t=1;t<=T;t++)
    {
        A=0;
        B=0;
        M.clear();
        S.clear();
        cin>>n>>m;
        for (i=1;i<=m;i++){
        cin>>I>>J>>C;
        a[i*2]=mp(mp(J,0),C);
        a[i*2-1]=mp(mp(I,1),C);
        B+=(DIS(J-I)*C%P)%P;
        B%=P;
        S.insert(I);
        S.insert(J);
        }
        sort(a+1,a+m*2+1);
        for (i=1;i<=m*2;i++)
        if (a[i].X.Y)
        {
            SU+=a[i].Y;
            M[a[i].X.X]=SU%P;
        } else {
            SU-=a[i].Y;
            M[a[i].X.X]=SU%P;
        }
        R=0;
        for (IT=S.begin();IT!=S.end();IT++)
            K[++R]=*IT;
        for (i=1;i<=R;i++)
        {
            if (M[K[i]]>M[K[i-1]]) ADD(K[i],M[K[i]]-M[K[i-1]]);
            if (M[K[i]]<M[K[i-1]]) DEL(K[i],-M[K[i]]+M[K[i-1]]);
        }
        cout<<"Case #"<<t<<": "<<(B-A+P)%P<<endl;
    }
    return 0;
}
