#include<cstdio>
#include<cstdlib>
using namespace std;

#define Maxn 11000

char sa[Maxn];
int x,l;
int le[Maxn],ri[Maxn],ori[Maxn];


int cal(int cur)
{
    if(abs(cur)==1)
    {
        if(cur<0)
            return -3;
        else
            return 3;
    }
    if(abs(cur)==3)
    {
        if(cur<0)
            return 1;
        return -1;
    }
    else if(abs(cur)<3)
    {
        if(cur<0)
            return -4;
        return 4;
    }
    else
    {
        if(cur<0)
            return 2;
        return -2;
    }
}
int main()
{
    //printf("%d\n",-2%3);
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);

    int tt;

    scanf("%d",&tt);
    for(int ca=1;ca<=tt;ca++)
    {
        scanf("%d%d",&l,&x);
        scanf("%s",sa);
        for(int i=l;i<x*l;i++)
            sa[i]=sa[i%l];

        for(int i=0;i<x*l;i++)
        {
            ori[i]=sa[i]-'i'+2;
            if(!i)
            {
                le[i]=ori[i];
                continue;
            }
            if(abs(le[i-1])==1)
            {
                if(le[i-1]<0)
                    le[i]=-ori[i];
                else
                    le[i]=ori[i];
                continue;
            }
            if(abs(le[i-1])==ori[i])
            {
                if(le[i-1]<0)
                    le[i]=1;
                else
                    le[i]=-1;
                continue;
            }
            int aa = abs(le[i-1]);
            if((ori[i]-aa==1)||(aa==4&&ori[i]==2))
            {
                int tmp=9-aa-ori[i];
                if(le[i-1]<0)
                    le[i]=-tmp;
                else
                    le[i]=tmp;
            }
            else
            {
                int tmp=9-aa-ori[i];
                if(le[i-1]<0)
                    le[i]=tmp;
                else
                    le[i]=-tmp;
            }
            //printf("i:%d %d\n",i,le[i]);

        }

        for(int i=x*l-1;i>=0;i--)
        {
            if(i==(x*l-1))
            {
                ri[i]=ori[i];
                continue;
            }
            if(abs(ri[i+1])==1)
            {
                if(ri[i+1]<0)
                    ri[i]=-ori[i];
                else
                    ri[i]=ori[i];
                continue;
            }
            if(abs(ri[i+1])==ori[i])
            {
                if(ri[i+1]<0)
                    ri[i]=1;
                else
                    ri[i]=-1;
                continue;
            }
            int aa=abs(ri[i+1]);
            if((aa-ori[i]==1)||(aa==2&&ori[i]==4))
            {
                int tmp=9-aa-ori[i];
                if(ri[i+1]<0)
                    ri[i]=-tmp;
                else
                    ri[i]=tmp;
            }
            else
            {
                int tmp=9-aa-ori[i];
                if(ri[i+1]<0)
                    ri[i]=tmp;
                else
                    ri[i]=-tmp;
            }

            //printf("i:%d ri:%d\n",i,ri[i]);

        }
        //printf("::%d %d\n",le[0],ri[x*l-1]);
        bool flag=false;
        for(int i=0;i<=x*l-3&&!flag;i++)
        {
            if(le[i]!=2)
                continue;
            for(int j=x*l-1;j>=i+2&&!flag;j--)
            {
                if(ri[j]!=4)
                    continue;
                if(cal(le[i])==le[j-1])
                {
                    flag=true;
                    break;
                }
            }
        }
        if(flag)
            printf("Case #%d: YES\n",ca);
        else
            printf("Case #%d: NO\n",ca);


    }

    return 0;
}
