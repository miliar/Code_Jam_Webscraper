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
    long n,r;
    cin>>n;
   // while(n--)
    for(r=1;r<=n;r++)
    {
        long a,b,s,i,ss,p,l;
        cin>>a>>b;
        s=sqrt(a);
        if(s*s==a)
        i=s;
        else
        i=s+1;
        ss=0;
        for(i=i;i*i<=b;i++)
        {
            p=i;
            long pp=i*i;
            string aa="",aaa="";
            string bb="",bbb="";
            char ab[10001]={0};
            char abb[10001]={0};
            sprintf(ab,"%ld",p);
            sprintf(abb,"%ld",pp);
            l=strlen(ab);
            long ll=strlen(abb);
            if(ll==1)
            ss++;
            else
            {
            aa=ab;
            bb=abb;
           // aa.reserve();
            reverse(ab,ab+l);
            reverse(abb,abb+ll);
            aaa=ab;
            bbb=abb;
          //  cout<<aaa<<" "<<aa;
            if(aaa==aa&&bbb==bb)
            {
               // cout<<aaa<<" ";
                ss++;
            }
            }

        }
        printf("Case #%ld: %ld\n",r,ss);
        //cout<<ss<<endl;
    }
}
