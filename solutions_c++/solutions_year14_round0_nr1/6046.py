#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream in;
    in.open("A-small-attempt1.in");
    ofstream out;
    out.open("outputA.txt");
    int t;
    in>>t;
    for(int x  = 0; x < t;x++)
    {
        int rowA, rowB;
        int gridA [4][4];
        int gridB [4][4];
        in>>rowA;
        for(int i = 0; i< 4; i++)
        {
            for(int j = 0; j<4;j++)
            {
                in>>gridA[i][j];
            }
        }
        in>>rowB;
        for(int i = 0; i< 4; i++)
        {
            for(int j = 0; j<4;j++)
            {
                in>>gridB[i][j];
            }
        }
        bool card = false;
        int card_value = -1;
        bool bad = false;
        for(int i = 0; i<4;i++)
        {
            for(int j = 0; j<4;j++)
            {
                if(gridA[rowA-1][i] == gridB[rowB-1][j] && !card)
                {
                    card = true;
                    card_value = gridA[rowA-1][i];
                }
                else if(gridA[rowA-1][i] == gridB[rowB-1][j] && card)
                {
                    bad = true;
                    break;
                }
            }
        }
        if(card && !bad) out<<"Case #"<<x+1<<": "<<card_value<<endl;
        else if(bad) out<<"Case #"<<x+1<<": Bad magician!"<<endl;
        else out<<"Case #"<<x+1<<": Volunteer cheated!"<<endl;
    }
    return 0;
}
