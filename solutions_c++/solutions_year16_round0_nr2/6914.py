#include <cstdio>
#include <cstring>
using namespace std;
int T;
char s[105];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int casei = 1; casei <= T; ++casei){
        scanf("%s",s);
        int len = strlen(s);
        int ans = 1;
        for(int i = 1; i < len; ++i){
            if(s[i] != s[i-1])
                ++ans;
        }
        if(s[len-1] == '+')
            --ans;
        printf("Case #%d: %d\n",casei,ans);
    }
    return 0;
}

