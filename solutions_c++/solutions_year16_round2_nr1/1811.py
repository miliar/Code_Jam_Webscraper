#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

using namespace std;

int cti(char x)
{
    return (int)(x-'A');
}

int num[10],c[26],t;
char s[2005];

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        memset(num,0,sizeof(num));
        memset(c,0,sizeof(c));
        scanf("%s",s);
        for(int i=0;s[i]!='\0';i++) c[cti(s[i])]++;
        num[0]=c[cti('Z')];
        c[cti('R')]-=c[cti('Z')];
        c[cti('O')]-=c[cti('Z')];
        num[2]=c[cti('W')];
        c[cti('O')]-=c[cti('W')];
        num[4]=c[cti('U')];
        c[cti('O')]-=c[cti('U')];
        c[cti('R')]-=c[cti('U')];
        num[6]=c[cti('X')];
        c[cti('S')]-=c[cti('X')];
        c[cti('I')]-=c[cti('X')];
        num[8]=c[cti('G')];
        c[cti('I')]-=c[cti('G')];
        num[7]=c[cti('S')];
        c[cti('V')]-=c[cti('S')];
        num[5]=c[cti('V')];
        c[cti('I')]-=c[cti('V')];
        num[3]=c[cti('R')];
        num[1]=c[cti('O')];
        num[9]=c[cti('I')];
        printf("Case #%d: ",z);
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<num[i];j++)   printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
