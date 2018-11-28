#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int n,j,k;
int a[100];

int isprime(int k)
{
    if(k==1)return 0;
    for(int i=2;i*i<=k;++i)
        if(k%i==0)
            return i;
    return 0;
}
void add()
{
    ++a[1];
    for(int i=1;i<=n-2;++i)
        if(a[i]>=2)
        {
            a[i+1]+=a[i]/2;
            a[i]%=2;
        }
}
long long cal(int k)
{
    long long f=1;
    long long s=0;
    for(int i=0;i<=n-1;++i)
    {
        s+=f*a[i];
        f*=k;
    }
    return s;
}
void search()
{
    int r=1<<(n-2);
    memset(a,0,sizeof(a));
    a[0]=a[n-1]=1;
    int ans[20];
    int s=0;
    k=0;
    while(++s<=r && k<j)
    {
        add();
        int f=1;
        memset(ans,0,sizeof(ans));
        for(int i=2;i<=10;++i)
        {
            int v=cal(i);
            ans[i]=isprime(v);
            if(!ans[i]){
                f=0;
                break;
            }
        }
        if(f){
            ++k;
            for(int i=n-1;i>=0;--i) cout<<a[i];
            for(int i=2;i<=10;++i) cout<<" "<<ans[i];
            cout<<endl;
        }
    }
}
void gen(int l,int s,int m)
{
    if(s==0 && m==0)
    {
        ++k;
        for(int i=n-1;i>=0;--i) cout<<a[i];
        for(int i=3;i<=11;++i) cout<<" "<<i;
        cout<<endl;
        return;
    }
    if(s<1) return;
    for(int i=l;i<=n-2 && k<j;++i)
    {
        a[i]=1;
        gen(i+1,s-1,m+((i&1==1)?-1:1));
        a[i]=0;
    }
}
void generate()
{
    k=0;
    int s=(n&1==1)? 2:0;
    memset(a,sizeof(a),0);
    for(int i=s;i<=n-2 && k<j;i=i+2)
    {
        a[0]=1;a[n-1]=1;
        for(int j=1;j<=n-2;++j) a[j]=0;
        gen(1,i,(n&1==1)?2:0);
    }
}
int main(){
    int T;
    scanf("%d",&T);
    for(int tcases=1;tcases<=T;++tcases){
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",tcases);
        if(n>=11)
            generate();
        else
            search();
    }
    return 0;
}
