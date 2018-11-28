#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    bool X = false,O=false;
    ifstream myReadFile;
    ofstream myPrintFile;
    myReadFile.open("large.in");
    myPrintFile.open("out.out");
    int tic_tac_toe_O[4][4];
    int tic_tac_toe_X[4][4];
    int tic_O[10];
    int tic_X[10];
    int dummy=0;
    int sum = 0;
    char character,empty_;
    int cases;
    myReadFile>>cases;
    for(int c=1; c<=cases; c++)
    {
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                myReadFile>>character;
                if(character=='X'||character=='O'||character=='T')
                {
                    sum = sum + 1;
                }
                if(character=='O' ||character=='T')
                {
                    tic_tac_toe_O[i][j]=1;
                }
                else
                {
                    tic_tac_toe_O[i][j]=0;
                }
                if(character=='X' ||character=='T')
                {
                    tic_tac_toe_X[i][j]=1;
                }
                else
                {
                    tic_tac_toe_X[i][j]=0;
                }

            }
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                dummy = dummy + tic_tac_toe_O[i][j];
            }
            tic_O[i] = dummy;
            dummy =0;
        }
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                dummy = dummy + tic_tac_toe_O[j][i];
            }
            tic_O[i+4] = dummy;
            dummy =0;
        }
        for(int i=0; i<4; i++)
        {
            dummy = dummy + tic_tac_toe_O[i][i];
        }
        tic_O[8] = dummy;
        dummy = 0;
        for(int i=0; i<4; i++)
        {
            dummy = dummy + tic_tac_toe_O[3-i][i];
        }
        tic_O[9] = dummy;
        dummy = 0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                dummy = dummy + tic_tac_toe_X[i][j];
            }
            tic_X[i] = dummy;
            dummy =0;
        }
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                dummy = dummy + tic_tac_toe_X[j][i];
            }
            tic_X[i+4] = dummy;
            dummy =0;
        }
        for(int i=0; i<4; i++)
        {
            dummy = dummy + tic_tac_toe_X[i][i];
        }
        tic_X[8] = dummy;
        dummy = 0;
        for(int i=0; i<4; i++)
        {
            dummy = dummy + tic_tac_toe_X[3-i][i];
        }
        tic_X[9] = dummy;
        dummy = 0;
        for(int i=0; i<10; i++)
        {
            if(tic_O[i]==4)
            {
                O = true;
            }
        }
        for(int i=0; i<10; i++)
        {
            if(tic_X[i]==4)
            {
                X = true;
            }
        }
        myPrintFile<<"Case #"<<c<<": ";
        if(X==true)
        {
            myPrintFile<<"X won"<<endl;
        }
        if(O==true)
        {
            myPrintFile<<"O won"<<endl;
        }
        if(X==false&&O==false&&sum==16)
        {
            myPrintFile<<"Draw"<<endl;
        }
        if(X==false&&O==false&&sum!=16)
        {
            myPrintFile<<"Game has not completed"<<endl;
        }
        sum = 0;
        dummy = 0;
        O = false;
        X = false;
    }
}


