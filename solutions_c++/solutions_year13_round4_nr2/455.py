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
#define P1 1000002013ll
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
long long n,m,i,j,k,A,B,P,L,R,C;
    FILE *file1=freopen("B-large (1).in" ,"r",stdin );
    FILE *file2=freopen("T.txt","w",stdout);
long long Ma(long long x,long long N)
{
    if (N-x>0) return Ma(x-(x-1)/2,N/2);
    return x;
}
long long Mi(long long x,long long N)
{
    if (x>1) return N/2+Mi((x-2)/2+1,N/2);
    return x;
}
int main()
{
    long long T,t;
    cin>>T;
    for (t=1;t<=T;t++)
    {
        cin>>n>>P;
        A=0;B=(1ll<<n)-1;
        while (A<B)
        {
            C=(A+B)>>1ll;
            if (Ma(C+1,(1ll<<n))<=P) A=C; else B=C-1;
            if (A+1==B) {
                if (Ma(B+1,(1ll<<n))<=P) A=B; B=A;
            }
        }
        R=A;
        A=0;B=(1ll<<n)-1;
        while (A<B)
        {
            C=(A+B)>>1ll;
            if (Mi(C+1,(1ll<<n))<=P) A=C; else B=C-1;
            if (A+1==B) {
                if (Mi(B+1,(1ll<<n))<=P) A=B; B=A;
            }
        }
        L=A;
        cout<<"Case #"<<t<<": "<<L<<" "<<R<<endl;
    }
    return 0;
}
