#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>

using namespace std;

long long int gcd(long long int a,long long int b)
{
    int c=0;
    c=a%b;
    if(c==0)
        return b;
    return gcd(b,c);
}

bool check1(long long int x){
    int i,a=1;
    for(i=1;i<=40;i++){
        a=a*2;
        if(x==a)return true;
    }
    return false;
}

bool check2(long long int a,long long int b){
    int i;
    for(i=1;i<=40;i++){
        b=b/2;
        while(a-b>0){
            a-=b;
        }
        if(a==0)return true;
    }
    return false;
}

int main()
{
    bool flag;
    long long int a,b,ans,g;
    int i,j,N,t;
    scanf("%d",&N);
    for(t=1;t<=N;t++){
        flag=true;
        ans=0;
        scanf("%lld/%lld",&a,&b);
        g=gcd(a,b);
        a/=g; b/=g;
        if(!check1(b))flag=false;
        for(i=1;i<=40;i++){
            a=a*2;
            if(a>=b){
                ans=i;
                break;
            }
        }
        if(!flag)printf("Case #%d: impossible\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
