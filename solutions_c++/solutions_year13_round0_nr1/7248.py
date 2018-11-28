/*Abram Thiessen
 *Tic-Tac-Toe-Tomek
 *Google Code Jam qualification round
 *13 April 2013
 */

#include <iostream>
#include <fstream>

using namespace std;
const int row=4,col=4,di=2;

int main()
{
    int cases;          //number of cases
    int r,c,i,full;     //increment variables
    bool stop=0;        //stops win check loop
    char board[row][col];
    int rline[row];     //horizontal line
    int cline[col];     //vettical lines
    int dline[di];      //diagonal lines
    ifstream inFile;    //input file
    ofstream outFile;
    inFile.open("A-large.in");    //open the file
    outFile.open("TTT.out");    //open the file
    if (inFile.fail())  //if the file did not open
    {
        cout << "The file did not open";
        return 0;
    }
    inFile>>cases;
    for (int i=1;((i<=cases)&&inFile.good());i++)
    {
        for (r=0;r<row;r++) //resetting win check counters
        {
            rline[r]=0;
            cline[r]=0;
            dline[r]=0;
        }
        for (r=0;r<row;r++)
        {
            for (c=0;c<col;c++)
            {
                inFile>>board[r][c];
                if (board[r][c]=='X')
                {
                    rline[r]++;
                    cline[c]++;
                    if (c==r)
                        dline[1]++;
                    else if ((r+c)==3)
                        dline[0]++;
                }
                else if (board[r][c]=='O')
                {
                    rline[r]--;
                    cline[c]--;
                    if (c==r)
                        dline[1]--;
                    else if ((r+c)==3)
                        dline[0]--;
                }
                else if (board[r][c]=='.')
                {
                    rline[r]=100;
                    cline[c]=100;
                    if (c==r)
                        dline[1]=100;
                    else if ((r+c)==3)
                        dline[0]=100;
                }
            }
        }
        for (r=0;r<row;r++) //resetting win check counters
        /*{
            cout<<rline[r]<<" ";
            cout<<cline[r]<<" ";
            cout<<dline[r%2]<<endl;
        }*/
        full=0;
        stop=0;
        for (r=0;r<row&&stop==0;r++)
        {
            if (rline[r]<50)    //has no dot
            {
                if      (rline[r]>=3)
                {
                    outFile <<"Case #"<<i<<": X won"<<endl;
                    //cout    <<"Case #"<<i<<": X won row"<<endl;
                    stop=1;
                }
                else if (rline[r]<=-3)
                {
                    outFile <<"Case #"<<i<<": O won"<<endl;
                    //cout    <<"Case #"<<i<<": O won row"<<endl;
                    stop=1;
                }
                full++;
            }
            if (stop==0)
            {
                if (cline[r]<50)    //has no dot
                {
                    if      (cline[r]>=3)
                    {
                        outFile <<"Case #"<<i<<": X won"<<endl;
                        //cout    <<"Case #"<<i<<": X won col"<<endl;
                        stop=1;
                    }
                    else if (cline[r]<=-3)
                    {
                        outFile <<"Case #"<<i<<": O won"<<endl;
                        //cout    <<"Case #"<<i<<": O won col"<<endl;
                        stop=1;
                    }
                }
                if (stop==0)
                {
                    if (r<2)
                    {
                        if (dline[r]<50)
                        {
                            if      (dline[r]>=3)
                            {
                                outFile <<"Case #"<<i<<": X won"<<endl;
                                //cout    <<"Case #"<<i<<": X won di"<<endl;
                                stop=1;
                            }
                            else if (dline[r]<=-3)
                            {
                                outFile <<"Case #"<<i<<": O won"<<endl;
                                //cout    <<"Case #"<<i<<": O won di"<<endl;
                                stop=1;
                            }
                        }
                    }
                }
            }
        }
        if (stop==0)
        {
            if (full==4)
                outFile <<"Case #"<<i<<": Draw"<<endl;
            else
                outFile <<"Case #"<<i<<": Game has not completed"<<endl;
        }
        //cout<<endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}
