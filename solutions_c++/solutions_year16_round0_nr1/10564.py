#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

int check;

int updateCheck(int num){
    while(num){
        check = check & (1023-(int)pow(2, num%10));
        num /= 10;
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tCase, num, Bleatrix, cnt = 1;
    scanf("%d", &tCase);
    while(cnt<=tCase){
        check = 1023;
        scanf("%d", &num);
        if(num == 0){
            printf("Case #%d: INSOMNIA\n", cnt++);
            continue;
        }
        for(int i = 1; ; i++){
            Bleatrix = num*i;
            updateCheck(Bleatrix);
            if(check==0){
                printf("Case #%d: %d\n", cnt++, Bleatrix);
                break;
            }
        }
    }

}
