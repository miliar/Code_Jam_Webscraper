#include <iostream>
#include <cstdio>

using namespace std;

int ex(long long num,int marker[])
{
    int ans=0;
    while(num>0){
        marker[int(num%10)]=1;
        num/=10;
    }
    for(int i=0;i<10;i++){
        ans+=marker[i];
    }
    return ans;
}

void solve(int i)
{
    long long n;
    scanf("%lld",&n);
    printf("Case #%d: ",i+1);

    long long tmp=n;
    int j=0,mark[10]={0};

    if(n==0){
        printf("INSOMNIA\n");
        return;
    }

    while(j<65535){
        if(ex(tmp,mark)==10){
            printf("%lld\n",tmp);
            return;
        }

        tmp+=n;
        j++;
    }
    if(j==65535){
        printf("INSOMNIA\n");
    }
}

int main(int argc, char *argv[])
{
    int t;
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt.out","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++)solve(i);
    return 0;
}
