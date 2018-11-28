/*********************************************************************
 *          									                     *
 *          author:  sagarpatel                                      *  
 *		    problem: codejam->Problem A. Standing Ovation            *
 *		                                                             *
 *********************************************************************/
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>

typedef long long int ll;
using namespace std;

#define M 1000000007
#define RI(XX) scanf("%d",&(XX))
#define RII(XX,YY) scanf("%d%d",&(XX),&(YY))
#define RIII(XX,YY,ZZ) scanf("%d%d%d",&(XX),&(YY),&(ZZ))
#define RLI(XX) scanf("%lld",&(XX))
#define RLII(XX,YY) scanf("%lld%lld",&(XX),&(YY))
#define RLIII(XX,YY,ZZ) scanf("%lld%lld%lld",&(XX),&(YY),&(ZZ))
#define RS(XX) scanf("%s",(XX))
#define FOR(II,XX,YY) for (II=(XX);II<=(YY);II++)
#define RFOR(II,XX,YY) for (II=(XX);II>=(YY);II--)
#define REP(II,NN) FOR(II,0,(NN-1))
#define RREP(II,NN) RFOR(II,(NN-1),0)
#define MOD(XX) ((XX)%M)
#define COF(ADDR) (*ADDR)
#define PI(XX) printf("%d\n",(XX))
#define PLI(XX) printf("%lld\n",(XX))
#define PS(XX) printf("%s\n",(XX))
#define _TC() int __T; RI(__T); int _tc; REP(_tc,__T) 

int main()
{
    int i,ans,n,p;
    char s[1010];
    _TC()
    {
        ans=0;      
        RI(n);
        RS(s);   
        REP(i,n+1) s[i]=s[i]-'0';
        p=s[0];
        FOR (i,1,n)
        {
            if(i>p)
            {
                ans+=(i-p);
                p+=(i+s[i]-p);
            }
			else
            p+=s[i];
        }
        printf("Case #%d: %d\n",_tc+1,ans);
    }
    return 0;
}
