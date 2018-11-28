#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 1000

char name[MAXN];

int main() {
    int t;
    scanf("%d",&t);
    for(int k = 1;k <= t;k++) {
        int n;
        scanf(" %s %d",name,&n);
        int pos[MAXN];
        int res = 0;
        int num = 0;
        int aux = 0;
        for(int i = 0;i < strlen(name);i++) {
            if(name[i] == 'a' || name[i] == 'e' || name[i] == 'i' || name[i] == 'o' || name[i] == 'u') {
                aux = 0;
            }
            else {
                aux++;
                if(aux >= n) pos[num++] = i;
            }
        }
        pos[num] = strlen(name);
        for(int i = 0;i < num;i++) {
            res += (pos[i]-n+2)*(pos[i+1]-pos[i]);
        }

        printf("Case #%d: %d\n",k,res);
    }
    return 0;
}
