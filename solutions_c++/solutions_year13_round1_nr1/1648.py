#include <stdio.h>

using namespace std;

int main(){
    freopen("caso.in","r",stdin);
    freopen("chosto.txt","w",stdout);
    long long int t,r,n,answer;
    scanf("%lld",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        scanf("%lld%lld",&r,&t);
        answer=0;
        long long int suma=1;
        while(t>0){
            if(t-(r*2+suma)>=0)
                answer++;
            t-=(r*2+suma);
            suma+=4;
        }
        printf("%lld\n",answer);
    }
    return 0;
}
