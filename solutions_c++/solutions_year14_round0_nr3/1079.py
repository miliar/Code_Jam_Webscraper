#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream infile("C-small-attempt0.in");
ofstream outfile("C-small-attempt0.out");

char mine[5][5];
char mineInitial[5][5];
bool clicked[5][5];

int T,t;
int R,C,M;

/*void display(char* arr)
{
    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            cout << arr[i*C+j];
        }
        cout << endl;
    }
}*/

void resultSpecial(char* arr)
{
    outfile << "Case #" << t+1 << ": " << endl;
    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            if(arr[i*C+j]=='*')
                outfile << '*';
            else
                outfile << 'c';
        }
        outfile << endl;
    }
}

void result(int i1, int j1)
{
    outfile << "Case #" << t+1 << ": " << endl;
    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            if(i==i1 && j==j1)
                outfile << 'c';
            else if(mineInitial[i][j]=='*')
                outfile << '*';
            else
                outfile << '.';
        }
        outfile << endl;
    }
}

/*void displayMine()
{
    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            cout << mine[i][j];
        }
        cout << endl;
    }
}*/

void initializeClick()
{
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            clicked[i][j]=false;
}
void click(int i, int j)
{
    if(i<0 || j<0 || i>=R || j>=C)
        return;
    if(clicked[i][j])
        return;
    clicked[i][j]=true;
    if(mine[i][j]=='0')
    {
        click(i-1,j-1);
        click(i-1,j);
        click(i-1,j+1);
        click(i,j-1);
        click(i,j+1);
        click(i+1,j-1);
        click(i+1,j);
        click(i+1,j+1);
    }
    return;
}
int main()
{
    infile >> T;

    for(t=0; t<T; t++)
    {
        infile >> R >> C >> M;

        char* arr = new char[R*C];

        int index;
        for(index=0; index<M; index++)
            arr[index]='*';
        //cout << index << endl;
        for( ; index<R*C; index++)
            arr[index]='.';

        if(M+1==R*C)
        {
            resultSpecial(arr);
            continue;
        }

        bool done=false;
        do
        {
            for(int i=0; i<R; i++)
                for(int j=0; j<C; j++)
                    mineInitial[i][j] = mine[i][j] = arr[i*C+j];

            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    int mineCount=0;
                    if(mine[i][j]=='*')
                        continue;
                    if(mine[i-1][j-1]=='*' && i-1>=0 && j-1>=0)
                        mineCount++;
                    if(mine[i-1][j]=='*' && i-1>=0)
                        mineCount++;
                    if(mine[i-1][j+1]=='*' && i-1>=0 && j+1<C)
                        mineCount++;

                    if(mine[i][j-1]=='*' &&j-1>=0)
                        mineCount++;

                    if(mine[i][j+1]=='*' && j+1<C)
                        mineCount++;

                    if(mine[i+1][j-1]=='*' && j-1>=0 && i+1<R)
                        mineCount++;
                    if(mine[i+1][j]=='*' && i+1<R)
                        mineCount++;
                    if(mine[i+1][j+1]=='*' && i+1<R && j+1<C)
                        mineCount++;
                    mine[i][j]= '0'+mineCount;
                }
            }

            int i1,j1;
            bool found = false;
            for(i1=0; i1<R; i1++)
            {
                for(j1=0; j1<C; j1++)
                {
                    if(mine[i1][j1]=='0')
                    {
                        found=true;
                        break;
                    }
                }
                if(found)
                    break;
            }

            if(!found)
                continue;
            initializeClick();
            click(i1,j1);

            bool impos=false;
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(clicked[i][j] || mine[i][j]=='*')
                        continue;
                    else
                    {
                        impos=true;
                        break;
                    }
                }
                if(impos)
                    break;
            }
            if(!impos)
            {
                result(i1,j1);
                done=true;
                break;
            }
        }while(next_permutation(arr,arr+R*C));
        if(!done)
        {
            outfile << "Case #" << t+1 << ": " << endl << "Impossible" << endl;
        }
    }

    infile.close();
    outfile.close();
    return 0;
}
