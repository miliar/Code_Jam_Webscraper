#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

bool palindrome(int nbe)
{
    int inverse(0), tmp(nbe);
    while (tmp>0)
    {
        inverse=(inverse*10) + tmp%10;
        tmp=tmp/10;
    }
    if(nbe == inverse)
        return true;
    else
        return false;

}

void checkResult(char* file)
{
    ifstream fileIn(file);
    ofstream fileOu("OutputResult.txt");

    if(fileOu && fileIn)
    {
        int nbtest(0), mini(0), maxi(0), i(0), tmpE(0), tmpZ(0), res(0);
        double tmpR(0), tmpF(0);
        string test;
        fileIn >> nbtest;

        while(i != nbtest)
        {
            res = 0;
            tmpR = 0.00;
            tmpE = 0;
            tmpF = 0.00;

            fileIn >> mini;
            fileIn >> maxi;
            i++;
            for(int j=mini; j<=maxi; j++)
            {
                if(palindrome(j))
                {
                    tmpR = sqrt(j);
                    tmpE = floor(tmpR);
                    tmpF = tmpR - tmpE;
                    if(tmpF == 0.0000000000000000)
                    {
                        tmpZ = (int)tmpR;
                        if(palindrome(tmpZ))
                        {
                            res++;
                        }
                    }
                }
            }
            fileOu << "Case #" << i << ": " << res << endl;
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
