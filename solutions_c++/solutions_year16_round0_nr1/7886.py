#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool digits[10];
bool allDigitsSeen(void){
    for(int i = 0;i < 10;i++)
        if(!digits[i])
            return false;
    return true;
}
int main()
{
    int t;
    scanf("%d", &t);
    for(int cases = 1;cases <= t;cases++){
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", cases);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }
        memset(digits,false,sizeof(digits));
        int i = 1, num;
        do{
            num = n * i;
            i++;
            while(num){
                digits[num % 10] = true;
                num /= 10;
            }
        }while(!allDigitsSeen());
        printf("%d\n", n * (i-1));
    }
    return 0;
}
