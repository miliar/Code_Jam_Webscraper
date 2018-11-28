#include <cstdio>
#include <stdlib.h>
#include <cstring>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <limits.h>
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define p(a) printf("%d ",a)
#define pl(a) printf("%lld\n",a)
#define SIZE 50000003
#define M 1000000007
#define SWAP(a,b) a= a^b, b=a^b, a=a^b
#define Z(a) memset(a,0,sizeof(a))
using namespace std;
typedef long long int ll;

/*inline int fastread()		// this is little bit slow compared to above one
{
    int i=0;
    char c=0;
    while (c<33)
        c=getchar_unlocked();
    while (c>33)
    {
		i = i*10+c-'0';
		c=getchar_unlocked();
    }
    return i;
} */
int t,i,j,k,first,second,A[4][4],B[4][4],hasht[17];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    s(t);
    for(i=1;i<=t;i++)
    {
        Z(hasht);

        s(first);

        for(k=0;k<4;k++)
            for(j=0;j<4;j++)
             s(A[k][j]);

        for(j=0;j<4;j++)
            hasht[A[first-1][j]]++;

        s(second);

        for(k=0;k<4;k++)
            for(j=0;j<4;j++)
             s(B[k][j]);

        for(j=0;j<4;j++)
            hasht[B[second-1][j]]++;

        int c=0,ans;
        for(j=1;j<17;j++)
        {
            if(hasht[j]==2)
            {
                ans=j;
                c++;
            }
        }



        if(c==1)
            printf("Case #%d: %d\n",i,ans);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",i);
        else if(c==0)
            printf("Case #%d: Volunteer cheated!\n",i);
       // for(j=1;j<17;j++)
       //     cout<<hasht[j]<<" ";
    }
}
