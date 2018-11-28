#include<cstdio>
#include<cstring>

using namespace std;

char s[105];
char s2[105];

int main() {
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int cs = 1;
    int T;
    scanf("%d",&T);
    while(T--) {
        scanf("%s",s);
        int len = strlen(s);
        int l2 = 0;
        char last = ' ';
        for(int i = 0; i < len; i++) {
            if(s[i] != last) {
                last = s[i];
                s2[l2++] = last;
            }
        }
        if(s2[l2 - 1] == '+') l2--;
        printf("Case #%d: ",cs++);
        printf("%d\n",l2);
    }
    return 0;
}
