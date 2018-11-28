#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string.h>
#include <fstream>
#include <time.h>

using namespace std ;

int main()
{
    cout<< "Start!"<< endl;



    clock_t t;
    t = clock();


    char* filename = "../A-large.in";

    ifstream fr;
    ofstream fw("../output.txt") ;

    fr.open(filename);
    if (fr != NULL)
    {
        //Read input
        int n ;
        fr >> n ;
        cout<< "T="<< n<<endl;
        for (int i=0 ; i < n; i++)
        {
            int winCase=0;
            bool ptExist=false;

            int m[4][4];
            for (int j=0;j<4;j++)
                for (int k=0;k<4;k++)
                {
                    char c;
                    fr >> c;
                    switch(c)
                    {
                    case 'X':
                        m[j][k]=1;
                        break;
                    case 'O':
                        m[j][k]=-1;
                        break;
                    case 'T':
                        m[j][k]=9;
                        break;
                    case '.':
                        m[j][k]=0;
                        ptExist = true;
                        break;
                    default:
                        m[j][k]=0;
                    }
                }
            if(fr.eof())
                break;


            //display
            for (int j=0;j<4;j++)
            {
                for (int k=0;k<4;k++)
                    cout << m[j][k];
                cout << endl;
            }

            //Compute

            int sumD1 = m[0][0]+m[1][1]+m[2][2]+m[3][3];
            int sumD2 = m[0][3]+m[1][2]+m[2][1]+m[3][0];

            if (sumD1 == 4 || sumD1 == 12 || sumD2 == 4 || sumD2 == 12)
            {
                winCase = 1;
            }
            else if (sumD1 == -4 || sumD1 == 6 || sumD2 == -4 || sumD2 == 6)
            {
                winCase = 2;
            }
            else
            {
                for (int j=0;j<4;j++)
                {
                    int sumR = m[j][0]+m[j][1]+m[j][2]+m[j][3];
                    int sumC = m[0][j]+m[1][j]+m[2][j]+m[3][j];
                    if (sumR == 4 || sumC == 4 || sumR == 12 || sumC == 12)
                    {
                        winCase = 1;
                        break;
                    }
                    else if (sumR == -4 || sumC == -4 || sumR == 6 || sumC == 6)
                    {
                        winCase = 2;
                        break;
                    }
                }
                if (winCase==0 && ptExist)
                    winCase=4;
                else if (winCase==0 && (!ptExist))
                    winCase=3;
            }

        //output

            switch(winCase)
            {
                case 1:
                    cout << "Case #" <<i+1<<": X won"<< endl;
                    fw << "Case #" <<i+1<<": X won"<< endl;
                    break;
                case 2:
                    cout << "Case #" <<i+1<<": O won"<< endl;
                    fw << "Case #" <<i+1<<": O won"<< endl;
                    break;
                case 3:
                    cout << "Case #" <<i+1<<": Draw"<< endl;
                    fw << "Case #" <<i+1<<": Draw"<< endl;
                    break;
                case 4:
                    cout << "Case #" <<i+1<<": Game has not completed"<< endl;
                    fw << "Case #" <<i+1<<": Game has not completed"<< endl;
                    break;
                default:
                    cout << "error"<< endl;
            }

        }//for each test
    }
    fr.close() ;
    fw.close();

    t = clock() - t;

    cout <<"Time: "<< (float)t <<" s"<< endl;

    return 0;
}
