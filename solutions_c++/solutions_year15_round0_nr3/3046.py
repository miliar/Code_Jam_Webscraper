#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;

int T, L, X;

char s[10011], str[10011];
bool did[10011];

pair<char, int> cal[150][150], tmp;

void init() {
    cal['1']['1'] = make_pair('1', 1);
    cal['1']['i'] = make_pair('i', 1);
    cal['1']['j'] = make_pair('j', 1);
    cal['1']['k'] = make_pair('k', 1);
    cal['i']['1'] = make_pair('i', 1);
    cal['j']['1'] = make_pair('j', 1);
    cal['k']['1'] = make_pair('k', 1);

    cal['i']['j'] = make_pair('k', 1);
    cal['j']['k'] = make_pair('i', 1);
    cal['k']['i'] = make_pair('j', 1);
    cal['j']['i'] = make_pair('k', -1);
    cal['k']['j'] = make_pair('i', -1);
    cal['i']['k'] = make_pair('j', -1);
    cal['i']['i'] = make_pair('1', -1);
    cal['j']['j'] = make_pair('1', -1);
    cal['k']['k'] = make_pair('1', -1);
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    init();

    int cas = 1;
    scanf("%d", &T);
    while(T--) {
        memset(did,0,sizeof(did));

        scanf("%d%d", &L, &X);
        scanf("%s", str);
        int len = 0;
        
        for(int i = 1; i <= X; i++) {
            for(int j = 0; j < L; j++) {
                s[len++] = str[j];
            }
        }

        char pre = '1'; int symbol = 1;
        for(int i = len - 1; i >= 0; i--) {
            tmp = cal[s[i]][pre];
            pre = tmp.first;
            symbol *= tmp.second;
            if(symbol == 1 && pre == 'k') did[i] = 1;
        }

        bool find = 0;
        pre = '1'; symbol = 1;
        for(int i = 0; i < len; i++) {
            tmp = cal[pre][s[i]];
            pre = tmp.first;
            symbol *= tmp.second;
            if(symbol == 1 && pre == 'i') {
                char pre2 = '1'; 
                int symbol2 = 1;
                for(int j = i + 1; j < len - 1; j++) {
                    tmp = cal[pre2][s[j]];
                    pre2 = tmp.first;
                    symbol2 *= tmp.second;
                    if(symbol2 == 1 && pre2 == 'j' && did[j + 1]) {
                        find = 1;
                        break;
                    }
                }
            }
            if(find) break;
        }
        if(find) {
            printf("Case #%d: YES\n", cas++);
        } else {
            printf("Case #%d: NO\n", cas++);
        }
    }
    
    return 0;
}