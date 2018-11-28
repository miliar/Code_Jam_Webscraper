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
bool palin(LL x)
{
     LL rev=0,temp=x;
     while (temp)
     {
           rev=rev*10+temp%10;
           temp/=10;
     }
     if (rev==x)
        return 1;
     return 0;
}
LL limit=(int)1e7 + 1;
vector<LL> v;
void precalc()
{
     LL i;
     FOR(i,1,limit)
     {
                   if (palin(i) && palin(i*i))
                      v.push_back(i*i);
     }
}
int main()
{
     #ifndef ONLINE_JUDGE
     f_in("C-large-1.in");
     f_out("out.txt");
     #endif
     int t,i,k=1;
     precalc();
     //cout<<v.size()<<endl;
     //FOR(i,0,v.size()-1) cout<<v[i]<<endl;
     cin>>t;
     while (t--)
     {
           cout<<"Case #"<<k++<<": ";
           LL a,b,ans=0;
           cin>>a>>b;
           i=0;
           while (i<v.size()) 
           {
                 if(v[i]>=a && v[i]<=b)
                 {
                 ans++;
                 }
           i++;
           }
           cout<<ans<<endl;
            

     }

//system("pause");
return 0;
}
