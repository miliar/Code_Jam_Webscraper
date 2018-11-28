#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<cctype>
#include<map>
#include<stack>
#include<cstdlib>
#include<queue>
#include<vector>
#include<algorithm>
#include<bitset>
#include<algorithm>
#include<set>
#include<limits.h>

using namespace std;
typedef long int LD;
typedef long long int LLD;
typedef float F;
typedef double LF;
typedef unsigned int U;
typedef unsigned long int LU;
typedef unsigned long long int LLU;
typedef char C;

#define sf scanf
#define sfi(x) scanf("%d",&x)
#define sfc(x) scanf("%c",&x)
#define sfi2(x,y) scanf("%d%d",&x,&y)
#define sfl(x) scanf("%ld",&x)
#define sfll(x) scanf("%lld",&x)
#define sfd(x) scanf("%lf",&x)
#define sfu(x) scanf("%llu",&x)
#define sfs(x) scanf("%s",x)
#define pf printf
#define pfi(x) printf("%d\n",x)
#define pfl(x) printf("%ld\n",x)
#define pfll(x) printf("%lld\n",x)
#define pfu(x) printf("%llu\n",x)
#define pfs(x) printf("%s\n",x)
#define pfc(x) printf("%c\n",x)
#define pb(x) push_back(x)
#define PI acos(-1.0)
#define sq(x) (x)*(x)
#define mem(x,y) memset(x,y,sizeof(x))
#define TEST int cs,T;sfi(T);for(cs=1;cs<=T;cs++)
#define nn printf("\n")
// xx-> diagonal -> 8 horizontal/vertical->4

const int xx[] = {0, 1, 0, -1, -1, 1, -1, 1};
const int yy[] = {1, 0, -1, 0, 1, 1, -1, -1};

// KX-> Knight moves
const int kx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
const int ky[] = {1, 2, 2, 1, -1, -2, -2, -1};


/******** debug **********/
#define chk1 printf("hi......1\n")
#define chk2 printf("hi......2\n")




#define mod 1000003
#define eps 10e-8
#define sz 105
#define sz1 1007
#define sz2 300009
/******* start my code ********/
char str[sz1];
deque<char>dq;
int main()
{
    int i,j,k,x,ans,l,n,mn,t,N_mn,mx,m;
    char ch,ch1;
    bool key=1,flag=1;
    LLD p,q,res,a,b;
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     sfi(m);
    for(x=1;x<=m;x++)
    {
        sfs(str);
        dq.pb(str[0]);
        ch=str[0];
        for(i=1; str[i]; i++)
        {
            if(ch<=str[i])
            {
                dq.push_front(str[i]);
                ch=str[i];
            }
            else dq.pb(str[i]);

        }
        pf("Case #%d: ",x);
        l=strlen(str);
        for(i=0; i<l; i++)
            pf("%c",dq[i]);
        nn;
        dq.clear();
       // memset(str,'\0',sizeof(str));
    }
    return 0;
}


/*


*/
