#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int t, letter[1000], num[100];

void remove_letter(int n, string s, char c){
    num[n] = letter[c];
    for (int i=0; i<s.size(); i++)
        letter[s[i]] -= num[n];
}

int main(){
    string s;

    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        cin >> s;

        for (int i='A'; i<='Z'; i++)
            letter[i] = 0;
        for (int i=0; i<=9; i++)
            num[i] = 0;

        for (int i=0; i<s.size(); i++)
            letter[s[i]]++;

        remove_letter(0, "ZERO", 'Z');
        remove_letter(6, "SIX", 'X');
        remove_letter(4, "FOUR", 'U');
        remove_letter(5, "FIVE", 'F');
        remove_letter(2, "TWO", 'W');
        remove_letter(1, "ONE", 'O');
        remove_letter(7, "SEVEN", 'S');
        remove_letter(3, "THREE", 'R');
        remove_letter(8, "EIGHT", 'T');
        remove_letter(9, "NINE", 'I');

        printf ("Case #%d: ", k);
        for (int i=0; i<10; i++){
            for (int j=0; j<num[i]; j++)
                cout << i;
        }
        cout << endl;
    }

    return 0;
}
