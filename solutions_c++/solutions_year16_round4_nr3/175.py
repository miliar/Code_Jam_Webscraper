#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

int r, c;
char maze[110][110];

struct human{
    int x, y, id;
    };

human h[500];

struct direction{
    int dx, dy;
    };
direction dir[4] = {
    {  0,  1 }, // v
    {  1,  0 }, // >
    {  0, -1 }, // ^
    { -1,  0 }  // <
    };

int solve(int hi){
    if (hi >= (r+c) * 2)
        return -1000000;
    int li = hi + 1;
    while(li >= 0 && h[hi].id != h[li].id){
        li = solve(li);
        }
    if (li < 0)
        return -1000000;
    int x, y, diri;
    x = h[hi].x;
    y = h[hi].y;
    if (y == -1)
        diri = 0;
    if (x == -1)
        diri = 1;
    if (y == r)
        diri = 2;
    if (x == c)
        diri = 3;
    x += dir[diri].dx;
    y += dir[diri].dy;
    while(x != -1 && x != c && y != -1 && y != r) {
        int dirj;
        char p = maze[x][y];
        if (p){
            if (p == '\\')
                dirj = diri ^ 1;
            else
                dirj = diri ^ 3;
            }
        else{
            dirj = (diri+1)%4;
            if ((diri ^ dirj) == 3)
                p = '/';
            else
                p = '\\';
            }
        maze[x][y] = p;
        diri = dirj;
        x += dir[diri].dx;
        y += dir[diri].dy;
        }
    if (x == h[li].x && y == h[li].y)
        return li + 1;
    else
        return -1000000;
    }

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> r >> c;
        memset(maze, 0, sizeof maze);
        int i = 0, j = 0, k = 0;
        for (j = 0; j < c; j++, k++){
            h[k].x = j;
            h[k].y = -1;
            }
        for (i = 0; i < r; i++, k++){
            h[k].x = c;
            h[k].y = i;
            }
        for (j = c-1; j >= 0 ; j--, k++){
            h[k].x = j;
            h[k].y = r;
            }
        for (i = r-1; i >= 0; i--, k++){
            h[k].x = -1;
            h[k].y = i;
            }
        for (i = 0; i < (r+c) * 2 ;i++){
            std::cin >> k;
            --k;
            h[k].id = i/2;
            }
        std::cout << "Case #" << tn << ":" << std::endl;
        int li = 0;
        while(li >= 0 && li < (r+c) * 2){
            li = solve(li);
            }
        if (li < 0)
            std::cout << "IMPOSSIBLE" << std::endl;
        else {
            for (i = 0; i < r; i++){
                for(j = 0; j < c; j++)
                    std::cout << (maze[j][i] ? maze[j][i] : '/');
                std::cout << std::endl;
                }
            }
        }
    return 0;
}
