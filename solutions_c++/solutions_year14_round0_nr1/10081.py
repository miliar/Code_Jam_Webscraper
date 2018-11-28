#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cassert>
#include <vector>
#include <algorithm>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <ctime>
#define pb push_back
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

int common(int *a,int *b)
{
     int i,j,k,ans=0;
     FOR(i,0,3)
          FOR(j,0,3)
          {
               if (a[i] == b[j] && ans==0)
                    ans = a[i];
               else if (a[i] == b[j])
                    return -1;
          }
     return ans;

}

int main()
{
     #ifndef ONLINE_JUDGE
     f_in("in1.txt");
     f_out("out1.txt");
     #endif
     st_clk
     srand(time(NULL));
     int t,i,k,j;
     cin>>t;
     for (k=0;k<t;k++)
     {
          int ans1,mat1[4][4],ans2,mat2[4][4];
          cin>>ans1;
          FOR(i,0,3)
               FOR(j,0,3)
                    cin>>mat1[i][j];
          cin>>ans2;
          FOR(i,0,3)
               FOR(j,0,3)
                    cin>>mat2[i][j];
          int ret = common(mat1[ans1-1],mat2[ans2-1]);
          if (ret>0)
               cout<<"Case #"<<k+1<<": "<<ret<<endl;
          else if (ret==-1)
               cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
          else
               cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
     }
     
return 0;
}