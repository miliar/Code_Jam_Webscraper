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


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int A[4],B[4];
    int t;
    sf(t);
    int n;
    int tmp;
    for(int i=1; i<=t; i++)
{
    sf(n);
    for(int j=0; j<4; j++)
    for(int k=0; k<4; k++)
    {
    sf(tmp);
    if(j==n-1)
    A[k]=tmp;
    }
    
    sf(n);
    for(int j=0; j<4; j++)
    for(int k=0; k<4; k++)
    {
    sf(tmp);
    if(j==n-1)
    B[k]=tmp;
    }
    int qwe=0;
    int num;
    for(int j=0; j<4; j++)
    for(int k=0; k<4; k++)
    {
         if(A[j]==B[k])
         {
              qwe++;
              num=j;
         }
    }
    if(qwe==0)
    cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
    else if(qwe>1)
    cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
    else if(qwe==1)
    cout<<"Case #"<<i<<": "<<A[num]<<endl;
    
}
    PAUSE();
    return 0;
}
