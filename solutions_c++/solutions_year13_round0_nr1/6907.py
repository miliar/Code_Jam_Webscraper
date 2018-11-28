/*------------------------------------------------------------------------------------------------|
| %%%%%%%%%%%%%%%%%%%%%%%%%MD.ASANUR JAMAL ANOWAR HOSSAIN ANU%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% |
| %%%%%%%%%%%%%%%%%%%%%%%%%%COMPUTER SCIENCE AND ENGINEERING%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% |
| %%%%%%%%%%%%%%%%%%%%%%%%%%%%ISLAMIC UNIVERSITY KUSHTIA%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% |
| %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%BANGLADESH%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% |
|-------------------------------------------------------------------------------------------------*/
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <list>
#include <map>
#include <fstream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <bitset>
#include <cctype>
#include <vector>
#include <complex>
#include <ctime>
#include <deque>
#include <memory>
#include <utility>

#define S(a)        scanf("%d",&a)
#define SL(a)       scanf("%ld",&a)
#define S2(a,b)     scanf("%d%d",&a,&b)
#define SL2(a,b)    scanf("%ld%ld",&a,&b)
#define S3(a,b,c)   scanf("%d%d%d",&a,&b,&c)
#define SL3(a,b,c)  scanf("%ld%ld%ld",&a,&b,&c)
#define SLL(a)      scanf("%lld",&a)
#define SLL2(a,b)   scanf("%lld%lld",&a,&b)
#define SLL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define SS(a)       scanf("%s",a)
#define SC(a)       scanf("%c",&a)
#define SD(a)       scanf("%lf",&a)
#define P(a)        printf("%d",a)
#define PL(a)       printf("%ld",a)
#define PLL(a)      printf("%lld",a)
#define PD(a)       printf("%lf",a)
#define PC(a)       printf("%c",a)
#define PS(a)       printf("%s",a)
#define CASE(kk)    printf("Case %ld: ",kk++)
#define NL(kk)      printf("\n")
#define PI 3.14159265358979323846264338327950
#define eps 1e-9
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

using namespace std;

int main()
{
    freopen("inputa.txt","r",stdin);
    freopen("outputa.txt","w",stdout);
    long m,ii;
    cin>>m;
    for(ii=1;ii<=m;ii++)
    {
        char a[105][105];
        long aa[100];
        long i;
        for(i=0;i<4;i++)
        cin>>a[i];
        long k=1,u=0,uu=1,j,s,p;
        for(i=0;i<4;i++)
        {
        for(j=0,s=0,p=0;j<4;j++)
        {
            if(a[i][j]=='.')
            uu=0;
            if(a[i][j]=='X'||a[i][j]=='T')
            s++;
            if(a[i][j]=='O'||a[i][j]=='T')
            p++;
        }
        aa[u++]=p;
        if(s==4)
        {
            k=0;
            break;
        }
        }
         if(k==0)
        cout<<"Case #"<<ii<<": X won\n";
        else
        {
            long kk=1;
            for(i=0;i<4;i++)
            {
                for(j=0,s=0,p=0;j<4;j++)
                {
                    if(a[j][i]=='X'||a[j][i]=='T')
                    s++;
                    if(a[j][i]=='O'||a[j][i]=='T')
                     p++;
                }
                aa[u++]=p;
                if(s==4)
                {
                    kk=0;
                    break;
                }
            }
            if(kk==0)
            cout<<"Case #"<<ii<<": X won\n";
            else
            {
                for(i=0,s=0,p=0;i<4;i++)
                {
                    if(a[i][i]=='X'||a[i][i]=='T')
                    s++;
                    if(a[i][i]=='O'||a[i][i]=='T')
                     p++;
                }
                 aa[u++]=p;
                if(s==4)
                {
                    cout<<"Case #"<<ii<<": X won\n";
                }
                else
                {
                    for(i=0,j=3,s=0,p=0;i<4;i++,j--)
                    {
                        if(a[j][i]=='X'||a[j][i]=='T')
                        s++;
                        if(a[j][i]=='O'||a[j][i]=='T')
                       p++;
                    }
                    aa[u++]=p;
                    if(s==4)
                    cout<<"Case #"<<ii<<": X won\n";
                    else
                    {
                        for(i=0,k=1;i<u;i++)
                        if(aa[i]==4)
                        {
                             cout<<"Case #"<<ii<<": O won\n";
                             k=0;
                             break;
                        }
                        if(k==1)
                        {
                              if(uu==0)
                              cout<<"Case #"<<ii<<": Game has not completed\n";
                              else
                              cout<<"Case #"<<ii<<": Draw\n";
                        }
                    }
                }
            }
        }

    }

    return 0;
}
