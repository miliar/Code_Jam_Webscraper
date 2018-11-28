#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream fin, fout;
    fin.open("A-small-attempt1.in");
    fout.open("c1.txt");
    int T, ans1, ans2, i, j, k, counter = 0, ans = 0;
    int deck1[4][4], deck2[4][4];
    fin >> T;
    for(k=0; k< T; k++)
        {
            counter = 0; ans = 0;
            fin >> ans1;
            for (i = 0; i<4; i++)
            {
                for (j = 0; j<4; j++)
                {
                    fin >> deck1[i][j];
                }
            }
            fin >> ans2;
            for (i = 0; i<4; i++)
            {
                for (j = 0; j<4; j++)
                {
                    fin >> deck2[i][j];
                }
            }
            for (i=0; i< 4; i++)
            {
                for (j=0; j< 4; j++)
                {
                    if(deck1[ans1-1][i] == deck2[ans2-1][j])
                    {
                        counter++; ans = deck1[ans1-1][i];
                    }
                    //cout << deck1[ans1-1][i] << endl;
                }
            }

        fout << "Case #"<< k+1<< ": ";
        if(counter > 1) fout << "Bad magician!"<<endl;
        if(counter == 1) fout << ans<< endl;
        if(counter == 0) fout << "Volunteer cheated!" << endl;
        }
            fout.close();
            return 0;
    }
