#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>


using namespace std;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef pair<unsigned,unsigned> uu;
typedef pair<ull,ull> ullull;

/*
1 -> E
2 -> F
3 -> G
4 -> H
5 -> I
6 -> N
7 -> O
8 -> R
9 -> S
10-> T
11-> U
12-> V
13-> W
14-> X
15-> Z
*/


char digit_letter[] = {
    'Z',
    'O',
    'W',
    'H',
    'U',
    'F',
    'X',
    'V',
    'G',
    'I'
}
    ;

string names[] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
}
    ;


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    ull T;
    cin >> T;
    for(ull t=1; t<=T; ++t) {
        string s;
        cin >> s;

        vector<int> digits(10);
        vector<int> letters(256);

//        cerr << "string: " << s << "\n";
        
        
        for(auto c : s)
            letters[c]++;

        for(int i=0; i<10; i+=2) {
            digits[i] = letters[digit_letter[i]];
//            cerr << "Found: " << digits[i]
//                 << " instances of " << i << "\n";
            
            for(auto c : names[i]) {
                letters[c] -= digits[i];
            }
        }

        for(int i=1; i<10; i+=2) {
            digits[i] = letters[digit_letter[i]];
//            cerr << "Found: " << digits[i]
//                 << " instances of " << i << "\n";
            for(auto c : names[i]) {
                letters[c] -= digits[i];
            }
        }
        
        cout << "Case #" << t << ": ";
        for(int d=0; d<10; ++d) {
            for(int k=0; k<digits[d]; ++k)
                cout << d;
        }
        
        cout << "\n";
    }
    cout << flush;
}
