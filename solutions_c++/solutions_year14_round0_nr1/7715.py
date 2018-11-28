// profile : sunnyLA4
 
// fundamentals headers
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
 
 
using namespace std;
 
#define SIZE 4000000
 
 
#define FOR(i,a,b)                  for(int i=a;i<b;i++)
#define REP(i,n)                    FOR(i,0,n)
#define s(n)                        scanf("%d",&n)
#define su(n)                       scanf("%u",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
 
typedef long long LL;
typedef unsigned int uI;
typedef unsigned long long uLL;
 
int readint()
{
    int t=0;
    char c,ch;
    ch=getchar();
    if (ch=='-') c=getchar();
    else c=ch;
    while (c<'0' || c>'9')
        c=getchar();
    while (c>='0' && c<='9')
    {
        t= (t<<3)+ (t<<1)+c-'0';
        c=getchar();
    }
    if (ch=='-') return -t;
    else return t;
}

 
int main()
{
 
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.in","w",stdout);
    int tc,p=0;
    s(tc);
    int c1,c2;
    int a1[4][4],a2[4][4];

    while(tc--){
        p++;
        int count=0,temp;
        s(c1);
        FOR(i,0,4)
        {   
            FOR(j,0,4)
            {
                s(a1[i][j]);
            }
        }
        s(c2);
        FOR(i,0,4)
        {   
            FOR(j,0,4)
            {
                s(a2[i][j]);
            }
        }

        FOR(i,0,4)
        {
            FOR(j,0,4)
            {
                if(a1[c1-1][i] == a2[c2-1][j])
                {
                    count++;
                    temp = a1[c1-1][i];
                }
            }
        }

        printf("Case #%d: ",p);
        
        if (count == 1)
        {
            printf("%d\n",temp);
        }
        else if (count == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }

    }    

    return 0;
}
 