#include <bits/stdc++.h>
#define REP(i, a, b) for(int i = int(a); i < int(b); i++)

using namespace std;
int main(int argc, char** argv)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    REP(t, 1, T + 1)
    {
        cout << "Case #" << t << ": ";
        unsigned long long int n;
        int bDigit[10] = { 0 };
        unsigned long long int iCounter = 1;
        int digitCounter = 0;
        cin >> n;

        if(n == 0) {
            cout << "INSOMNIA";
        } else {
            while(digitCounter != 10) {
                unsigned long long int iModulo, iTemp;
                iTemp = n * iCounter;
                iCounter++;
                while(iTemp != 0) {
                    iModulo = iTemp % 10;
                    iTemp = iTemp / 10;
                    if(bDigit[iModulo] == 0) {
                        bDigit[iModulo] = 1;
                        digitCounter++;
                    }
                }
            }
            cout << n * (iCounter - 1);
        }
        cout << endl;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
