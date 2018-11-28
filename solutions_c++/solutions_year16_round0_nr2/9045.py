#include <cstdio>
#include <cstring>

int main(){
    int Case;
    scanf("%d",&Case);
    for(int c = 1; c <= Case; ++c){
        char in[105];
        scanf("%s",in);
        size_t len = strlen(in);
        int count = 0;
        char cur = '+';

        for(int i = len - 1;i >= 0;--i){
            if(in[i] != cur){
                cur = in[i];
                count++;
            }
        }

        printf("Case #%d: %d\n", c, count);
    }
}
