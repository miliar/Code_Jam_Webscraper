
#include <fstream>
#include <string.h>

using namespace std;

int T; //nr. testcases
char game[4][5];
ifstream f1("A-small-attempt0.in");
ofstream f2("A-small-attempt0.out");

void read()
{
    for (int i=0; i<4; i++)
    {
        f1.get();
        f1.get(game[i], 5);

    }
    f1.get();

}


int win_no_T(int i)
{
    //check if somebody won without Ts:
    for (int j=0; j<4; j++)
        if (game[j][0]!='.' &&
            game[j][0]==game[j][1] &&
            game[j][0]==game[j][2] &&
            game[j][0]==game[j][3])
        {
            f2<<"Case #"<<i<<": "<<game[j][0]<<" won"<<endl;
            return 1;
        }
        else if (game[0][j]!='.' &&
                game[0][j]==game[1][j] &&
                game[0][j]==game[2][j] &&
                game[0][j]==game[3][j])
        {
            f2<<"Case #"<<i<<": "<<game[0][j]<<" won"<<endl;
            return 1;
        }


    if (game[0][0]!='.' &&
        game[0][0]==game[1][1] &&
        game[0][0]==game[2][2] &&
        game[0][0]==game[3][3])
    {
        f2<<"Case #"<<i<<": "<<game[0][0]<<" won"<<endl;
        return 1;
    }
    if (game[0][3]!='.' &&
        game[0][3]==game[1][2] &&
        game[0][3]==game[2][1] &&
        game[0][3]==game[3][0])
    {
        f2<<"Case #"<<i<<": "<<game[0][3]<<" won"<<endl;
        return 1;
    }

    return 0;

}


//check if somebody won with a T and find its position
int win_T(int i)
{
    int isT=0;
    int u, j;
    for (u=0; u<4 && !isT; u++)
        for (j=0; j<4 && !isT; j++)
            if (game[u][j]=='T')
                    isT=1;
    u--;
    j--;


    if (isT)
    {
        //check for 3 Xs on T's column/line
        int c=0, l=0;
        for(int k=0; k<4; k++)
        {   if(game[u][k]=='X')
                l++;
            if (game[k][j]=='X')
                c++;
        }
        if (c==3 || l==3)
        {
            f2<<"Case #"<<i<<": X won"<<endl;
            return 1;
        }

        //check for 3 Os on T's column/line
        c=0;
        l=0;
        for(int k=0; k<4; k++)
        {   if(game[u][k]=='O')
                l++;
            if (game[k][j]=='O')
                c++;
        }
        if (c==3 || l==3)
        {
            f2<<"Case #"<<i<<": O won"<<endl;
            return 1;
        }


        //if T is on the principal diagonal
        //check for 3 Xs or 3 Os there
        if (u==j)
        {
            int x=0, o=0;
            for (int k=0; k<4; k++)
            {
                if (game[k][k]=='X')
                    x++;
                else if (game[k][k]=='O')
                    o++;
            }

            if (o==3 || x==3)
            {
                f2<<"Case #"<<i<<": "<<game[0][0]<<" won"<<endl;
                return 1;
            }
        }

        //if T is on the secondary diagonal
        //check for 3 Xs or 3 Os there
        else if (j==3-u)
        {
            int x=0, o=0;
            for (int k=0; k<4; k++)
            {
                if (game[k][3-k]=='X')
                    x++;
                else if (game[k][3-k]=='O')
                    o++;
            }

            if (o==3 || x==3)
            {
                f2<<"Case #"<<i<<": "<<game[0][3]<<" won"<<endl;
                return 1;
            }
        }



    }

    return 0;

}

int check_game(int i)
{
    if (win_T(i))
        return 1;

    if (win_no_T(i))
        return 1;




    int dot=0;
    for (int j=0; j<4 && !dot; j++)
        if (strchr(game[j], '.')!=NULL)
            dot=1;


    if (dot)
    {   f2<<"Case #"<<i<<": Game has not completed"<<endl;
        return 1;
    }
    else
    {
        f2<<"Case #"<<i<<": Draw"<<endl;
        return 1;
    }

}

int main()
{
    f1>>T;
    for (int i=1; i<=T; i++)
    {

        read();

        check_game(i);
    }

    f1.close();
    f2.close();
    return 0;
}
