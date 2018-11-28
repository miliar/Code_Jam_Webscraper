#include<cstdio>
#include<cstring>

bool used[10];

long long solve(long long n);
bool sleep(void);

int main(){
    int T;
    int N;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &N);
        if(N == 0) printf("Case #%d: INSOMNIA\n", ++cnt);
        else{
            printf("Case #%d: %lld\n", ++cnt, solve((long long)N));
        }
    }
    return 0;
}

long long solve(long long n){
    memset(used, false, sizeof(used));
    long long curr = 0;
    while(!sleep()){
        curr += n;
        long long tmp = curr;
        while(tmp > 0){
            used[tmp%10] = true;
            tmp /= 10;
        }
    }
    return curr;
}

bool sleep(void){
    for(int i = 0; i < 10; i++){
        if(used[i] == false) return false;
    }
    return true;
}
