#include<cstdio>
#include<cstring>
using namespace std;
char a[150][40],b[150][40],c[150][40];
int cnt,n,l,val,pos,x,mark[150];


int main()
{
    int t,i,flag,j,k,temp,temp2;
freopen("out.txt","w",stdout);
freopen("inp.txt","r",stdin);
    scanf("%d",&t);
    while(t--)
    {
        x++;
        flag=0;
        val=0;
        scanf("%d %d",&n,&l);
        for(i=0; i<n; i++)
        {
            scanf("%s",a[i]);
        }
        for(i=0; i<n; i++)
        {
            scanf("%s",b[i]);
        }

        for(i=0; i<(1<<l); i++)
        {
            cnt=0;
            for(j=0; j<n; j++)
            {
                strcpy(c[j],a[j]);
                mark[j]=0;
            }
            temp=i;
            temp2=l-1;
            while(temp)
            {
                if(temp&1)
                {
                    for(j=0; j<n; j++)
                        c[j][temp2]=(c[j][temp2]=='1')?'0':'1';
                }
                temp>>=1;
                temp2--;
            }
            for(j=0; j<n; j++)
            {
                for(k=0; k<n; k++)
                {
                    if(mark[k]==0 && strcmpi(c[j],b[k])==0)
                    {
                        cnt++;
                        mark[k]=1;
                        break;
                    }
                }

            }
            if(cnt==n)
            {
                flag=1;
                pos=i;
                break;

            }
        }
        if(i==1<<l)
        {
            printf("Case #%d: NOT POSSIBLE\n",x);
        }
        if(flag)
        {
            while(pos)
            {
                if(pos&1)
                val++;

                pos>>=1;

            }
            printf("Case #%d: %d\n",x,val);
        }
    }

    return 0;
}
