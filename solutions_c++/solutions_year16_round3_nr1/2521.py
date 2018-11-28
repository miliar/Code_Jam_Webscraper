/****** HAREE KRISHNA   ******/

//#include<bits/stdc++.h>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<list>
#include<climits>

using namespace std;

typedef long int ld;
typedef long long int lld;
typedef float f;
typedef double lf;
typedef unsigned int u;
typedef unsigned long int lu;
typedef unsigned long long int llu;
typedef char C;

#define sf scanf
#define pf printf
#define ff first
#define ss second
#define PI acos(-1.0)
#define sq(x) (x)*(x)
#define rep(i,x,cases) for(i=x;i<cases;i++)
#define repin(i,cases,x) for(i=cases;i>=x;i--)
#define nn printf("\n")
#define mem(arr,man) memset(arr,man,sizeof(arr))
#define TEST int test,zz;scanf("%d",&zz);for(test=1;test<=zz;test++)

#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d %d",&x,&y)
#define sci3(x,y,z) scanf("%d %d %d",&x,&y,&z)

#define pfi(x) printf("%d\n",x)
#define pfi2(x,y) printf("%d %d\n",x,y)
#define pfi3(x,y,z) printf("%d %d %d\n",x,y,z)

#define scl(x) scanf("%ld",&x)
#define scl2(x,y) scanf("%ld %ld",&x,&y)
#define scl3(x,y,z) scanf("%ld %ld %ld",&x,&y,&z)

#define scs(str) scanf("%s",str)

#define pfs(str) printf("%s\n",str)

#define pb push_back

// ASCII Vlaue
// A=65,Z=90,a=97,z=122,0=48,9=57

#define chk1 printf("chek1\n")
#define chk2 printf("chek2\n")
#define chk3 printf("chek3\n")
#define sz 1000005

/******   start your code   *******/

class clas
{
public:
    int indx,man;
    clas()
    {

    }
    clas(int a,int b)
    {
        indx=a;
        man=b;
    }
};
bool operator<(clas A,clas B)
{
    return A.man<B.man;
}
priority_queue<clas>pq;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    bool key;
    int i,j,k,x,ans,l,n,mn,t,N_mn,mx,m;
    char ch,ch1;
    clas gud,thap;
    TEST
    {
        sci(n);
        for(i=0; i<n; i++)
        {
            sci(x);
            gud.indx=i;
            gud.man=x;
            pq.push(gud);
        }
        pf("Case #%d: ",test);
        while(!pq.empty())
        {
            gud=pq.top();
            if(gud.man!=1)
            {
                pq.pop();
                thap=pq.top();
                pq.pop();
                pf("%c%c ",gud.indx+'A',thap.indx+'A');
                gud.man--;
                thap.man--;
                if(gud.man)
                    pq.push(gud);
                if(thap.man)
                    pq.push(thap);
            }
            else
            {
                l=pq.size();
                if(l%2)
                {
                    gud=pq.top();
                    pf("%c ",gud.indx+'A');
                    pq.pop();
                    for(i=0; i<(l-1)/2; i++)
                    {
                        gud=pq.top();
                        pq.pop();
                        thap=pq.top();
                        pq.pop();
                        pf("%c%c ",gud.indx+'A',thap.indx+'A');
                    }
                }
                else
                {
                    for(i=0; i<(l/2); i++)
                    {
                        gud=pq.top();
                        pq.pop();
                        thap=pq.top();
                        pq.pop();
                        pf("%c%c ",gud.indx+'A',thap.indx+'A');
                    }
                }
            }
        }
        nn;
    }
    return 0;
}

/*
input:

output:

*/
