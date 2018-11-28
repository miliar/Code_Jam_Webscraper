#include <iostream>
#include <fstream>
#include <vector>

#define DEBUG 1
#define TYPE uint64_t

using namespace std;

void helper(char c, int pos, string word, vector<int>& table, vector<int>& res){
    int val;
    val = table[c - 'A'];
    res[pos] += val;
    for(char ch : word)
        table[ch - 'A'] -= val;
}

int main() {
#ifdef DEBUG
    string infile ="A-large.in";
    string outfile ="A-large.out";

    ifstream in(infile);
    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to input.txt

    std::ofstream out(outfile);
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

    TYPE T,i, eight,zero;
    vector<int> table(26);
    vector<int> res(10);
    string s;
    cin >> T;

    for(i = 1; i <= T; ++i){
        std::fill(table.begin(), table.end(), 0);
        std::fill(res.begin(), res.end(), 0);

        cin >> s;
        for(char c : s){
            table[c - 'A']++;
        }

        helper('G', 8, "EIGHT", table, res);
        helper('Z', 0, "ZERO", table, res);
        helper('W', 2, "TWO", table, res);
        helper('U', 4, "FOUR", table, res);
        helper('X', 6, "SIX", table, res);
        helper('R', 3, "THREE", table, res);
        helper('O', 1, "ONE", table, res);
        helper('S', 7, "SEVEN", table, res);
        helper('V', 5, "FIVE", table, res);
        helper('I', 9, "NINE", table, res);

        cout << "Case #"<< i <<": ";

        for(int j = 0 ; j < 10 ; ++j){
            for(int k = 0 ; k < res[j] ; ++k){
                cout << j;
            }
        }

        cout << endl;
    }
#ifdef DEBUG
    cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
#endif

    return 0;
}