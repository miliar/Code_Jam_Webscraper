#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string xwon = "X won";
string owon = "O won";
string draw = "Draw";
string nowin = "Game has not completed";

char gamestate[4][4];

int checkresult()
{
    int tiles = 0;
    for(int x = 0; x <4; x++)
        {
            int countx = 0;
            int county = 0;
            int t = 0;
            for(int y = 0; y < 4; y++)
            {

                if(gamestate[x][y] == 'X')
                {
                  tiles++;
                  countx++;
                }
                else if(gamestate[x][y] == 'O')
                {
                    tiles++;
                    county++;
                }
                else if(gamestate[x][y] == 'T')
                {
                    tiles++;
                  t++;
                }

                if(y == 3)
                {

                    if((countx == 4) || (countx+t == 4))
                    {
                        return 0;
                    }
                    else if((county == 4) || (county+t == 4))
                    {
                        return 1;
                    }

                }
            }
        }

        for(int x = 0; x <4; x++)
        {
            int countx = 0;
            int county = 0;
            int t = 0;
            for(int y = 0; y < 4; y++)
            {
                if(gamestate[y][x] == 'X')
                {
                  //tiles++;
                  countx++;
                }
                else if(gamestate[y][x] == 'O')
                {
                    //tiles++;
                    county++;
                }
                else if(gamestate[y][x] == 'T')
                {
                  t++;
                }

                if(y == 3)
                {
                    if((countx == 4) || (countx+t == 4))
                    {
                        return 0;
                    }
                    else if((county == 4) || (county+t == 4))
                    {
                        return 1;
                    }

                }
            }
        }

int countx = 0;
                int county = 0;
                int t = 0;
        for(int x = 0; x <4; x++)
        {

            for(int y = 0; y < 4; y++)
            {
                if(y == x)
                {

                if(gamestate[y][x] == 'X')
                {
                  //tiles++;
                  countx++;
                }
                else if(gamestate[y][x] == 'O')
                {
                    //tiles++;
                    county++;
                }
                else if(gamestate[y][x] == 'T')
                {
                  t++;
                }

                if(x == 3)
                {

                }
            }
            }
            if((countx == 4) || (countx+t == 4))
                    {
                        return 0;
                    }
                    else if((county == 4) || (county+t == 4))
                    {
                        return 1;
                    }

        }

countx = 0;
                county = 0;
                t = 0;
        for(int x = 0; x <4; x++)
        {

            for(int y = 0; y < 4; y++)
            {
                if(x+y == 3)
                {

                if(gamestate[x][y] == 'X')
                {
                  //tiles++;
                  countx++;
                }
                else if(gamestate[x][y] == 'O')
                {
                    //tiles++;
                    county++;
                }
                else if(gamestate[x][y] == 'T')
                {
                  t++;
                }

                if(x == 3)
                {


                }
            }
            }
            if((countx == 4) || (countx+t == 4))
                    {
                        return 0;
                    }
                    else if((county == 4) || (county+t == 4))
                    {
                        return 1;
                    }
        }

        if(tiles == 16)
            return 2;
        else
            return 3;

}

int main()
{
    fstream in("A-large.in", ios::in);
    fstream out("output.txt", ios::out);
    int t;

    in >> t;

    for(int i =0; i < t; i++)
    {
        for(int x = 0; x <4; x++)
        {
            for(int y = 0; y < 4; y++)
            {
                in >>gamestate[x][y];
            }
        }
        int result = checkresult();
        out << "Case #" << i+1 <<": ";
        switch(result)
        {
        case 0:
            out << xwon << endl;
            break;
        case 1:
            out << owon << endl;
            break;
        case 2:
            out << draw << endl;
            break;
        case 3:
            out << nowin << endl;
            break;
            }

        }



    in.close();
    out.close();
    return 0;
}
