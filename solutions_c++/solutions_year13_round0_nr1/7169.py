#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdio>
#include <sstream>

using namespace std;

char horizontal_check(vector<vector<char> > b, int line);
char vertical_check(vector<vector<char> > b, int column);
char first_diagonal_check(vector<vector<char> > b);
char second_diagonal_check(vector<vector<char> > b);

int main()
{
    //variables
    ifstream file;
    file.open("A-large.in");
    string line;
    getline(file, line);
    int T = atoi(line.c_str());
    cout<<"T: "<<T<<endl;
    ofstream file_out;
    file_out.open("A-large.out");
    string result;
    
    //board variable
    vector< vector<char> > board(4, vector<char> (4));
    
    //get the data case by case
    for(int n = 1; n <= T; n++)
    {
        //loading the game board
        for(int i = 0; i < 4; i++)
        {
            getline(file, line);
            for(int tt = 0; tt < 4; tt++)
            {
                board[i][tt] = line[tt];
                cout<<board[i][tt];
            }
            cout<<endl;
        }
        
        //start analysis the data on the board
        for(int k = 0; k < 4; k++)
        {
            for(int l = 0; l < 4; l++)
            {
                //check first line to detect any vertical or diognal matching
                if(k == 0)
                {
                    //check the diagonal matching (only on the first column first line)
                    //check first column
                    if(l == 0)
                    {
                        if(first_diagonal_check(board) == 'X')
                        {
                            result = "X won";
                            break;
                            break;
                        }
                        if(first_diagonal_check(board) == 'O')
                        {
                            result = "O won";
                            break;
                            break;
                        }
                    }
                    
                    if(l == 3)
                    {
                        if(second_diagonal_check(board) == 'X')
                        {
                            result = "X won";
                            break;
                            break;
                        }
                        if(second_diagonal_check(board) == 'O')
                        {
                            result = "O won";
                            break;
                            break;
                        }
                    }
                    
                    //vertical check
                    if(vertical_check(board, l) == 'X')
                    {
                        result = "X won";
                        break;
                        break;
                    }
                    if(vertical_check(board, l) == 'O')
                    {
                        result = "O won";
                        break;
                        break;
                    }
                }
                //horizental check
                if(horizontal_check(board, k) == 'O')
                {
                    result = "O won";
                    break;
                    break;
                }
                if(horizontal_check(board, k) == 'X')
                {
                    result = "X won";
                    cout<<"CHECKED"<<endl;
                    break;
                    break;
                }
            }

            if(result == "X won" || result == "O won")
                break;
            
            result = "Draw";
            
            for(int m = 0; m < 4;m++)
            {
                for(int t = 0; t < 4; t++)
                {
                    if(board[m][t] == '.')
                        result = "Game has not completed";
                }
            }
        }
        
        getline(file, line);
        cout<<"Case #"<<n<<": "<<result<<endl;
        file_out<<"Case #"<<n<<": "<<result<<endl;
        result = "";
    }
    
    file.close();
    file_out.close();
	
	return 0;
}

char horizontal_check(vector<vector<char> > b, int line)
{
    if(b[line][0] == 'X')
    {
        for(int i = 1; i < 4; i++)
        {
            if(b[line][i] == 'O' || b[line][i] == '.')
                return 'D';
        }
        return 'X';
    }
    if(b[line][0] == 'O')
    {
        for (int i = 1; i < 4; i++)
        {
            if(b[line][i] == 'X' || b[line][i] == '.')
                return 'D';
        }
        return 'O';
    }
    if(b[line][0] == 'T')
    {
        if(b[line][1] == 'X')
        {
            for(int i = 2; i < 4; i++)
            {
                if(b[line][i] == 'O'  || b[line][i] == '.')
                    return 'D';
            }
            return 'X';
        }
        
        if(b[line][1] == 'O')
        {
            for (int i = 2; i < 4; i++)
            {
                if(b[line][i] == 'X' || b[line][i] == '.')
                    return 'D';
            }
            return 'O';
        }
        
        if(b[line][1] == '.')
            return 'D';

    }
    if(b[line][0] == '.')
    {
        return 'D';
    }
    
}

char vertical_check(vector<vector<char> > b, int column)
{
    if(b[0][column] == 'X')
    {
        for(int i = 1; i < 4; i++)
        {
            if(b[i][column] == 'O' || b[i][column] == '.')
                return 'D';
        }
        return 'X';
    }
    if(b[0][column] == 'O')
    {
        for (int i = 1; i < 4; i++)
        {
            if(b[i][column] == 'X' || b[i][column] == '.')
                return 'D';
        }
        return 'O';
    }
    if(b[0][column] == 'T')
    {
        if(b[1][column] == 'X')
        {
            for(int i = 2; i < 4; i++)
            {
                if(b[i][column] == 'O'  || b[i][column] == '.')
                    return 'D';
            }
            return 'X';
        }
        
        if(b[1][column] == 'O')
        {
            for (int i = 2; i < 4; i++)
            {
                if(b[i][column] == 'X' || b[i][column] == '.')
                    return 'D';
            }
            return 'O';
        }
        
        if(b[1][column] == '.')
            return 'D';
        
    }
    if(b[0][column] == '.')
    {
        return 'D';
    }
    

}

char first_diagonal_check(vector<vector<char> > b)
{
    if(b[0][0] == 'X')
    {
        for(int i = 1; i < 4; i++)
        {
            if(b[i][i] == 'O' || b[i][i] == '.')
                return 'D';
        }
        return 'X';
    }
    if(b[0][0] == 'O')
    {
        for (int i = 1; i < 4; i++)
        {
            if(b[i][i] == 'X' || b[i][i] == '.')
                return 'D';
        }
        return 'O';
    }
    if(b[0][0] == 'T')
    {
        if(b[1][1] == 'X')
        {
            for(int i = 2; i < 4; i++)
            {
                if(b[i][i] == 'O'  || b[i][i] == '.')
                    return 'D';
            }
            return 'X';
        }
        
        if(b[1][1] == 'O')
        {
            for (int i = 2; i < 4; i++)
            {
                if(b[i][i] == 'X' || b[i][i] == '.')
                    return 'D';
            }
            return 'O';
        }
        
        if(b[1][1] == '.')
            return 'D';
        
    }
    if(b[0][0] == '.')
    {
        return 'D';
    }
}

char second_diagonal_check(vector<vector<char> > b)
{
    if(b[0][3] == 'X')
    {
        for(int i = 1; i < 4; i++)
        {
            if(b[i][3 - i] == 'O' || b[i][3 - i] == '.')
                return 'D';
        }
        return 'X';
    }
    if(b[0][3] == 'O')
    {
        for (int i = 1; i < 4; i++)
        {
            if(b[i][3 - i] == 'X' || b[i][3 - i] == '.')
                return 'D';
        }
        return 'O';
    }
    if(b[0][3] == 'T')
    {
        if(b[1][2] == 'X')
        {
            for(int i = 2; i < 4; i++)
            {
                if(b[i][3 - i] == 'O'  || b[i][3 - i] == '.')
                    return 'D';
            }
            return 'X';
        }
        
        if(b[1][2] == 'O')
        {
            for (int i = 2; i < 4; i++)
            {
                if(b[i][3 - i] == 'X' || b[i][3 - i] == '.')
                    return 'D';
            }
            return 'O';
        }
        
        if(b[1][2] == '.')
            return 'D';
        
    }
    if(b[0][3] == '.')
    {
        return 'D';
    }
}