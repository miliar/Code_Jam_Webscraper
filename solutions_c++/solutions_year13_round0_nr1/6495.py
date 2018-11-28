#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string func(char x[4][4])
{
    int score_x = 0;
    int score_o = 0;
    char current;
    bool dot = false;
    string o_won = "O won";
    string x_won = "X won";
    string draw = "Draw";
    string nc = "Game has not completed";
    for(int i=0;i<4;i++)
    {
        score_o = 0;
        score_x = 0;
        for(int j=0;j<4;j++)
        {
            current = x[i][j];
            if(current == 'T'){score_x++;score_o++;}
            else if(current == 'X')
                score_x++;
            else if(current == 'O')
                score_o++;
            else if(current == '.')
                dot = true;
        }
        if(score_o > 3)
            return o_won;
        if(score_x > 3)
            return x_won;
    }
    for(int i=0;i<4;i++)
    {
        score_o = 0;
        score_x = 0;
        for(int j=0;j<4;j++)
        {
            current = x[j][i];
            if(current == 'T'){score_x++;score_o++;}
            else if(current == 'X')
                score_x++;
            else if(current == 'O')
                score_o++;
        }
        if(score_o > 3)
            return o_won;
        if(score_x > 3)
            return x_won;
    }
    score_o = 0;
    score_x = 0;
    for(int i=0,j=0;i<4;i++,j++)
    {
        current = x[i][j];
        if(current == 'T'){score_x++;score_o++;}
        else if(current == 'X')
            score_x++;
        else if(current == 'O')
            score_o++;
    }
    if(score_o > 3)
        return o_won;
    if(score_x > 3)
        return x_won;

    score_o = 0;
    score_x = 0;
    if(x[0][3] == 'X') score_x++;
    else if(x[0][3] == 'O') score_o++;
    else if (x[0][3] == 'T') {score_x++; score_o++;}

    if(x[1][2] == 'X') score_x++;
    else if(x[1][2] == 'O') score_o++;
    else if (x[1][2] == 'T') {score_x++; score_o++;}

    if(x[2][1] == 'X') score_x++;
    else if(x[2][1] == 'O') score_o++;
    else if (x[2][1] == 'T') {score_x++; score_o++;}

    if(x[3][0] == 'X') score_x++;
    else if(x[3][0] == 'O') score_o++;
    else if (x[3][0] == 'T') {score_x++; score_o++;}

    if(score_o > 3)
        return o_won;
    if(score_x > 3)
        return x_won;
    if(dot)
        return nc;
    return draw;
}

int main()
{
    char file[8] = "ali.txt";
    char file2[8] = "out.txt";
    char x[4][4],tmp;
    int i,sayi,j,k;
    ifstream in(file);
    ofstream out(file2,ios::out);
    in>>sayi;
    for(k=0;k<sayi;k++)
    {
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                in>>tmp;
                x[i][j]=tmp;
            }
        out<<"Case #"<<k+1<<": "<<func(x)<<"\n";
    }
    return 0;
}
