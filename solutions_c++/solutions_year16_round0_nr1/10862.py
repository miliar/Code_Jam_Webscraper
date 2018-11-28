#include <cstdio>

void test_case(){
    bool used[10];
    for(int d=0;d<10;d++) used[d]=false;
    int total_seen = 0;
    
    int num;
    scanf("%d",&num);
    
    if(num == 0){
        printf("INSOMNIA\n");
    } else{
        int cur = 0;
        while(total_seen < 10){
            cur += num;
            
            int tmp = cur;
            while(tmp > 0){
                int dig = tmp%10;
                tmp /= 10;
                if(!used[dig]){
                    used[dig] = true;
                    ++total_seen;
                }
            }
        }
        printf("%d\n", cur);
    }
}

int main(){
    int test_num;
    scanf("%d",&test_num);
    for(int test=1;test<=test_num;++test){
        printf("Case #%d: ",test);
        test_case();
    }
    return 0;
}
