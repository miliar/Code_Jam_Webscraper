#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<string.h>
#include<vector>
#include<map>
using namespace std;

#define mx 10000000
#define ip freopen("a.txt","r",stdin)
#define op freopen("out.txt","w",stdout)

#define sint1(a) scanf("%d",&a)
#define sint2(a,b) scanf("%d %d",&a,&b)
#define sint3(a,b,c) scanf("%d %d %d",&a,&b,&c)


#define sch1(a) scanf("%c",&a)
#define sch2(a,b) scanf("%c %c",&a,&b)
#define sch3(a,b,c) scanf("%c %c %c",&a,&b,&c)


#define sll1(a) scanf("%lld",&a)
#define sll2(a,b) scanf("%lld %lld",&a,&b)
#define sll3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)

#define ll long long int

#define lpi0(a,b) for(int a=0;a<b;a++)
#define lpd0(a,b) for(int a=b-1;a>=0;a--)

#define lpi1(a,b) for(int a=1;a<=b;a++)
#define lpd1(a,b) for(int a=b;a>0;a--)

#define vi vector<int>
#define pii pair<int,int>
#define mp make_pair

#define pi acos(-1)

#define mm(a,b) memset(a,b,sizeof(a))


int main()
{
//    ip;
//    op;
    int t;
    int cs=1;

    sint1(t);
    getchar();
    while(t--)
    {

        char s[2100];
        int ans[12];
        int cnt[30];
        mm(ans,0);
        mm(cnt,0);
        gets(s);

        int l=strlen(s);




        for(int i=0;i<l;i++)
        {
            int x=s[i]-65;

            cnt[x]++;
        }

        int x='Z'-65;
        int p=cnt[x];
        ans[0]=p;
        cnt['Z'-65]-=p;
        cnt['E'-65]-=p;
        cnt['R'-65]-=p;
        cnt['O'-65]-=p;


        x='W'-65;
        p=cnt[x];
        ans[2]=p;
        cnt['T'-65]-=p;
        cnt['W'-65]-=p;
        cnt['O'-65]-=p;

        x='U'-65;
        p=cnt[x];
        ans[4]=p;
        cnt['F'-65]-=p;
        cnt['O'-65]-=p;
        cnt['U'-65]-=p;
        cnt['R'-65]-=p;


        x='F'-65;
        p=cnt[x];
        ans[5]=p;
        cnt['F'-65]-=p;
        cnt['I'-65]-=p;
        cnt['V'-65]-=p;
        cnt['E'-65]-=p;


        x='V'-65;
        p=cnt[x];
        ans[7]=p;
        cnt['S'-65]-=p;
        cnt['E'-65]-=(2*p);
        cnt['V'-65]-=p;
        cnt['N'-65]-=p;

        x='X'-65;
        p=cnt[x];
        ans[6]=p;
        cnt['S'-65]-=p;
        cnt['I'-65]-=p;
        cnt['X'-65]-=p;


        x='O'-65;
        p=cnt[x];
        ans[1]=p;
        cnt['O'-65]-=p;
        cnt['N'-65]-=p;
        cnt['E'-65]-=p;


        x='R'-65;
        p=cnt[x];
        ans[3]=p;
        cnt['T'-65]-=p;
        cnt['H'-65]-=p;
        cnt['R'-65]-=p;
        cnt['E'-65]-=(2*p);

        x='H'-65;
        p=cnt[x];
        ans[8]=p;
        cnt['E'-65]-=p;
        cnt['I'-65]-=p;
        cnt['G'-65]-=p;
        cnt['H'-65]-=p;
        cnt['T'-65]-=p;

        x='E'-65;
        p=cnt[x];
        ans[9]=p;
        cnt['N'-65]-=p;
        cnt['I'-65]-=p;
        cnt['N'-65]-=p;
        cnt['E'-65]-=p;

        printf("Case #%d: ",cs++);

        for(int i=0;i<10;i++)
        {
            for(int j=0;j<ans[i];j++)
            {
                printf("%d",i);
            }
        }

        printf("\n");

    }


}
