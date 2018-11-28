#include <cstdio>
#include <cstring>
#include <cstdlib>

char pan[105], tmp[105];

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int totalCase, len;
    scanf("%d", &totalCase);
    for(int cases = 1; cases <= totalCase; ++cases){
        scanf("%s", &pan);
        len = strlen(pan);
        int cnt = 0;
        while(1){
            int pos = -1;
            for(int i = len-1; i >= 0; --i){
                if(pan[i] == '-'){
                    pos = i;
                    break;
                }
            }
            if(pos == -1)
                break;
            if(pan[0] == '+'){
                cnt++;
                for(int i = 0; i < len; ++i){
                    if(pan[i] == '-')
                        break;
                    pan[i] = '-';
                }
            }
            for(int i = 0; i <= pos; ++i){
                if(pan[pos-i] == '-')
                    tmp[i] = '+';
                else if(pan[pos-i] == '+')
                    tmp[i] = '-';
            }
            for(int i = 0; i <= pos; ++i)
                pan[i] = tmp[i];
            //printf("%s\n", pan);
            cnt++;
        }
        printf("Case #%d: %d\n", cases, cnt);
    }
    return 0;
}
/*
5
-
-+
+-
+++
--+-
*/
