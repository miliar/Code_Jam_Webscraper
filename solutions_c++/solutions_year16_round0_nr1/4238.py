#include <iostream>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

static int testCase, N, currentN;
static bool digits[10];

bool checkDigits()
{
    for (int i = 0; i < 10; i++)
        if (!digits[i]) return false;
    return true;
}

void seeDigits(int N)
{
    while (N)
    {
        digits[N % 10] = true;
        N /= 10;
    }
}

int main(void)
{
    string fileName;
    
    cin >> fileName;
    
    ifstream fin(fileName);
    ofstream fout("output.txt");
    
    fin >> testCase;
    
    for (int caseN = 0; caseN < testCase; caseN++)
    {
        for (int i = 0; i < 10; i++)
            digits[i] = false;
        
        fin >> N;
        
        if (N == 0)
        {
            fout << "Case #" << caseN + 1 << ": INSOMNIA" << endl;
        }
        
        else
        {
            for (int i = 1; !checkDigits(); i++)
            {
                currentN = N * i;
                
                seeDigits(currentN);
            }
            
            fout << "Case #" << caseN + 1 << ": " << currentN << endl;
        }
    }
    
    return 0;
}
