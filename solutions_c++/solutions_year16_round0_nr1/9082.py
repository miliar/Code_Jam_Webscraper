#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<time.h>
#include<new>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<ctype.h>
#include<string>
#include<iterator>
#include<bitset>
#include<map>
#include<set>
#include<utility>
#include<memory.h>
#include<cstdlib>
#define IOS ios_base::sync_with_stdio(false);\
cin.tie(NULL);cout.tie(NULL);
#define PI 2*acos(0)
#define inf 0x3f3f3f3f
#define inf2 2305843009213693952LL
#define F first
#define S second
#define pp cout<<
#define ppb push_back
#define ppf push_front
#define ll long long
#define ull unsigned long long
#define ssi(x) scanf("%d",&x)
#define ssl(x) scanf("%lld",&x)
#define ssd(x) scanf("%lf",&x)
#define ssc(x) scanf("%c",&x)
#define sss(x) scanf("%s",&x)
#define ssii(x,y) scanf("%d %d",&x,&y)
#define ssdd(x,y) scanf("%lf %lf",&x,&y)
#define sscc(x,y) scanf("%c %c",&x,&y)
#define ssss(x,y) scanf("%s %s",&x,&y)
#define fre1 freopen("A-large.in","r",stdin)
#define fre2 freopen("out_a2.txt","w",stdout)
#define feol fprintf(f,"\n")
#define sz(x) (int)x.size()
#define eol cout<<'\n'
#define ssp cout<<' '
#define ggt getchar()
#define ppt cout<<'.'
using namespace std;
int a[15];
main()
{
    fre1;
    fre2;
    ll i,j,k,l;
    ll n;
    int cas,cs=0;
    cin>>cas;
    while(cs++<cas){
    cin>>n;
    int found=0;
    i=0;
    memset(a,0,sizeof a);
    while(found < 10 && n)
    {
       i++;
       k=n*i;
//       if(k>10000000000LL) cout<<"asdasdasd\n";
       while(k)
       {
           l=k%10;
           k/=10;
           if(a[l]==0)
           {
               found++;
               a[l]=1;
           }
       }
    }

    if(found==10) cout<<"Case #"<<cs<<": "<<n*i;
    else cout<<"Case #"<<cs<<": INSOMNIA";eol;
}
}


