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

int t,n,c,p[20005],id=1,num[35],s,m,ok[15];
bool ch;

void fnd(int nw,int l)
{
    if(nw==l)
    {
        for(int b=2;b<=10;b++)
        {
            for(int i=0;i<id;i++)
            {
//                if(b<=3)
//                {
//                    if(p[i]>=(int)pow(b,n-1))
//                    {
//                        s=1;
//                        break;
//                    }
//                }
                s=0;
                m=1;
                for(int j=l;j>=0;j--)
                {
                    s+=num[j]*m;
                    s%=p[i];
                    m*=b;
                    m%=p[i];
                }
                if(s==0)
                {
                    ok[b]=p[i];
                    break;
                }
            }
            if(s!=0)    break;
        }
        if(s==0)
        {
            c++;
            for(int i=0;i<=l;i++)   printf("%d",num[i]);
            for(int i=2;i<=10;i++)  printf(" %d",ok[i]);
            printf("\n");
        }
        return;
    }
    num[nw]=0;
    fnd(nw+1,l);
    if(c==t)    return;
    num[nw]=1;
    fnd(nw+1,l);
}

int main()
{
//    freopen("C-large.in","r",stdin);
//    freopen("C-large.out","w",stdout);

//  pre prime
    p[0]=2;
    for(int i=3;id!=20000;i+=2)
    {
        ch=false;
        for(int j=0;p[j]*p[j]<=i;j++)
        {
            if(i%p[j]==0)
            {
                ch=true;
                break;
            }
        }
        if(ch)  continue;
        p[id]=i;
        id++;
    }
//  end pro prime

    scanf("%d%d%d",&n,&n,&t);
    num[0]=num[n-1]=1;
    printf("Case #1:\n");
    fnd(1,n-1);
//    printf("\n\n%d",c);
    return 0;
}
