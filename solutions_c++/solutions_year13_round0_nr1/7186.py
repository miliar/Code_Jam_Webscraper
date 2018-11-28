#include <iostream>
#include <cstdlib>

using namespace std;

int xcount, ocount, tcount;
bool x, o;
bool dot;

bool isWinner()
{
    x=o=false;
    if ((xcount==4) || (xcount==3 && tcount==1))
    { x=true; return true; }
    if ((ocount==4) || (ocount==3 && tcount==1))
    { o=true; return true; }
    return false;
}

void counter(char c)
{
    if (c=='X')
        xcount++;
    else if (c=='O')
        ocount++;
    else if (c=='T')
        tcount++;
    else
        dot=true;
}

int main()
{
    ios_base::sync_with_stdio(0);

    int testy;

    char tab[4][4];
    bool winner;

    string result;

    cin>>testy;
    for (int numcase=1; numcase<=testy; numcase++)
    {
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                cin>>tab[i][j];

        dot=false;
        result="";
        winner=false;

        /*sprawdzenie wierszy*/
        for (int w=0; w<4; w++)
        {
            xcount=ocount=tcount=0;
            for (int i=0; i<4; i++)
                counter(tab[w][i]);

            if(isWinner())
            {
                winner=true;
                break;
            }
        }
        if(!winner)
        {
            /*sprawdzenie kolumn*/
            for (int k=0; k<4; k++)
            {
                xcount=ocount=tcount=0;
                for (int i=0; i<4; i++)
                    counter(tab[i][k]);

                if(isWinner())
                {
                    winner=true;
                    break;
                }
            }
        }
        if(!winner)
        {
            /*sprawdzenie przek¹tnej L->R*/
            xcount=ocount=tcount=0;
            for (int i=0; i<4; i++)
                counter(tab[i][i]);

            if(isWinner())
                winner=true;
        }
        if(!winner)
        {
            /*sprawdzenie przek¹tnej R->L*/
            xcount=ocount=tcount=0;
            for (int i=0; i<4; i++)
                counter(tab[i][3-i]);

            if(isWinner())
                winner=true;
        }

        if(winner)
        {
            if (x) result = "X won";
            else result = "O won";
        }
        else
        {
            if (!dot) result = "Draw";
            else result = "Game has not completed";
        }
        cout<<"Case #"<<numcase<<": "<<result<<endl;
    }
    return 0;
}
