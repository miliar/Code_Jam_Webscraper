#include<cstdio>
int main()
{
    freopen("QA.in","r",stdin);
    freopen("QA.out","w",stdout);
    int T,x,ans;
    bool ch[20],check;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d",&x);
        for(int i=0;i<10;i++)
            ch[i]=false;
        if(x==0) printf("Case #%d: INSOMNIA\n",I);
        else
        {
            check=false;
            ans=0;
            while(!check)
            {
                ans+=x;
                for(int c=ans;c>0;c/=10)
                    ch[c%10]=true;
                check=true;
                for(int i=0;i<10;i++)
                    check=(check&&ch[i]);
            }
            printf("Case #%d: %d\n",I,ans);
        }
    }
}
