#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for(int i = int(a); i < int(b); i++)

int main(int argc, char** argv)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int N, T, i;

    string str;

    string number[] = { "ZERO", "TWO", "FOUR", "SIX", "EIGHT", "THREE", "SEVEN", "FIVE", "NINE", "ONE" };

    char condition[] = { 'Z', 'W', 'U', 'X', 'G', 'H', 'S', 'F', 'I', 'O' };

    int numIndex[] = { 0, 2, 4, 6, 8, 3, 7, 5, 9, 1 };

    cin >> T;

    REP(i, 1, T + 1)
    {
        int arr[26] = { 0 };

        int num[10] = { 0 };

        cout << "Case #" << i << ": ";
        int j, k;

        cin >> str;

        for(j = 0; j < str.length(); j++) {
            arr[str[j] - 'A']++;
        }

        for(j = 0; j < 10; j++) {
            int iTemp = arr[condition[j] - 'A'];
            num[numIndex[j]] = iTemp;
            string strTemp = number[j];
            for(k = 0; k < strTemp.length(); k++) {
                arr[strTemp[k] - 'A'] -= iTemp;
            }
        }

        for(j = 0; j < 10; j++) {
            for(k = 0; k < num[j]; k++) {
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}
