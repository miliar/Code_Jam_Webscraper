#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main(int argc, char * argv[])
{
    int cases = 0;
    ifstream fin("B-small-attempt0.in");
    ofstream fout("write2.txt");

    bool s[100] = {};
    char read = 0;
    int height = 0;
    int moves = 0;

    bool tmp = false;

    if(fin.is_open())
    {
        //cout << "Opened File" << endl;

        fin >> cases;

        for(int casenum = 1; casenum <= cases; casenum++)
        {
            fout << "Case #" << casenum << ": ";
            moves = 0;

            fin >> noskipws >> read;
            for(height = 0; fin.peek() != '\n' && fin.peek() != EOF; height++)
            {
                fin >> read;
                if(read == '+')
                {
                    s[height] = true;
                }
                else if(read == '-')
                {
                    s[height] = false;
                }
            }

            for(int parse = 0; parse < height; parse++)
            {
                if(s[parse] == false)
                {
                    for(int allminus = 0; allminus < parse; allminus++)
                    {
                        s[allminus] = false;
                    }
                    if(parse != 0)
                    {
                        moves++;
                    }

                    while(s[parse + 1] == false && parse < height)
                    {
                        parse++;
                    }

                    for(int allplus = 0; allplus <= parse; allplus++)
                    {
                        s[allplus] = true;
                    }
                    moves++;
                }
            }

            fout << moves << endl;
        }

        fin.close();
        fout.close();
    }
    else
    {
        cout << "Could not open file." << endl;
    }

    return 0;
}
