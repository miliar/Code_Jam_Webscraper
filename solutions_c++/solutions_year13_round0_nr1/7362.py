#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int row(vector<string> v)
{
    for(int j=0 ; j<4 ; j++)
        {
            int X=0;
            int O=0;

            for(int i=0 ; i<4 ; i++)
            {
                if(v[j][i] == 'X' || v[j][i] == 'T')
                    X++;
                if(v[j][i] == 'O' || v[j][i] == 'T')
                    O++;
            }
            if(X == 4)
            {
                return 1;
            }
            if(O == 4)
            {
             return 2;
            }
        }
        return 3;
}
int column(vector<string> v)
{
    for(int j=0 ; j<4 ; j++)
        {
            int X = 0;
            int O = 0;

            for(int i=0 ; i<4 ; i++)
            {
                if(v[i][j] == 'X' || v[i][j] == 'T')
                    X++;
                if(v[i][j] == 'O' || v[i][j] == 'T')
                    O++;
            }
            if(X == 4)
            {
               return 1;
            }
            if(O == 4)
            {
                return 2;
            }
        }
        return 3;
}

int main_diagonal(vector<string> v)
{
    int X = 0;
    int O = 0;
    for(int k = 0 ; k<4 ; k++)
        {
            if(v[k][k] == '.')
                return 3;
            if(v[k][k] == 'X' || v[k][k]== 'T')
                X++;

            if(v[k][k] == 'O' || v[k][k]== 'T')
                O++;


        }
        if(X == 4)
        {
            return 1;
        }
        if(O == 4)
        {
            return 2;
        }
        return 3;
}

int other_diagonal(vector<string> v)
{

    int X = 0;
    int O = 0;

       int i = 0;
            for(int k=3 ; k>=0 ; k--)
            {

                if(v[i][k] == '.')
                return 3;

                if(v[i][k]== 'X' || v[i][k] == 'T')
                    X++;

                if(v[i][k]== 'O' || v[i][k]== 'T')
                    O++;
                    i++;
            }

        if(X == 4)
        {
            return 1;
        }
        if(O == 4)
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
    int T;
    cin>>T;

    for(int i =0 ; i<T ; i++)
    {
        vector<string> v(4);
        for(int j=0; j<4 ; j++)
            cin>>v[j];

        bool notComplete = true;

        string result=" ";


        if(row(v)== 1 || column(v)==1 || main_diagonal(v)==1 || other_diagonal(v)== 1)
            result ="X won";
        else if(row(v)== 2 || column(v)==2 || main_diagonal(v)==2 || other_diagonal(v)== 2)
            result ="O won";
            else
            {
        for(int k=0; k<4; k++)
        {
            for(int n=0; n<4; n++)
            {
                if(v[k][n] != '.')
                    notComplete = false;

                else if(v[k][n] == '.')
                {
                    notComplete = true;
                    break;
                }
            }
            if(notComplete)
                break;
        }
            if(notComplete)
                result ="Game has not completed";
            if(!notComplete)
                result = "Draw";
            }

        cout<<"Case #"<<i+1<<": "<<result<<endl;
    }

    return 0;
}
