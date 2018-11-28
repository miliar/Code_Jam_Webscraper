/* 
 * File:   main.cpp
 * Author: karan_000
 *
 * Created on April 12, 2014, 12:05 PM
 */

#include <cstdlib>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    int T;
    ofstream fout;
    ifstream fin;
    
    fin.open("C:\\Users\\karan_000\\Desktop\\GoogleCodeJam\\A-small-attempt2.in", ios::in);
    fout.open("C:\\Users\\karan_000\\Desktop\\GoogleCodeJam\\QualQ1_small_soln2.txt", ios::out | ios::trunc);
    
    fin>>T;
    
    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        int rownum1, rownum2;
        bool table[16];
        int outputNum = 0, outputCards = 0;
        int inputNum;
        
        for (int i = 0; i < 16; i++)
        {
            table[i] = false;
        }
        
        fin>>rownum1;
        for (int i = 1; i <= 4; i++)
        {
            for (int j = 1; j <= 4; j++)
            {
                fin>>inputNum;
                if (i == rownum1)
                {
                    table[inputNum - 1] = true;
                }
            }
        }
        
        fin>>rownum2;
        for (int i = 1; i <= 4; i++)
        {
            for (int j = 1; j <= 4; j++)
            {
                fin>>inputNum;
                if (i == rownum2 && table[inputNum - 1])
                {
                    outputCards++;
                    outputNum = inputNum;
                }
            }
        }
        
        fout<<"Case #"<<caseNum<<": ";
        switch (outputCards)
        {
            case 0:
                fout<<"Volunteer cheated!"<<endl;
                break;
                
            case 1:
                fout<<outputNum<<endl;
                break;
                
            default:
                fout<<"Bad magician!"<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}

