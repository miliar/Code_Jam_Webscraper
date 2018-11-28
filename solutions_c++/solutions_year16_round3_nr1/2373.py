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
#define sz 14
#define sz1 300
#define sz2 3000
/******* start my code ********/
class data
{
public:
    int id,val;
    data()
    {

    }
    data(int a,int b)
    {
        id=a;
        val=b;
    }
};
bool operator<(data A,data B)
{
    return A.val<B.val;
}
priority_queue<data>pq;
int main()
{
    int i,j,k,x,ans,l,n,mn,t,N_mn,mx,m;
    char ch,ch1;
    bool key=1,flag=1;
    data bal,don;

     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

    TEST
    {
        sfi(n);
        for(i=0; i<n; i++)
        {
            sfi(x);
            bal.id=i;
            bal.val=x;
            pq.push(bal);
        }
        pf("Case #%d: ",cs);
        while(!pq.empty())
        {
            bal=pq.top();
            if(bal.val!=1)
            {
                pq.pop();
                don=pq.top();
                pq.pop();
                pf("%c%c ",bal.id+'A',don.id+'A');
                bal.val--;
                don.val--;
                if(bal.val)
                    pq.push(bal);
                if(don.val)
                    pq.push(don);
            }
            else
            {
                l=pq.size();
                if(l%2)
                {
                    bal=pq.top();
                    pf("%c ",bal.id+'A');
                    pq.pop();
                    for(i=0; i<(l-1)/2; i++)
                    {
                        bal=pq.top();
                        pq.pop();
                        don=pq.top();
                        pq.pop();
                        pf("%c%c ",bal.id+'A',don.id+'A');
                    }
                }
                else
                {
                    for(i=0; i<(l/2); i++)
                    {
                        bal=pq.top();
                        pq.pop();
                        don=pq.top();
                        pq.pop();
                        pf("%c%c ",bal.id+'A',don.id+'A');
                    }
                }
            }
        }
        nn;
    }
    return 0;
}


/*
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1


*/
