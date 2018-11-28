#include<stdio.h>
#include<string.h>

using namespace std;
char s[10010];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,Smax,ca=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&Smax);
        scanf("%s",s);
        int n = 0, ans = 0;
        for(int i=0; i<=Smax; ++i){
            int x = static_cast<int>(s[i]-'0');
            if(n<i){
                ans += (i-n);
                n = i+x;
            }
            else{
                n+=x;
            }
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
