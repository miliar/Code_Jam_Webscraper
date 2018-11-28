#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

char lib[50][20];
int a[50];
int to[6][90][26],k[6];
int n,m;
void add_trie(char s[],int t)
{
    int index,p=0;
    for(int i=0;s[i];i++)
    {
        index=s[i]-'A';
        if(to[t][p][index]==0)
        {
            to[t][p][index]=k[t]++;
        }
        p=to[t][p][index];
    }
}
int cal()
{
    memset(to,0,sizeof(to));
    for(int i=0;i<m;i++)
        k[i]=1;
    for(int i=0;i<n;i++)
        add_trie(lib[i],a[i]);
    int sum=0;
    bool f=1;
    for(int i=0;i<m;i++)
    {
        if(k[i]==1)f=0;
        sum+=k[i];
    }
    if(f==0)return 0;
    else return sum;
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int t,ti=1;scanf("%d",&t);
	while(t--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%s",lib[i]);
        int ans=0,tot=0;
        int lim;
        if(m==4)
        {
            lim=1<<(2*n);
            for(int i=0;i<lim;i++)
            {
                int c=i;
                for(int k=0;k<n;k++)
                {
                    a[k]=c&3;
                    c>>=2;
                }
                c=cal();
                if(c>tot)tot=c,ans=1;
                else if(c==tot)ans++;
            }
        }
        else if(m==3)
        {
            lim=1;
            for(int i=0;i<n;i++)lim*=3;
            for(int i=0;i<lim;i++)
            {
                int c=i;
                for(int k=0;k<n;k++)
                {
                    a[k]=c%3;
                    c/=3;
                }
                c=cal();
                if(c>tot)tot=c,ans=1;
                else if(c==tot)ans++;
            }
        }
        else if(m==2)
        {
            lim=1<<n;
            for(int i=0;i<lim;i++)
            {
                int c=i;
                for(int k=0;k<n;k++)
                {
                    a[k]=c&1;
                    c>>=1;
                }
                c=cal();
                if(c>tot)
                    tot=c,ans=1;
                else if(c==tot)
                    ans++;
            }
        }
        else
        {
            for(int i=0;i<n;i++)
                a[i]=0;
            tot=cal();
            ans=1;
        }
        printf("Case #%d: %d %d\n",ti++,tot,ans);
    }
	return 0;
}
