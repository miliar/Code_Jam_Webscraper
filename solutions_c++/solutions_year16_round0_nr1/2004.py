#include <bits/stdc++.h>

using namespace std;

bool Z[15];
int casos, num, hay, en;

int main(){
    scanf("%d", &casos);
    for(int v=1; v<=casos; v++){
        scanf("%d", &num);
        printf("Case #%d: ", v);
        if(num==0){
            printf("INSOMNIA\n");
            continue;
        }
        for(int i=0; i<10; i++)
            Z[i]=true;
        hay=0;
        en = 0;
        while(hay<10){
            en+=num;
            int s=en;
            for(int e=0; e<9; e++){
                if(s>0){
                    int g = s%10;
                    s/=10;
                    hay+=Z[g];
                    Z[g] = false;
                }
            }
        }
        printf("%d\n", en);
    }
    return 0;
}
