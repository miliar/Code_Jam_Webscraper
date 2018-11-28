#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("MagicTrickOut.out");
    int n;
    in>>n;
    for(int a=1;a<=n; a++)
    {
        int cards[4][4], cards2[4][4], i, j, pos1, pos2;
        in>>pos1;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                in>>cards[i][j];
            }
        }
        in>>pos2;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                in>>cards2[i][j];
            }
        }

        int cont=0, aux;

        for(i=0;i<4;i++)
        {
            for(j=0; j<4;j++)
            {
                if(cards[pos1-1][i]==cards2[pos2-1][j])
                {
                    cont++; aux=cards[pos1-1][i];
                }
            }
        }

        if(cont==1)
        {
            out<<"Case #"<<a<<": "<<aux<<"\n";
        }
        else
        {
            if(cont>1)
            {
                out<<"Case #"<<a<<": "<<"Bad magician!"<<"\n";
            }
            else
            {
               out<<"Case #"<<a<<": "<<"Volunteer cheated!"<<"\n";
            }
        }






    }



}
