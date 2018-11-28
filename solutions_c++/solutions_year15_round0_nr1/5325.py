#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int smax;
    char s[1010];
    int T,t,i,j,k,sum=0,ans;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d %s",&smax,s);
        sum=0; ans=0;
        for(i=0;s[i];i++){
            k=s[i]-'0';
            if(k){
                if(ans+sum>=i){
                    ans+=0;
                }else{
                    ans=i-sum;///ans=ans+ i-sum-ans +1
                }
                sum+=k;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
