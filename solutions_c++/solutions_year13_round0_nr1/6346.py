#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

int winnerPattern[10] = {
    0x0F, 0xF0, 0xF00, 0xF000,
    0x8888, 0x4444, 0x2222, 0x1111,
    0x8421, 0x1248
};

const char* selectWinner(int player1, int player2)
{
    const char *winner = "Game has not completed";
    for (int i = 0; i < 10; ++i)
    {
        if ((player1 & winnerPattern[i]) == winnerPattern[i])
        {
            winner = "X won";
            break;
        } else if ((player2 & winnerPattern[i]) == winnerPattern[i])
        {
            winner = "O won";
            break;
        } else if (i == 9 && (player1 | player2) == 0xFFFF)
        {
            winner = "Draw";
        }
    }
    return winner;
}

int main(int argc, char const *argv[])
{
    int c = 0;
    int player1 = 0;
    int player2 = 0;
    char input = 0;

    cin >> c;
    for (int i = 0; i < c; ++i)
    {
        player1 = player2 = 0;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                cin >> input;
                switch(input) {
                case 'X':
                    player1 |= (1 << j * 4 + k);
                    break;
                case 'O':
                    player2 |= (1 << j * 4 + k);
                    break;
                case 'T':
                    player1 |= (1 << j * 4 + k);
                    player2 |= (1 << j * 4 + k);
                    break;
                default:
                    break;
                }
            }
        }
        cout << "Case #" << (i + 1) << ": " << selectWinner(player1, player2) << endl;
    }
    return 0;
}
