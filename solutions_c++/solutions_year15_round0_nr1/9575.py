#include<cstdio>
#include<cstdlib>

using namespace std;

int main(){
    int T, S;
    char str[1024], str2[1024];
    gets(str);
    sscanf(str, "%d", &T);
    for(int c = 1; c <= T; c++){
        gets(str);
        sscanf(str, "%d %s", &S, str2);
        int G = 0, ans = 0;
        for(int i = 0; i <= S; ++i){
            if((str2[i] - '0') > 0 && i > G) {ans += i - G; G = i; }
            G += str2[i] - '0';
        }
        printf("Case #%d: %d\n", c, ans); 
    }
    return 0;
}
