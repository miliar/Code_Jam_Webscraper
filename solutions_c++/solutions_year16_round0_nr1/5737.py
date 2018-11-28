#include <cstdio>
#include <cstring>

bool f[10];
char fc;
int t, n;

int main(){
    scanf("%d", &t);
    
    for(int cs=1; cs<=t; cs++){
        scanf("%d", &n);
        if(n == 0){
            printf("Case #%d: INSOMNIA\n", cs);
            continue;
        }
        
        memset(f, false, sizeof(f));
        fc=0;
        
        long long k=0;
        while(fc!=10){
            k++;
            long long t=n*k;
            while(t){
                if(!f[t%10]){
                    f[t%10]=true;
                    fc++;
                }
                t/=10;
            }
        }
        
        printf("Case #%d: %lld\n", cs, k*n);
    }
    
    return 0;
}