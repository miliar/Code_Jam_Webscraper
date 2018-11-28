#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
int A[110];
int B[220];
struct node
{
    int ch[210];int n;
}K[100010];
int thesame=0;
bool cmp(node a,node b)
{
    if(a.n==b.n)
    {
        int i;
        for(i=a.n;i>=1;i--)
        {
            if(a.ch[i]!=b.ch[i]) break;
        }
        /*if(i==0)
        {
            for(int j=1;j<=a.n;j++) printf("%d",a.ch[j]);printf("\n");
            thesame=1;
        }*/
        return a.ch[i]<b.ch[i];
    }
    return a.n<b.n;
}
int o;
void dfs(int k,int sum,int n)
{
    int i,j;//cout<<k<<"  "<<n<<endl;
    if((((n&1)==0)&&k>=n/2+1)||((n&1)&&k==n/2+2))
    {
        for(i=1;i<=n/2;i++) A[n+1-i]=A[i];
        //for(i=1;i<=n;i++) printf("%d",A[i]);printf("\n");
        for(i=1;i<2*n;i++) B[i]=0;
        for(i=1;i<=n;i++)
        {
            if(A[i])
            {
                for(j=1;j<=n;j++)
                {
                    if(A[j])
                    {
                        B[i+j-1]+=A[i]*A[j];
                    }
                }
            }
        }
        for(i=1;i<=(2*n-1)/2;i++) if(B[i]!=B[2*n-i]) return ;
        for(i=1;i<2*n;i++) if(B[i]>=10) return ;
        //for(i=1;i<2*n;i++)printf("%d",B[i]);printf("\n");
        for(i=1;i<2*n;i++)
        {
            K[o].ch[i]=B[i];K[o].n=2*n-1;
        }
        o++;
        return ;
    }

    if((n&1)&&k==n/2+1)
    {//cout<<"WWW"<<endl;
        if(sum>=4)
        {
            A[k]=2;
            dfs(k+1,sum-4,n);
            A[k]=0;
        }
        if(sum>=1)
        {
            A[k]=1;
            dfs(k+1,sum-1,n);
            A[k]=0;
        }
        dfs(k+1,sum,n);
        return ;
    }

    for(i=k;i<=n/2;i++)
    {
        if(sum>=8)
        {
            A[i]=2;
            dfs(i+1,sum-8,n);
            A[i]=0;
        }
        if(sum>=2)
        {
            A[i]=1;
            dfs(i+1,sum-2,n);
            A[i]=0;
        }
    }
    dfs(i,sum,n);
}
char ch1[1010],ch2[1010];
int n1,n2;
int dfsa(int l,int r)
{
    if(l==r) return l;
    int mid=(l+r)/2;int s;
    if(K[mid].n<n1) s=-1;
    else if(K[mid].n>n1) s=1;
    else
    {
        int i;
        for(i=n1;i>=1;i--) if(K[mid].ch[i]!=A[i]) break;
        if(i==0) s=0;
        else if(K[mid].ch[i]<A[i]) s=-1;
        else s=1;
    }
    if(s>=0) return dfsa(l,mid);
    else return dfsa(mid+1,r);
}

int dfsb(int l,int r)
{//cout<<l<<"  "<<r<<endl;
    if(l==r) return l;
    int mid=(l+r)/2+1;int s;

    if(K[mid].n<n2) s=-1;
    else if(K[mid].n>n2) s=1;
    else
    {
        int i;
        for(i=n2;i>=1;i--) if(K[mid].ch[i]!=B[i]) break;
        if(i==0) s=0;
        else if(K[mid].ch[i]<B[i]) s=-1;
        else s=1;
    }
    if(s>0) return dfsb(l,mid-1);
    else return dfsb(mid,r);
}
int main()
{
    o=0;
    freopen("ac.in","r",stdin);
    freopen("miao.out","w",stdout);
    int i,j,k;
    int a,b,s;
    K[o].n=1;K[o].ch[1]=1;o++;
    K[o].n=1;K[o].ch[1]=4;o++;
    K[o].n=1;K[o].ch[1]=9;o++;
    for(int n=2;n<=60;n++)
    {//cout<<n<<endl;
        A[1]=1;
        dfs(2,7,n);
        A[1]=2;
        dfs(2,1,n);
    }
    //cout<<o<<endl;
    thesame=false;
    sort(K,K+o,cmp);
    //cout<<thesame<<endl;
/*
    for(i=1;i<o;i++)
    {
        for(j=1;j<=K[i].n;j++) printf("%d",K[i].ch[j]);printf("\n");
        for(j=K[i].n;j>=1;j--)
        {
            if(K[i].ch[j]!=K[i-1].ch[j]) break;
        }
        if(j==0)
        {
            for(j=1;j<=K[i].n;j++) printf("%d",K[i].ch[j]);
            printf("\n");
        }
    }
*/
    int T;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        tt++;
        scanf("%s%s",ch1,ch2);
        n1=strlen(ch1);n2=strlen(ch2);
        for(i=1;i<=n1;i++) A[i]=ch1[n1-i]-'0';
        for(i=1;i<=n2;i++) B[i]=ch2[n2-i]-'0';
        b=dfsb(0,o-1);a=dfsa(0,o-1);
        //cout<<a<<"  "<<b<<endl;
        printf("Case #%d: %d\n",tt,b-a+1);
    }
    return 0;
}
