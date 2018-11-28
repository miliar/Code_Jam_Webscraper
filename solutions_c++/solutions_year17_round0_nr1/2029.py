/* بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
/* رَّبِّ زِدْنِى عِلْمًا */


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
#include <map>
#include <list>
#include <stack>
#include <set>
#include <deque>

using namespace std;

#define OUTPUT freopen("myfile.txt","w",stdout);
#define INPUT freopen("A-large.in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 100005
#define MOD 1000000007
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back
#define ppb pop_back
#define setBit(a,n) a|(1<<n)
#define setBitStatement(a,n) a|=1<<n;
#define resetBit(a,n) a&=~(1<<n);
#define checkBit(a,n) ((a&(1<<n))!=0)
#define toggleBit(a,n) a^=1<<n;
#define floatingEqual(a,b) (fabs(a-b)<=EPS)
#define floatingLess(a,b) ((b-a)>=EPS)
#define floatingGreater(a,b) ((a-b)>=EPS)

#define INF 1000000000

char inp[100005];

int main()
{
    // Bismillahir Rahmanir Rahim
    // Rabbi Zidni Ilma

    int T,tp=1;
    int N,K;
    int i,j,cnt;

    INPUT
    OUTPUT

    getInt(T)

    while(T--)
    {
        scanf("%s",inp);
        getInt(K)

        cnt = 0;

        N = strlen(inp);

        for(i=0;;i++)
        {
            if((i+K)>N)
            {
                break;
            }

            if(inp[i]=='-')
            {
                cnt++;

                for(j=0;j<K;j++)
                {
                    if(inp[i+j]=='+')
                    {
                        inp[i+j]='-';
                    }

                    else
                    {
                        inp[i+j]='+';
                    }
                }
            }
        }

        for(i=0;i<N;i++)
        {
            if(inp[i]=='-')
            {
                cnt = -1 ;
            }
        }

        if(cnt==-1)
        {
            printf("Case #%d: IMPOSSIBLE\n",tp);
        }

        else
        {
            printf("Case #%d: %d\n",tp,cnt);
        }

        tp++;
    }


    return 0;
}
