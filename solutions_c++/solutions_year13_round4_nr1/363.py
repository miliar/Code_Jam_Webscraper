#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int N,M,K;
struct node
{
    int s,num,o;
}A[100010];
const long long mod=1000002013;
node st[1000010];
int top;
bool cmp(node a,node b)
{
    if(a.s==b.s) return a.o>b.o;
    return a.s<b.s;
}
int main()
{
    freopen("AA.in","r",stdin);
    freopen("AA.out","w",stdout);
    int i,j,k;
    int a,b,s;
    int T;
    int tt=0;
    scanf("%d",&T);
    while(T--)
    {tt++;
        scanf("%d%d",&N,&M);
        k=0;
        long long sum1=0;
        for(i=0;i<M;i++)
        {
            scanf("%d%d%d",&a,&b,&s);
            long long p=b-a;
            sum1+=(((N*p-p*(p-1)/2)%mod)*s)%mod;sum1%=mod;
            A[k].s=a;A[k].o=1;A[k++].num=s;
            A[k].s=b;A[k].o=0;A[k++].num=s;
        }
        sort(A,A+k,cmp);
        top=-1;
        long long sum=0;
        long long op;
        for(i=0;i<k;i++)
        {
            if(A[i].o)
            {
                st[++top]=A[i];
            }
            else
            {
                s=A[i].num;
                while(top>=0&&s>=st[top].num)
                {
                    //cout<<st[top].s<<endl;
                    op=A[i].s-st[top].s;s-=st[top].num;
                    sum+=((((N*op-op*(op-1)/2))%mod)*st[top].num)%mod;
                    sum%=mod;
                    top--;
                }
                if(s)
                {
                    op=A[i].s-st[top].s;
                    sum+=(((N*op-op*(op-1)/2)%mod)*s)%mod;
                    sum%=mod;
                    st[top].num-=s;
                }
            }
            //cout<<sum<<endl;
        }
        printf("Case #%d: %lld\n",tt,((sum1-sum)%mod+mod)%mod);
    }
    return 0;
}
