#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;


void checkResult(char* file)
{
    ifstream fileIn(file);
    ofstream fileOu("OutputResult.txt");

    if(fileOu && fileIn)
    {
        int T, M, N, i(1);
        fileIn >> T;
        while(i <= T)
        {
            fileIn >> N;
            fileIn >> M;
            int sch[101][101];
            for(int j(0); j<N; j++)
            {
                for(int k(0); k<M; k++)
                {
                    fileIn >> sch[j][k];
                }
            }
            bool statCol = true;
            bool statLig = true;
            for(int l(0); l<N; l++)
            {
                for(int c(0); c<M; c++)
                {
                    statCol = true;
                    statLig = true;
                    for(int h(0); h<=100; h++)
                    {
                        if(sch[l][c] == h)
                        {
                            int testL = 0;
                            while(testL < N)
                            {
                                if(sch[l][c] < sch[testL][c])
                                {
                                    statLig = false;
                                    break;
                                }
                                testL++;
                            }
                            int testC = 0;
                            while(testC < M)
                            {
                                if(sch[l][c] < sch[l][testC])
                                {
                                    statCol = false;
                                    break;
                                }
                                testC++;
                            }
                            if(statCol == false && statLig == false)
                            {
                                break;
                            }
                        }
                    }
                    if(statCol == false && statLig == false)
                    {
                        break;
                    }
                }
                if(statCol == false && statLig == false)
                {
                    break;
                }
            }
            if(statCol == false && statLig == false)
            {
                fileOu << "Case #" << i << ": " << "NO" << endl;
            }
            else
            {
                fileOu << "Case #" << i << ": " << "YES" << endl;
            }
            i++;
        }
    }
    else
    {
        cout << "Fichier non ouvert. Fin du programme" << endl;
    }
}

int main(int argc, char** argv)
{
    checkResult(argv[1]);
    return 0;
}
