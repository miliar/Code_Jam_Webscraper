#include <iostream>
#include <cstdio>
using namespace std;

int T , N;

int main(){
    //freopen("A-large.in","r" , stdin);
    //freopen("A-large.out","w" , stdout);
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> N;
        if(N == 0){
            printf("Case #%d: INSOMNIA\n" , i);
        }else{
            bool cnt[10] = {0} , flag = true;
            int ans = 0;
            do{
                flag = true;
                ans += N;
                int tem = ans;
                while(tem){
                    cnt[tem%10] = true;
                    tem = tem/10;
                }
                for(int j = 0; j < 10; j++){
                    if(!cnt[j]){
                        flag = false;
                        break;
                    }
                }
            }while(!flag);
            printf("Case #%d: %d\n" , i , ans);
        }
    }
    return 0;
}
