#include <cstdlib>
#include <cstdio>

using namespace std;

char s[4][5];

inline bool oc(int i, int j) {
    return (s[i][j] == 'O' || s[i][j] == 'T');
}

inline bool xc(int i, int j) {
    return (s[i][j] == 'X' || s[i][j] == 'T');
}

int main() {
    freopen("A-small-attempt0.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t = 0;
    scanf("%d", &t);
    for(int p = 0; p < t; p++) {
        printf("Case #%d: ", p + 1);

        for(int i = 0; i < 4; i++)  scanf("%s", s[i]);

        int c = 0;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                if(s[i][j] != '.') c++;

        bool flag = false, b;
        for(int i = 0; i < 4; i++) {
            b = true;
            for(int j = 0; j < 4; j++)
                if(!oc(i, j)) b = false;
            if(b) {
                puts("O won");
                flag = true;
                break;
            }
            b = true;
            for(int j = 0; j < 4; j++)
                if(!xc(i, j)) b = false;
            if(b) {
                puts("X won");
                flag = true;
                break;
            }

            b = true;
            for(int j = 0; j < 4; j++)
                if(!oc(j, i)) b = false;
            if(b) {
                puts("O won");
                flag = true;
                break;
            }
            b = true;
            for(int j = 0; j < 4; j++)
                if(!xc(j, i)) b = false;
            if(b) {
                puts("X won");
                flag = true;
                break;
            }
        }

        if(!flag) {
        b = true;
        for(int i = 0; i < 4; i++)
            if(!oc(i, i))   b = false;
        if(b) {
            puts("O won");
            flag = true;
        }
        b = true;
        for(int i = 0; i < 4; i++)
            if(!xc(i, i))   b = false;
        if(b) {
            puts("X won");
            flag = true;
        }

        b = true;
        for(int i = 0; i < 4; i++)
            if(!oc(i, 3 - i))   b = false;
        if(b) {
            puts("O won");
            flag = true;
        }
        b = true;
        for(int i = 0; i < 4; i++)
            if(!xc(i, 3 - i))   b = false;
        if(b) {
            puts("X won");
            flag = true;
        }
        }

        if(!flag) {
            if(c < 16) puts("Game has not completed");
            else    puts("Draw");
        }
    }

    return 0;
}
