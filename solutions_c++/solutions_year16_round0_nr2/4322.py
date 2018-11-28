#include <iostream>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

static int testCase, S_length, ans, blankLocation;
static string S;

bool isAllHappy()
{
    for (int i = 0; i < S_length; i++)
        if (S[i] != '+') return false;
    return true;
}

void flip(int bottom)
{
    int temp;
    
    for (int top = 0; top <= bottom; top++)
    {
        if (S[top] == '+') S[top] = '-';
        else S[top] = '+';
    }
    
    for (int i = 0; i <= bottom / 2; i++)
    {
        temp = S[i];
        S[i] = S[bottom - i];
        S[bottom - i] = temp;
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
        fin >> S;
        
        S_length = S.length();
        ans = 0;
        
        while (!isAllHappy())
        {
            ans++;
            
            if (S[0] == '+')
            {
                for (int i = 1; i < S_length; i++)
                {
                    if (S[i] == '-')
                    {
                        blankLocation = i - 1;
                        break;
                    }
                }
                flip(blankLocation);
            }
            
            else
            {
                for (int i = S_length - 1; i >= 0; i--)
                {
                    if (S[i] == '-')
                    {
                        blankLocation = i;
                        break;
                    }
                }
                flip(blankLocation);
            }
        }
        
        fout << "Case #" << caseN + 1 << ": " << ans << endl;
    }
    
    return 0;
}
