#include <bits/stdc++.h>
#define REP(i, a, b) for(int i = int(a); i < int(b); i++)
using namespace std;

string flip(string str, int iIndex);

int main(int argc, char** argv)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    REP(t, 1, T + 1)
    {
        cout << "Case #" << t << ": ";
        string str;
        int iWordLength = 0, iTemp;
        int iCount = 0;
        
        cin >> str;
        iWordLength = str.length();

        bool bContinueLoop = true;

        do {
            iTemp = iWordLength - 1;
            while(iTemp != -1) {
                if(str[iTemp] == '+') {
                    iTemp--;
                } else {
                    break;
                }
            }

            if(iTemp != -1) {
                if(str[0] == '+') {
                    iTemp = 1;
                    while(str[iTemp] == '+')
                        iTemp++;
                    str = flip(str, iTemp - 1);
                } else {
                    str = flip(str, iTemp);
                }
                iCount++;
            } else {
                bContinueLoop = false;
            }

        } while(bContinueLoop);

        cout << iCount << endl;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

string flip(string str, int iIndex)
{
    int i = 0;
    string temp;
    temp = str;

    REP(i, 0, iIndex + 1)
    {
        char ch = str[iIndex - i];
        if(ch == '-') {
            temp[i] = '+';
        } else {
            temp[i] = '-';
        }
    }
    return temp;
}
