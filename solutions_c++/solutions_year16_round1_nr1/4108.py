#include <iostream>

using namespace std;

void reorganising(string & table)
{
    for(int i = table.size(); i > 0; i--)
    {
        table[i] = table[i-1];
    }
}

int main()
{
    int wordsCounter = 0;
    int t;
    cin >> t;
    string S;
    for(int i = 0; i < t; i++)
    {
        string table;
        cin >> S;
        char left, right;
        left = S[0];
        right = S[0];
        table += S[0];
        wordsCounter++;

        for(int j = 1; j < S.size(); j++)
        {
            if(S[j] < right)
            {
                right = S[j];
                table += S[j];
                wordsCounter++;
            } else if(S[j] < left)
            {
                right = S[j];
                table += S[j];
                wordsCounter++;
            } else {
                left = S[j];
                table += ' ';
                reorganising(table);
                table[0] = S[j];
                wordsCounter++;
            }
        }

        cout << "Case #" << i+1 << ": " << table << endl;
    }
    return 0;
}
