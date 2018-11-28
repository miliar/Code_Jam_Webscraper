#include<iostream>
#include<string.h>
using namespace std;

main() {
    int t;
    cin >> t;

    for (int T=1 ; T<=t; T++) {
        string s;
        cin >> s;
        int len = s.length();

        int ans[10];
        for (int i=0 ; i<10 ; i++)
            ans[i] = 0;

        int alph[91];
        for (int i='A' ; i<='Z' ; i++)
            alph[i] = 0;

        for (int i=0 ; i<len ; i++)
            alph[s[i]]++;

        string word[] = {"ZERO", "TWO", "EIGHT", "SIX", "SEVEN", "FIVE", "FOUR", "THREE", "NINE", "ONE"};
        int num[] = {0, 2, 8, 6, 7, 5, 4, 3, 9, 1};
        char check[] = {'Z', 'W', 'G', 'X', 'S', 'V', 'F', 'T', 'I', 'O'};
        for (int i=0 ; i<10 ; i++) {
            int n = alph[check[i]];
            ans[num[i]] += n;
            for (int j=0 ; j<word[i].length() ; j++)
                alph[word[i][j]] -= n;
        }

        cout << "Case #" << T << ": ";
        for (int i=0 ; i<10 ; i++) {
            for (int j=0 ; j<ans[i] ; j++)
                cout << i;
        }
        cout << endl;
    }
}
