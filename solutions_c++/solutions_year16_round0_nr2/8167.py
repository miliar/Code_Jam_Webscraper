#include<cstdio>
#include<cstring>
using namespace std;

char s[110];
void rev(int j,int l)
{
    int i;
    char t;
    for(i=0;i<=(j+l)/2;i++)
    {
        t = s[i];
        s[i] = s[l+j-i];
        s[l+j-i]=t;
    }
}

int check()
{
    int i;
    int l=strlen(s);
    for(i=0;i<l;i++)
    {
        if(s[i] == '-')
            return i;
    }
    return -1;
}

int main ()
{
    freopen("revenge.in","r",stdin);
    freopen("revenge.out","w",stdout);
    int T,i,n;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%s",s);
        printf("Case #%d: ",i);
        int ans=0;
        int l;
        while(1)
        {
            int j=check();
            if(j == -1)
                break;
            if(j != 0)
            {
                int k=j+1;int counts=0;
                while(s[k] == '-')
                {
                    k++;
                    counts++;
                }
                rev(j,counts);
                ans++;
                j=0;
            }
            if(j == 0)
            {
                while(s[j] == '-')
                {
                    s[j] = '+';
                    j++;
                }
                ans++;
            }
        }
        printf("%d\n",ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
