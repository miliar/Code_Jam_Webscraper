#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<queue>
#include<utility>
using namespace std;

//#define inp(a) scanf("%d",&a)
#define out(a) printf("%d\n",a)
#define inpll(a) scanf("%lld",&a)
#define outll(a) printf("%lld\n",a)

#define swap(a,b) {a=a+b;a=a-b;b=a-b;}
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>

#define ll long long int
#define mod 1000000007

#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define rep(i,a,b) for(i=a;i<b;i++)


inline void inp(int *n)
{
    *n = 0;
    int ch = getchar_unlocked();
    while(ch < '0' || ch > '9')
    {
        ch = getchar_unlocked();
    }
    while(ch >= '0' && ch <= '9')
        (*n) = ((*n)<<3) + ((*n)<<1) + ch - '0', ch = getchar_unlocked();
}

int main()
{
    int i,j,t,m1[4][4],m2[4][4],r1,r2,c,count=0,x;
    inp(&t);
    while(t--)
    {
        count++;c=0;
        inp(&r1);
        rep(i,0,4)
         rep(j,0,4)
           inp(&m1[i][j]);
        inp(&r2);
        rep(i,0,4)
         rep(j,0,4)
           inp(&m2[i][j]);
        rep(i,0,4)
         rep(j,0,4)
            if(m1[r1-1][i]==m2[r2-1][j])
            {
                c++;
                x=m1[r1-1][i];
                break;
            }
        if(c==1)
            printf("Case #%d: %d\n",count,x);
        else if(c==0)
            printf("Case #%d: Volunteer cheated!\n",count);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",count);

    }
    return 0;
}
