#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>


int main()
{
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/ominous_omino/D-small-attempt0.in","r",stdin);
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/ominous_omino/D-small-attempt0.out","w",stdout);
    int cases;
    scanf("%d", &cases);
    int ominoes, rows, cols;
    for(int case_num = 1; case_num <= cases; case_num ++)
    {
        scanf("%d%d%d", &ominoes, &rows, &cols);
        if(rows * cols % ominoes != 0)
        {
            printf("Case #%d: RICHARD\n", case_num);
            continue;
        }
        if(ominoes == 1 || ominoes == 2)
        {
            printf("Case #%d: GABRIEL\n", case_num);
            continue;
        }
        if(ominoes == 3 && (rows == 1 || cols == 1))
        {
            printf("Case #%d: RICHARD\n", case_num);
            continue;
        }
        if(ominoes == 4 && (rows <= 2 || cols <= 2))
        {
            printf("Case #%d: RICHARD\n", case_num);
            continue;
        }
        printf("Case #%d: GABRIEL\n", case_num);
    }
    return 0;
}

