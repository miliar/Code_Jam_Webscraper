#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAX = 100 + 10;
char arr[MAX];

int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen=1;casen<=TN;casen++){
        scanf("%s", arr);
        printf("Case #%d: ", casen);
        int len = strlen(arr), ans = 0;
        for(int i = 1 ; i < len ; i++){
            if(arr[i] != arr[i-1]) ans++;
        }
        if(arr[len-1] == '-') ans++;
        printf("%d\n", ans);
    }
    return 0;
}
