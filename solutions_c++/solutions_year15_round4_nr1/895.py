#include<cstdio>
#include<vector>
using namespace std;

char IN[200][200];
int n, m;

bool arrow(int x, int y) {
    return IN[x][y] == '<' || IN[x][y] == '>' ||IN[x][y] == 'v' ||IN[x][y] == '^';
}

bool unsafe(int x, int y) {
    //printf("unsafecheck %d %d %c\n", x, y, IN[x][y]);
    bool res = true;
    if(IN[x][y] == '<') {
        for(int k = y - 1; k >=0; k--)
            if(arrow(x ,k)) res = false;
    } else if (IN[x][y] == '>') {
        for(int k = y+1; k < m; ++k)
            if(arrow(x, k)) res = false;
    } else if (IN[x][y] == 'v') {
      //  printf("3rd if\n");
        for(int c = x+1; c < n; ++c)
            if(arrow(c, y)) res = false;
       // printf("gone\n");
    } else {
        for(int c = x-1; c >= 0; c--)
            if(arrow(c, y)) res = false;
    }
    return res;
}

bool tryrot(int x, int y) {
 //   printf("tryrot %d %d\n", x, y);
    IN[x][y] = '<';
    if(!unsafe(x, y)) return true;
    IN[x][y] = '>';
    if(!unsafe(x, y)) return true;
    IN[x][y] = 'v';
    if(!unsafe(x, y)) return true;
    IN[x][y] = '^';
    if(!unsafe(x, y)) return true;
    return false;
}

int main() {
    int Z;
    scanf("%d", &Z);
    for(int zz = 1; zz <= Z; ++zz) {
        int result = 0;
        bool fail = false;
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; ++i)
            scanf("%s", IN[i]);
 //       printf("loaded\n");
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
   //             printf("%d %d\n", i, j);
                if(arrow(i, j)) {
     //               printf("isarrow\n");
                    if(unsafe(i, j)) {
       //                 printf("isunsafe\n");
                        if(!tryrot(i, j)) {
         //                   printf("fail\n");
                            fail = true;
                            break;
                        } else {
           //                 printf("succ\n");
                            result++;
                        }
                    }
                }
            }
        }
        //printf("went through\n");
        if(!fail)
            printf("Case #%d: %d\n", zz, result);
        else
            printf("Case #%d: IMPOSSIBLE\n", zz);
    }
    return 0;
}
