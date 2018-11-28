#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<ctype.h>
#include<deque>
#include<list>
#include<set>
#define inf (1<<30)
#define pi acos(-1.0)
#define LL long long int
#define LU unsigned long long int
#define eps 1e-9
#define mod 100000007
#define mem(a) memset(a,0,sizeof(a))
#define neg(a) memset(a,-1,sizeof(a))
#define pub(a) push_back(a)
#define pob(a) pop_back(a)
#define puf(a) push_front(a)
#define pof(a) pop_front(a)
#define mkp(a,b) make_pair(a,b)

using namespace std;
int n,m,i,j,k,l,a[1000009],b[1000009],p[1000009],ans,cn,t,x,y,z,mx,mn,s,len;
char c[1000009],d[1000009],ch;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        mem(b);
        mem(a);
        scanf("%s",c);
        len=strlen(c);
        for(i=0;i<len;i++)
        {
            a[c[i]]++;
        }
        b[0]=a['Z'];
        a['Z']-=b[0];
        a['E']-=b[0];
        a['R']-=b[0];
        a['O']-=b[0];
        b[2]=a['W'];
        a['T']-=b[2];
        a['W']-=b[2];
        a['O']-=b[2];
        b[4]=a['U'];
        a['F']-=b[4];
        a['O']-=b[4];
        a['U']-=b[4];
        a['R']-=b[4];
        b[6]=a['X'];
        a['S']-=b[6];
        a['I']-=b[6];
        a['X']-=b[6];
        b[8]=a['G'];
        a['E']-=b[8];
        a['I']-=b[8];
        a['G']-=b[8];
        a['H']-=b[8];
        a['T']-=b[8];
        b[1]=a['O'];
        a['O']-=b[1];
        a['N']-=b[1];
        a['E']-=b[1];
        b[3]=a['T'];
        a['T']-=b[3];
        a['H']-=b[3];
        a['R']-=b[3];
        a['E']-=b[3];
        a['E']-=b[3];
        b[5]=a['F'];
        a['F']-=b[5];
        a['I']-=b[5];
        a['V']-=b[5];
        a['E']-=b[5];
        b[7]=a['S'];
        a['S']-=b[7];
        a['E']-=b[7];
        a['V']-=b[7];
        a['E']-=b[7];
        a['N']-=b[7];
        b[9]=a['I'];
        printf("Case #%d: ",l);
        for(i=0;i<10;i++)
        {
            for(j=0;j<b[i];j++)
            {
                printf("%d",i);
            }
        }
        printf("\n");
    }
    return 0;
}
