#include<stdio.h>
int N,ans;
char s[150][150];
char ch[150];
int m[150][150];
int getans()
{
    ans=0;
    char l=0;
    int all=-1;
    for(int i=0;s[0][i];i++)
    {
        if(s[0][i]!=l)
        {
            all++;
            ch[all]=s[0][i];
            m[0][all]=1;
            l=s[0][i];
        }
        else m[0][all]++;
    }
    for(int i=1;i<N;i++)
    {
        int k=-1;
        char last=0;
        for(int j=0;s[i][j];j++)
        {
            if(s[i][j]!=last)
            {
                k++;
                if(ch[k]!=s[i][j]) return 0;
                m[i][k]=1;
                last=s[i][j];
            }
            else m[i][k]++;

        }
        if(k!=all) return 0;
    }

    for(int j=0;j<=all;j++)
    {
        int sum=0;
        for(int i=0;i<N;i++)
        {
            sum+=m[i][j];
        }
        int p=sum/N;//printf("p=%d,sum=%d\n",p,sum);
        for(int i=0;i<N;i++)
        {
             if(m[i][j]>p) ans+=m[i][j]-p;
             else ans+=p-m[i][j];
        }

    }
    return 1;
}
int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.txt","w",stdout);
    int T,t=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++) scanf("%s",&s[i]);
        int fl=getans();
        if(fl) printf("Case #%d: %d\n",t++,ans);
        else printf("Case #%d: Fegla Won\n",t++);
    }
    return 0;
}
