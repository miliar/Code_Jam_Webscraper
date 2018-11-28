//Standing ovation
#include <cstdio>

//char A[1003];

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,sum,maxi,res;
    char k;
    scanf("%d\n",&T);
    for(int caso=1;caso<=T;caso++) {
        sum=res=0;
        scanf("%d",&maxi);
        for(int i=0;i<=maxi;i++) {
            scanf(" %c",&k);
            if(i>sum) {
                res+=i-sum;
                sum=i;
            }
            sum+=k-'0';//puede ir arriba del if
        }
        printf("Case #%d: %d\n",caso,res);
    }



return 0;
}
