#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

#include "game.h"

using namespace std;

int N = 4;

vector<string> read_board(int n)
{
    vector<string> x;
    
    for (int i=0; i<n; i++)
    {
        string a;
        cin >> a;
        x.push_back(a);
    }
    return x;
}

string left_right_win(vector<string> gameboard)
{
    int x_cnt = 0, o_cnt = 0;
    
    for (int i=0; i<gameboard.size(); i++)
    {
        for (int j=0; j<gameboard[i].size(); j++)
        {
            if(gameboard[i][j] == 'X' || gameboard[i][j] == 'T')
                x_cnt++;
            if (gameboard[i][j] == 'O' || gameboard[i][j] == '.')
                x_cnt = 0;
        }
        if(x_cnt == 4)
            return "X";
    }
    
    for (int i=0; i<gameboard.size(); i++)
    {
        for (int j=0; j<gameboard[i].size(); j++)
        {
            if(gameboard[i][j] == 'O' || gameboard[i][j] == 'T')
                o_cnt++;
            if (gameboard[i][j] == 'X' || gameboard[i][j] == '.')
                o_cnt = 0;
        }
        if(o_cnt == 4)
            return "O";
    }
    return "N";
}

string up_down_win(vector<string> gameboard)
{
    int x_cnt = 0, o_cnt = 0;
    
    for (int i=0; i<gameboard.size(); i++)
    {
        for (int j=0; j<gameboard[i].size(); j++)
        {
            if(gameboard[j][i] == 'X' || gameboard[j][i] == 'T')
                x_cnt++;
            if (gameboard[j][i] == 'O' || gameboard[j][i] == '.')
                x_cnt = 0;
        }
        if(x_cnt == 4)
            return "X";
    }
    
    for (int i=0; i<gameboard.size(); i++)
    {
        for (int j=0; j<gameboard[i].size(); j++)
        {
            if(gameboard[j][i] == 'O' || gameboard[j][i] == 'T')
                o_cnt++;
            if (gameboard[j][i] == 'X' || gameboard[j][i] == '.')
                o_cnt = 0;
        }
        if(o_cnt == 4)
            return "O";
    }
    return "N";
}

string diag0_win(vector<string> gameboard)
{
    int x_cnt = 0, o_cnt = 0;
    
    for (int i=0; i<gameboard.size(); i++)
    {
        if(gameboard[i][i] == 'X' || gameboard[i][i] == 'T')
                x_cnt++;
        if (gameboard[i][i] == 'O' || gameboard[i][i] == '.')
                x_cnt = 0;
        if(x_cnt == 4)
            return "X";
    }
    
    for (int i=0; i<gameboard.size(); i++)
    {
        if(gameboard[i][i] == 'O' || gameboard[i][i] == 'T')
                o_cnt++;
        if (gameboard[i][i] == 'X' || gameboard[i][i] == '.')
                o_cnt = 0;
        if(o_cnt == 4)
            return "O";
    }
    return "N";
}

string diag1_win(vector<string> gameboard)
{
    int x_cnt = 0, o_cnt = 0;
    int j = (int)gameboard.size();
    
    for (int i=0; i<gameboard.size(); i++)
    {
        j--;
        if(gameboard[i][j] == 'X' || gameboard[i][j] == 'T')
            x_cnt++;
        if (gameboard[i][j] == 'O' || gameboard[i][j] == '.')
            x_cnt = 0;
        if(x_cnt == 4)
            return "X";
    }
    
    j = (int)gameboard.size();
    
    for (int i=0; i<gameboard.size(); i++)
    {
        j--;
        if(gameboard[i][j] == 'O' || gameboard[i][j] == 'T')
            o_cnt++;
        if (gameboard[i][j] == 'X' || gameboard[i][j] == '.')
            o_cnt = 0;
        if(o_cnt == 4)
            return "O";
    }
    return "N";
}

string check_draw(vector<string> gameboard)
{
    int c_cnt = 0;
    
    for (int i=0; i<gameboard.size(); i++)
    {
        for (int j=0; j<gameboard[i].size(); j++)
        {
            if(gameboard[i][j] != '.')
                c_cnt++;
        }
    }
    if(c_cnt == 16)
        return "Draw";
    return "N";
}

string check_win(vector<string> gameboard)
{
    string ud = up_down_win(gameboard);
    string lr = left_right_win(gameboard);
    string diag0 = diag0_win(gameboard);
    string diag1 = diag1_win(gameboard);
    string draw = check_draw(gameboard);
    
    if(ud != "N")
        return (ud + " won");
    if(lr != "N")
        return (lr + " won");
    if(diag0 != "N")
        return (diag0 + " won");
    if(diag1 != "N")
        return (diag1 + " won");
    if(draw != "N")
        return draw;
    return "Game has not completed";
}

void run_game(int t_case)
{
    vector<string> gameboard;
    
    gameboard = read_board(N);
    
    cout << "Case #" << t_case << ": " << check_win(gameboard) << endl;
}

int main()
{
    freopen("A-small-attempt.in", "r", stdin);
    freopen("A-small-attempt3.out", "w", stdout);
    int n;
    
    cin >> n;
    
    for (int i=0; i<n; i++)
    {
        run_game(i+1);
    }
}
