#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

bool check[10];

int main() {

    int T;
    int test_case;
    int num,turn,res,add,cnt;
    bool allCheck;
    scanf("%d",&T);

    for(test_case = 1; test_case <= T; test_case++) {
        cnt = 0;
        allCheck = true;
        memset(check,false,sizeof(check));
        scanf("%d",&num);
        if(num==0) {
            printf("Case #%d: INSOMNIA\n",test_case);
            continue;
        }
        add = num;
        turn = 1;
        while(true) {
            res = num;
            while(num>0) {
                if(!check[num%10]) {
                    check[num%10] = true;
                    cnt++;
                }
                num /= 10; 
            }
            if(cnt==10) break; 
            num = add*(turn++);
        }
        printf("Case #%d: %d\n", test_case,res);
    }

    return 0;
}


