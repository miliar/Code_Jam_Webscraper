#include <iostream>
#include <cstdio>
#include <cassert>

using namespace std;

int x, o, dot;

void read_board(const char *board)
{
    x = o = dot = 0;
    char c;
    for (int i = 0, mask = 0x1; i < 16; ++i, mask <<= 1)
    {
        c = board[i];
        if (c == 'X')
            x |= mask;
        else if (c == 'O')
            o |= mask;
        else if (c == 'T')
            x |= mask, o |= mask;
        else
            ++dot;
    }
}

bool is_won(int player)
{
    static int pattern[] = {
        0xF, 0xF0, 0xF00, 0xF000,
        0x1111, 0x2222, 0x4444, 0x8888,
        0x8421, 0x1248
    };

    for (int i = 0; i < 10; ++i)
    {
        if ((player & pattern[i]) == pattern[i])
        {
            //printf("0x%X / 0x%X\n", player, pattern[i]);
            return true;
        }
    }
    return false;
}

const char * solve()
{
    if (is_won(x))
        return "X won";
    if (is_won(o))
        return "O won";
    if (dot == 0)
        return "Draw";
    return "Game has not completed";
}

void test()
{
    read_board("XXXT....OO......");
    assert(x == 0x0F);
    assert(o == 0x308);
    assert(dot == 10);
    assert(strcmp(solve(), "X won") == 0);

    read_board("XOXTXXOOOXOXXXOO");
    assert(dot == 0);
    assert(strcmp(solve(), "Draw") == 0);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        char board[17] = { 0 };
        for (int j = 0; j < 4; ++j)
            cin >> board + (j * 4);
        read_board(board);
        printf("Case #%d: %s\n", i + 1, solve());
    }
    return 0;
}

