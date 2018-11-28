#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf("%c", &x)
#define pf(x) printf("%d", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define ENDL printf("\n")
#define INF 2147483647
#define min(x,y) x<y?x:y
#define max(x,y) x>y?x:y
#define pf2(x,y) printf("%d %d", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)

using namespace std;

typedef long long ll;

inline void PAUSE()
{
     char tmp;
     cin>>tmp;
}

double c,f,x;

double magic(int i)
{
       double s=0;
       int k=i;
       for(;i>0; i--)
       {
            s+=c/(2+(i-1)*f);
       }
       s+=x/(2+k*f);
       return s;
}

double sum(int k)
{
       //if(k==0) return 0.5;
       //return 1.0/(2+k*f)+sum(k-1);
       double s=0;
       for(; k>=0; k--)
       s+=1.0/(2+k*f);
       return s;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    sf(t);

    double res=0;
    double qwe,asd;
    for(int i=1; i<=t; i++)
{
    scanf("%lf %lf %lf", &c, &f, &x);
    qwe=x/2;
    asd=c/2+x/(2+f);
    int k=int(x/c);
    k>4 ? (k-=4) : k=1;
    //k=1;
    while(qwe>asd)
    {
         qwe=asd;
         asd=c*sum(k)+x/(2+(k+1)*f);
         k++;
    }
    printf("Case #%d: %1.8lf\n",i,qwe);
}
    PAUSE();
    return 0;
}
