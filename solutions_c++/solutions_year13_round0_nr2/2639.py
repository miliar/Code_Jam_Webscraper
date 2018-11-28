#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<algorithm>
#include<stack>
#include<set>
#include<map>
#include<math.h>
#include<ctime>
#define LL long long
#define ULL unsigned long long
#define L long
#define VCTP vector<pair<LL,LL> >
#define PII pair<LL,LL>
#define PDD pair<double,double>
#define F first
#define S second
#define FOR(i,lb,ub) for(i=lb;i<=ub;i++)
#define RFOR(i,ub,lb) for(i=ub;i>=lb;i--)
#define FORS(it,v) for(it=v.begin();it!=v.end();it++)
#define st_clk double st=clock();
#define end_clk double en=clock();
#define show_time cout<<"\tTIME="<<(en-st)/CLOCKS_PER_SEC<<endl;
#define sc(n) scanf("%d",&n)
#define scst(n) scanf("%s",n)
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
using namespace std;
 #ifndef ONLINE_JUDGE
inline int getchar_unlocked() { return getchar(); }
#endif
template <class T>
inline void r_f(T &p)
{
         char c;
         while ((c=getchar_unlocked()) < 48 || c > 57);
         p=c-48;
         while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
}
int a[101][101];
int n,m;
bool check(int i,int j,int f)
{
     int k;
     if (f==1)
     {
        FOR(k,0,m-1)
                    if (a[i][k]==2)
                       return 0;
        return 1;
     }
     else
     {
         FOR(k,0,n-1)
                     if (a[k][j]==2)
                        return 0;
         return 1;
     }
}
        
int main()
{
     #ifndef ONLINE_JUDGE
     f_in("B-small-attempt0.in");
     f_out("out.txt");
     #endif
     int t,k=1,i,j;
     cin>>t;
     while (t--)
     {
           cout<<"Case #"<<k++<<": ";
           
           cin>>n>>m;
           FOR(i,0,n-1)
           FOR(j,0,m-1) cin>>a[i][j];
           
           FOR(i,0,n-1)
           FOR(j,0,m-1)
           {
                       if (a[i][j]==1)
                       {
                          if (check(i,j,1) || check (i,j,2));
                          else {
                               cout<<"NO\n";
                               goto end;
                               }
                          }
           }
           cout<<"YES\n";
           end:;
           
           
           

     }

//system("pause");
return 0;
}
