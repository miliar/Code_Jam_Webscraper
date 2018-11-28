#include <cstdio>

int main(){
    int t, smax, membersClapping, x = 1, y;
    char str[1003];
    scanf("%d", &t);

    while(t--){
        scanf("%d %s", &smax, str);
        y = 0;
        membersClapping = (str[0]-'0');
        for(int i = 1 ; str[i] != '\0' ; i++){
            if((i > membersClapping) && (str[i] != '0')){
                y += (i-membersClapping);
                membersClapping += (i-membersClapping);
            }
            membersClapping += (str[i]-'0');
        }
        printf("Case #%d: %d\n", x++, y);
    }

    return 0;
}
