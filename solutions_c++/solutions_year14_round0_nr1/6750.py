
#include <iostream>
#include <stdint.h>
void load_mat(int32_t mat[4][4]) {
    for(int32_t r = 0; r < 4; r++)
    {
        for(int32_t c = 0; c < 4; c++)
        {
            std::cin >> mat[r][c];
        }
    }
}
void print_mat(int32_t mat[4][4]) {
    for(int32_t i = 0; i < 4; i++)
    {
        for(int32_t j = 0; j < 4; j++)
        {
            std::cout << mat[i][j] << " ";
        }
        std::cout << std::endl;
    }
}
void proc_rows(int32_t f[4], int32_t s[4], int32_t round_num) {
    int32_t res [16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int32_t one = 0;
    int32_t oneI = 0;

    for(int32_t i = 0; i < 4; i++)
    {
        res[f[i] - 1]++;
        res[s[i] - 1]++;
    }
    for(int32_t i = 0; i < 16; i++)
    {
        if(res[i] == 2)
        {
            oneI = i;
            one++;
        }
    }
    if(one == 1)
    {
        std::cout << "Case #" << round_num << ": " << (oneI + 1) << 
std::endl;
    }
    else
    {
        if(one > 1)
        {
           std::cout << "Case #" << round_num << ": Bad magician!" << 
std::endl;
        }
        else
        {
            std::cout << "Case #" << round_num << ": Volunteer cheated!" 
<< std::endl;
        }
    }
}
void round(int32_t round_num) {
    int32_t c_f, c_s;
    int32_t mat_f[4][4];
    int32_t mat_s[4][4];
    std::cin >> c_f;
    load_mat(mat_f);
    std::cin >> c_s;
    load_mat(mat_s);
    proc_rows(mat_f[c_f - 1], mat_s[c_s - 1], round_num);
}
int main() {
    int32_t rn = 1;
    std::cin >> rn;
    for(int32_t r = 1; r <= rn; r++)
    {
        round(r);
    }
    return 0;
}
