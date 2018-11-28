#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int T;
    char s[110];
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d\n",&T);
    for(int i=1;i<=T;++i) {
        int result = 0;
        printf("Case #%d: ",i);
        gets(s);
        for(int j=0;j<strlen(s)-1;++j) {
            if(s[j]==s[j+1]) continue;
            else ++result;
        }
        if(s[strlen(s)-1]=='-')
            ++result;
        printf("%d\n",result);
    }
    return 0;
}
