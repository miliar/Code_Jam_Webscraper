#pragma warning( disable : 4996 ) 
#include <cstdio>
#include <iostream>

using namespace std;
char maps[55][55];
int yes;
void try_it(int r,int c,int ci,int max_ri,int remain_bomb){
    if (yes)
        return;
    if (ci == c){
        if (remain_bomb != 0)
            return;
        if (r == 1 || c == 1)
            yes = 1;
        for (int ri = 0; ri < r; ri++)
            if (maps[ri][0] == '.'&&maps[ri][1] == '*')
                return;
        for (int ci = 0; ci < c;ci++)
            if (maps[0][ci] == '.'&&maps[1][ci] == '*')
                return;
        yes = 1;
    }
    for (int this_ri = 0; this_ri <= max_ri; this_ri++){
        for (int ri = 0; ri < r; ri++){
            if (ri < this_ri)
                maps[ri][ci] = '.';
            else
                maps[ri][ci] = '*';
        }
        try_it(r, c, ci + 1, this_ri, remain_bomb - this_ri);
        if (yes)
            return;
    }
}

int main(){
    int cc, tt;
    scanf("%d", &tt);
    for (int cc = 1; cc <= tt; cc++){
        int r, c, m;
        int reverse_mode = 0;
        cin >> r >> c >> m;
        printf("Case #%d:\n", cc);
        yes = 0;
        memset(maps, '*', sizeof(maps));
        if (r*c - m == 1)
            yes = 1;
        try_it(r, c, 0, r, r*c-m);
        maps[0][0] = 'c';
        if (yes){
            for (int ri = 0; ri < r; ri++){
                for (int ci = 0; ci < c; ci++)
                    printf("%c", maps[ri][ci]);
                printf("\n");
            }
        }
        else
            printf("Impossible\n");
    }
}