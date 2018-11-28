#include <bits/stdc++.h>
using namespace std;
typedef long long int64;
struct Time{
    clock_t c_lock=clock();
    ~Time(){
        fprintf(stderr,"\nrunning time: %lums\n",1000*(clock()-c_lock)/CLOCKS_PER_SEC);
    }
}Time;//return running time.
int cases,len,cnt;
char str[111];
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d",&cases);
    for (int i=1; i<=cases; i++) {
        printf("Case #%d: ",i);
        memset(str, 0, sizeof str);
        cnt=0;
        scanf("%s",str);
        len=(int)strlen(str);
        for (int j=len-1; j>=0; j--) {
            if (str[j]=='-') {
                if (j-1>=0) {
                    if(str[j-1]=='+'){cnt+=2;}
                }
                else{cnt++;}
            }
        }
        printf("%d\n",cnt);
    }
}