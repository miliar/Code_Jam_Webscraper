#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main(){
    int T;
    char str[1001];
    string res;

    scanf("%d\n", &T);
    for(int caso=1;caso<=T;caso++){
        scanf("%s", str);

        res = str[0];
        for(int i=1;i<strlen(str);i++){
            if( str[i] >= res[0] )
                res = str[i] + res;
            else
                res = res + str[i];
        }

        printf("Case #%d: %s", caso, res.c_str());
        if( caso < T )
            printf("\n");
    }

    return 0;
}