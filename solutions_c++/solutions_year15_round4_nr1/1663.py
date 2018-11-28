#include<ctype.h>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

#include<complex>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

#include<algorithm>
#include<string>

#define inf             2000000000
#define infLL           1000000000LL*1000000000
#define PI              3.141592653589793238462643383279502884

#define Lp0(i,n)        for(i=0;i<n;i++)
#define rLp0(i,n)       for(i=n-1;i>=0;i--)
#define Lp1(i,n)        for(i=1;i<=n;i++)
#define rLp1(i,n)       for(i=n;i>0;i--)
#define Wh(a)           while(a)

#define Pr              printf
#define Pr1(a)          printf("%d ",a)
#define Pr2(a,b)        printf("%d %d ",a,b)
#define Pr3(a,b,c)      printf("%d %d %d ",a,b,c)
#define Pr4(a,b,c,d)    printf("%d %d %d %d ",a,b,c,d)
#define Prh(a)          printf("%hd ",a)
#define Prll(a)         printf("%lld ",a)
#define Prll2(a,b)      printf("%lld %lld ",a,b)
#define PrI64(a)        printf("%I64d ",a)
#define PrI642(a,b)     printf("%I64d %I64d ",a,b)
#define Prf(a)          printf("%f ",a)
#define Prlf(a)         printf("%lf ",a)
#define Prg(a)          printf("%g ",a)
#define Prc(a)          printf("%c ",a)
#define Prs(a)          printf("%s ",a)
#define EL              printf("\n")
#define Sc              scanf
#define Sc1(a)          scanf("%d",&a)
#define Sc2(a,b)        scanf("%d %d",&a,&b)
#define Sc3(a,b,c)      scanf("%d %d %d",&a,&b,&c)
#define Sc4(a,b,c,d)    scanf("%d %d %d %d",&a,&b,&c,&d)
#define Sch(a)          scanf("%hd",&a)
#define Scll(a)         scanf("%lld",&a)
#define Scll2(a,b)      scanf("%lld %lld ",&a,&b)
#define ScI64(a)        scanf("%I64d",&a)
#define ScI642(a,b)     scanf("%I64d %I64d ",&a,&b)
#define Scf(a)          scanf("%f",&a)
#define Sclf(a)         scanf("%lf",&a)
#define Scc(a)          scanf("%c",&a)
#define Scs(a)          scanf("%s",&a)
#define Scsl(a)         gets(a)

#define I               int
#define LLI             long long int
#define SI              short int
#define F               float
#define D               double
#define C               char
#define S               string
#define Mapii           map<int,int>
#define Mapsi           map<string,int>
#define Seti            set<int>
#define mSeti           multiset<int>
#define Heap            priority_queue<pii>
#define Vcti            vector<int>
#define Pii             pair<int,int>
#define Psi             pair<string,int>
#define Cmp             complex<double,double>
#define It              iterator
#define Be              begin()
#define En              end()
#define Si              size()
#define To              top()
#define Fr              front()
#define Fi              first
#define Se              second
#define Mkp             make_pair
#define Im              imag()
#define Re              real()

using namespace std;
int cn[200][200],n,m;
char mp[200][200];
main()
{
    int cnt,nq,q,i,j,k;
    Sc1(nq);
    Lp1(q,nq)
    {
        Sc2(n,m);
        Sc(" ");
        Lp0(i,n)
//            gets(mp[i]);
            Scs(mp[i]);
//        Lp0(i,n)
//        {
//            Prs(mp[i]);EL;
//        }
        Lp0(i,n+1)
            Lp0(j,m+1)
            {
                cn[i][j]=0;
            }
        cnt=0;
//            if(q==nq)
//                Pr("nm= %d %d\n",n,m);
        Lp0(i,n)
        {
            Lp0(j,m)
                if(mp[i][j]!='.')
                    break;
//            if(q==nq)
//                Pr("1 %d %d\n",i,j);
            cn[i][j]++;
            if(mp[i][j]=='<'&&j<m)
            {
                cnt++;
//                Pr("%d %d\n",i,j);
            }

            rLp0(j,m)
                if(mp[i][j]!='.')
                    break;
//            if(q==nq)
//                Pr("1 %d %d\n",i,j);
            if(j<0)
                continue;
            cn[i][j]++;
            if(mp[i][j]=='>')
            {
                cnt++;
//                Pr("%d %d\n",i,j);
            }
        }
        Lp0(j,m)
        {
            Lp0(i,n)
                if(mp[i][j]!='.')
                    break;
//            if(q==nq)
//                Pr("2 %d %d\n",i,j);
            cn[i][j]++;
            if(mp[i][j]=='^'&&i<n)
            {
                cnt++;
//                Pr("%d %d\n",i,j);
            }

            rLp0(i,n)
                if(mp[i][j]!='.')
                    break;
//            if(q==nq)
//                Pr("2 %d %d\n",i,j);
            if(i<0)
                continue;
            cn[i][j]++;
            if(mp[i][j]=='v')
            {
                cnt++;
//                Pr("%d %d\n",i,j);
            }
            if(cn[i][j]>=4)
            {
                cnt=-1;
                break;
            }
        }
        if(cnt!=-1)
            Pr("Case #%d: %d\n",q,cnt);
        else
            Pr("Case #%d: IMPOSSIBLE\n",q);
    }
    return 0;
}
