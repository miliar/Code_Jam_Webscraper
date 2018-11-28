#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define ms(x,y) memset(x,y,sizeof(x))
#define fr(i,x,y) for(int i=x;i<=y;i++)
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
char s[2005];
int num[222],f[15];
void doit()
{
    ms(num,0);
    scanf("%s",s);
    int len=strlen(s);
    fr(i,0,len-1) num[s[i]]++;
    f[2]=num['W'];
    num['W']-=f[2];
    num['T']-=f[2];
    num['O']-=f[2];
    f[4]=num['U'];
    num['F']-=f[4];
    num['O']-=f[4];
    num['U']-=f[4];
    num['R']-=f[4];
    f[5]=num['F'];
    num['F']-=f[5];
    num['I']-=f[5];
    num['V']-=f[5];
    num['E']-=f[5];
    f[7]=num['V'];
    num['S']-=f[7];
    num['E']-=f[7];
    num['V']-=f[7];
    num['E']-=f[7];
    num['N']-=f[7];
    f[6]=num['S'];
    num['S']-=f[6];
    num['I']-=f[6];
    num['X']-=f[6];
    f[0]=num['Z'];

    num['Z']-=f[0];
    num['E']-=f[0];
    num['R']-=f[0];
    num['O']-=f[0];
    f[1]=num['O'];
    num['O']-=f[1];
    num['N']-=f[1];
    num['E']-=f[1];
     f[3]=num['R'];
    num['T']-=f[3];
    num['H']-=f[3];
    num['R']-=f[3];
    num['E']-=f[3];
    num['E']-=f[3];
    f[8]=num['G'];
    num['E']-=f[8];
    num['I']-=f[8];
    num['G']-=f[8];
    num['H']-=f[8];
    num['T']-=f[8];
     f[9]=num['E'];
    num['N']-=f[9];
    num['I']-=f[9];
    num['N']-=f[9];
    num['E']-=f[9];
    fr(i,0,9)
    fr(j,1,f[i])
        printf("%d",i);
    printf("\n");
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {   printf("Case #%d: ",++i);
        doit();
    }
}
