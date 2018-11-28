#include<cstdio>

using namespace std;

char str[10000];

int main(){
    int tc;
    scanf("%d", &tc);
    for(int T=1;T<=tc;++T){
        int n;
        scanf("%d %s", &n, str);
        int cnt=0, cc = 0, i=0;
        for(char* c=str; *c; ++c, ++i){
            if(cc<i){
                cnt+=i - cc;//(*c=='0');
                cc += (i -cc);
            }
            cc += *c-'0';
        }
        printf("Case #%d: %d\n", T, cnt);
    }
    return 0;
}
