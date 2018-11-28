#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <climits>
#define LL long long
#define set_bit(aa,bb) (aa|(1<<bb))
#define check_bit(aa,bb) (aa&(1<<bb))
#define MX 120001
#define PB push_back



using namespace std;

/*

LL gcd(LL a,LL b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}

LL bigmod(LL p,LL e,LL M)
{
    if(e==0)return 1;
    if(e%2==0)
    {
        LL t=bigmod(p,e/2,M);
        return (t*t)%M;
    }
    return (bigmod(p,e-1,M)*p)%M;
}

LL modinverse(LL a,LL M)
{
    return bigmod(a,M-2,M);
}




bool is_prime[MAX];
L prime[MAX];

bool sieve()
{
    long i,j;
    prime[0]=2;
    int k=1;
    int sq=(sqrt(MAX));
    for(i=3; i<=sq; i+=2)
    {
        if(!is_prime[i])
        {
            for(j=i*i; j<=MAX; j+=(2*i))
                is_prime[j]=1;
        }
    }
    for(j=3; j<=MAX; j+=2)
    {
        if(!is_prime[j])
        {
            prime[k++]=j;
        }
    }
}


long NOD(long n)
{
    int  i,j,k;
    long sq=sqrt(n);
    long res=1;
    for(i=0; prime[i]<=sq; i++)
    {
        int cnt=1;
        if(n%prime[i]==0)
        {
            while(n%prime[i]==0)
            {
                cnt++;
                n=n/prime[i];
                if(n==1) break;
            }
            res*=cnt;
            sq=sqrt(n);
        }
    }
    if(n>1) res*=2;
    return res;
}
*/


int main()
{

    FILE *fp;
    fp=fopen("out1.txt", "w");

    int i,j,k;
    int cases=1;
    int t, ans1, ans2, op;
    cin>>t;
    while(t--)
    {
        cin>>ans1;
        int cnt[17];
        memset(cnt, 0, sizeof cnt);
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                cin>>op;
                if(i==ans1)
                    cnt[op]++;
            }
        }
        cin>>ans2;
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                cin>>op;
                if(i==ans2)
                    cnt[op]++;
            }
        }
        vector<int>V;
        V.clear();
        for(i=1; i<=16; i++)
        {
            if(cnt[i]==2)
            {
                V.PB(i);
            }
        }
        fprintf(fp, "Case #%d: ", cases++);
        if(V.size()==0)

            fprintf(fp, "Volunteer cheated!\n");
        else if(V.size()==1)
            fprintf(fp,"%d\n", V[0]);
        else
            fprintf(fp, "Bad magician!\n");

    }
    return 0;
}
/*

2
SQ 1 0
SQ 0 0
SQ 6 0
SQ 5 0



*/
