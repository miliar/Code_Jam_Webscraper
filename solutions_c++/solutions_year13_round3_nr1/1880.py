#include<iostream>
#include<map>
#include<vector>
#include<set>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define mod 1000000007
#define pinf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a);
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define ps(a) printf("%s",a);
#define nline printf("\n")
#define pc(a) printf("%c",a)
#define ll long long
#define MAX(a,b,c) ((a>b)?(a>c?a:c):(b>c?b:c))
#define MIN(a,b,c) ((a<b)?(a<c?a:c):(b<c?b:c))
int conso(char ch)
{
    if(ch!='a'&&ch!='e'&&ch!='o'&&ch!='u'&&ch!='i')
        return 1;
    else
    return 0;
}

int main()
{
int t,p,n;
int i,j,x,l,count=0,pos1,pos2,count2=0;
char s[101];
FILE * fp,*fw;
fp=fopen("A-small-attempt0 .in","r");
fw=fopen("output1.txt","w");
fscanf(fp,"%d",&t);
for(p=1;p<=t;p++)
    {
    count=0;
    fscanf(fp,"%s %d",s,&n);
    l=strlen(s);

    for(j=n;j<=l;j++)
        {
        for(i=0;i<=l-j;i++)
            {
                count2=0;
                for(x=i;x<l&&x<i+j;x++)
                    {
                        if(!conso(s[x]))
                        count2=0;
                    else
                        count2++;
                    if(count2>=n)
                        {
                            count++;
                        break;}

                        }

                }
            }
    fprintf(fw,"Case #%d: %d\n",p,count);
    }

return 0;
}
