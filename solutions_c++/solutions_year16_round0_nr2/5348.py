#include<iostream>

using namespace std;

int main() {
    int nCases, i = 1;
    cin >> nCases;
    while(getchar() != '\n');
    while(nCases--) {
        char c, curr = 'Y';
        int nMoves = 0;
        while((c = getchar()) != '\n' && (c == '-' || c == '+')) {
            if(curr == 'Y')
                curr = c;
            else {
                if(c != curr)
                    nMoves++;
                curr = c;
            }
        }
        if(curr == '-')
            nMoves++;
        cout << "Case #" << i++ << ": " << nMoves << endl;
    }
    return 0;
}