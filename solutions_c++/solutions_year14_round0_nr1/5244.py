#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    //get the number of test cases
    string line;
    getline(cin,line);
    stringstream firstline(line);
    int numbertestcases;
    firstline >> numbertestcases;
    int row[2];
    int conf[2][4][4];
    bool hashtable[2][16];
    int nmatches;
    int number;
    for(int l=1;l<=numbertestcases;l++)
    {
        for(int m=1;m<=2;m++)
        {
            getline(cin,line);
            stringstream firstanswer(line);
            firstanswer >> row[m-1]; //answer
            for(int r=1;r<=4;r++)
            {
                getline(cin,line);
                stringstream rowline(line);
                rowline >> conf[m-1][r-1][0];
                rowline >> conf[m-1][r-1][1];
                rowline >> conf[m-1][r-1][2];
                rowline >> conf[m-1][r-1][3];
            }
        }
        //OK we have the numbers
        number = 0;
        nmatches = 0;
        for(int j=1;j<=2;j++)
        {
            for(int y=1;y<=16;y++) hashtable[j-1][y-1]=false;//init hash table
            for(int i=1;i<=4;i++) //copy into hashtable
            {
                hashtable[j-1][conf[j-1][row[j-1]-1][i-1]-1] = true;//-1 on number
            }
        }
        //search matches
        int x;
        for(int i=1;i<=4;i++)
        {
            x = conf[0][row[0]-1][i-1]; //different numbers in row
            //is x in second hash table
            if (hashtable[1][x-1]==true) //-1 on number
            {
                number = x;
                nmatches++;
            }
        }
        if (nmatches==1) cout << "Case #" << l << ": " << number << endl;
        else if (nmatches>1) cout << "Case #" << l << ": " << "Bad magician!" << endl;
        else cout << "Case #" << l << ": " << "Volunteer cheated!" << endl;
    }
    return 0;
}
