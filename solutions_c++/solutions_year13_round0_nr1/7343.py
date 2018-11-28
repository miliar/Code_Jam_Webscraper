#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int check_row(vector<string> myVec)
{
    for(int j=0 ; j<4 ; j++)
        {
            int countX=0;
            int countO=0;

            for(int k=0 ; k<4 ; k++)
            {
                if(myVec[j][k] == 'X' || myVec[j][k] == 'T')
                    countX++;
                if(myVec[j][k] == 'O' || myVec[j][k] == 'T')
                    countO++;
            }
            if(countX == 4)
            {
                return 1;    // 1 if x win
            }
            if(countO == 4)
            {
             return 2;   // 2 if o win
            }
        }
        return 3;
}
int check_column(vector<string> myVec)
{
    for(int j=0 ; j<4 ; j++)
        {
            int countX = 0;
            int countO = 0;

            for(int k=0 ; k<4 ; k++)
            {
                if(myVec[k][j] == 'X' || myVec[k][j] == 'T')
                    countX++;
                if(myVec[k][j] == 'O' || myVec[k][j] == 'T')
                    countO++;
            }
            if(countX >= 4)
            {
               return 1;
            }
            if(countO >= 4)
            {
                return 2;
            }
        }  // checked the rows and columns
        return 3;
}

int check_main_diagonal(vector<string> myVec)
{
    int countX = 0;
    int countO = 0;
    for(int k = 0 ; k<4 ; k++)
        {
            if(myVec[k][k] == '.')
                return 3;
            if(myVec[k][k] == 'X' || myVec[k][k]== 'T')
                countX++;

            if(myVec[k][k]== 'O' || myVec[k][k]== 'T')
                countO++;


        }    // check the main diagonal
        if(countX == 4)
        {
            return 1;
        }
        if(countO == 4)
        {
            return 2;
        }
        return 3;
}

int check_other_diagonal(vector<string> myVec)
{

    int countX = 0;
    int countO = 0;

       int n = 0;
            for(int k=3 ; k>=0 ; k--)
            {

                if(myVec[n][k] == '.')
                return 3;

                if(myVec[n][k]== 'X' || myVec[n][k] == 'T')
                    countX++;

                if(myVec[n][k]== 'O' || myVec[n][k]== 'T')
                    countO++;
                    n++;
            }
          // check the other diagonal
        if(countX >= 4)
        {
            return 1;
        }
        if(countO >= 4)
        {
            return 2;
        }
        else
            return 3;
}
int main()
{
    freopen("A-large.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
    freopen("output.txt", "wt", stdout); // same for out.txt
    long T;
    cin>>T;

    for(int i =0 ; i<T ; i++)
    {
        vector<string> myVec(4);
        for(int j=0; j<4 ; j++)
            cin>>myVec[j];

        bool notComplete = true;

        string result=" ";
       /* cout<<"row"<<check_row(myVec)<<endl;
        cout<<"col"<<check_column(myVec)<<endl;
        cout<<"main"<<check_main_diagonal(myVec)<<endl;
        cout<<"other"<<check_other_diagonal(myVec)<<endl;*/

        if(check_row(myVec)== 1 || check_column(myVec)==1 || check_main_diagonal(myVec)==1 || check_other_diagonal(myVec)== 1)
            result ="X won";
        else if(check_row(myVec)== 2 || check_column(myVec)==2 || check_main_diagonal(myVec)==2 || check_other_diagonal(myVec)==2)
            result ="O won";
            else
            {
        for(int k=0; k<4; k++)
        {
            for(int n=0; n<4; n++)
            {
                if(myVec[k][n] != '.')
                    notComplete = false;

                else if(myVec[k][n] == '.')
                {
                    notComplete = true;
                    break;
                }
            }
            if(notComplete)
                break;
        }   // check if completed or no
            if(notComplete)
                result ="Game has not completed";
            if(!notComplete)
                result = "Draw";
            }

        cout<<"Case #"<<i+1<<": "<<result<<endl;
    }
    return 0;
}
