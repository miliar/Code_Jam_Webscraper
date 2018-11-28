#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

string winner(char board[16], int start, int step)
{
    int check = 0;
    for (size_t i = 0; i < 4; ++i)
    {
        if(board[start+step*i] == 'O') check += 7;
        else if(board[start+step*i] == 'X') check += 5;
        else if(board[start+step*i] == '.') return "line incomplete";
    }
    if(check%7 == 0) return "O won";
    else if(check%5 == 0) return "X won";
    else return "no winner";
}
              
int main () {
    ofstream answer;
    answer.open ("answer_large.txt");
    
    ifstream input("input_large.txt");
    if (!input)
    {
        cout << "read unsucessful";
        exit(1);
    }
        
    size_t cases;
    input >> cases;
    
    for (size_t t = 0; t < cases; t++)
    {
        //make board
        char board[16];
        for (size_t i = 0; i < 16; ++i)
        {
            input >> board[i];
        }
        
        //check win
        vector<string> wincombo;
        wincombo.push_back(winner(board, 0, 1));
        wincombo.push_back(winner(board, 4, 1));
        wincombo.push_back(winner(board, 8, 1));
        wincombo.push_back(winner(board, 12, 1));
        wincombo.push_back(winner(board, 0, 4));
        wincombo.push_back(winner(board, 1, 4));
        wincombo.push_back(winner(board, 2, 4));
        wincombo.push_back(winner(board, 3, 4));
        wincombo.push_back(winner(board, 0, 5));
        wincombo.push_back(winner(board, 3, 3));
                
        bool flagWin = false, flagIncomplete = false;
        for(size_t i = 0; i < wincombo.size(); ++i)
        {
            if(wincombo[i] == "O won")
            {
                answer << "Case #" << t+1 << ": " << "O won" << endl;
                flagWin = true;
                break;
            }
            else if (wincombo[i] == "X won")
            {
                answer << "Case #" << t+1 << ": " << "X won" << endl;
                flagWin = true;
                break;
            }
        }
        if (flagWin == false)
        {
            for(size_t i = 0; i < wincombo.size(); ++i)
            {
                if(wincombo[i] == "line incomplete")
                {
                    answer << "Case #" << t+1 << ": " << "Game has not completed" << endl;
                    flagIncomplete = true;
                    break;
                }
            }
            if (flagIncomplete == false) answer << "Case #" << t+1 << ": " << "Draw" << endl;
        }
    }
}
