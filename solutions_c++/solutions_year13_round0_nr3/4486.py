/*
uva :
author : rafsan
algo :
*/
#include<iostream>
#include<algorithm>
#include<bitset>
#include<cctype>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<climits>
#include<functional>
#include<istream>
#include<iterator>
#include<iomanip>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>

using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b-1);i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define PB push_back
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define PII pair<int,int>
#define PCC pair<char,char>
#define PIC pair<int,char>
#define PCI pair<char,int>
#define FST first
#define SEC second
#define VS vector<string>
#define VI vector<int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define MIN(a,b) (a>b?b:a)
#define MAX(a,b) (a>b?a:b)
#define PI acos(-1.0)
#define RADIANS(x) (((1.0 * x * PI) / 180.0))
#define DEGREES(x) (((x * 180.0) / (1.0 * pi)))
#define SINE(x) (sin(RADIANS(x)))
#define COSINE(x) (cos(RADIANS(x)))
#define SETBIT(x, i) (x |= (1 << i))
#define TANGENT(x) (tan(RADIANS(x)))
#define ARCSINE(x) (DEGREES((asin(x))))
#define RESETBIT(x, i) (x &= (~(1 << i)))
#define ARCCOSINE(x) (DEGREES((acos(x))))
#define ARCTANGENT(x) (DEGREES((atan(x))))
#define INFILE() freopen("C-small-attempt0.in","r",stdin)
#define OUTFILE()freopen("C_small.out","w",stdout)
#define IN scanf
#define OUT printf
#define LL long long
#define ULL unsigned long long
#define EPS 1e-9
#define MOD 10007
#define LIM 4
template<typename T>inline string toString(T a)
{
    ostringstream os("");
    os<<a;
    return os.str();
}
bool ispalin(LL res)
{
    string str=toString(res);
    int l=str.size();
    for(int i=0; i<=l/2; i++)
        if(str[i]!=str[l-i-1])return 0;
    return 1;
}
int arr[10000008];
int main()
{
    int ks,mn,val,state,ret;
    int a,b;
    INFILE();
    OUTFILE();
    cin>>ks;
    LL lim=1000;
    arr[0]=0;
    int tot=0;
    for(LL i=1; i<=lim; i++)
    {
        arr[i]=arr[i-1];
        if(ispalin(i)&&ispalin(i*i))
        {
            arr[i]+=1;
          //  tot=arr[i];
        }

    }
//cout<<tot<<endl;
    //FOR(i,0,10)cout<<arr[i]<<" ";

    FOR(cas,1,ks+1)
    {
        cin>>a>>b;
        a=ceil(sqrt(a));
        b=sqrt(b);
        ret=arr[b]-arr[a-1];
        cout<<"Case #"<<cas<<": "<<ret<<endl;
    }
    return 0;
}
/*

*/
