#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int MAXN = 100 + 5;
char buf[MAXN];

inline int trans(char c){
    return c == '+' ? 1 : 0;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int Cas = 1;Cas <= T;++ Cas){
        printf("Case #%d: ",Cas);
        scanf("%s",buf);
        int n = strlen(buf),status = 1,ans = 0;
        for(int j,i = n - 1;i >= 0;i = j){
            j = i - 1;
            while(j >= 0 && buf[j] == buf[i]) -- j;
            if(trans(buf[i]) != status){
                ++ ans;
                status ^= 1;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
