#include <iostream>
#include <fstream>
#include <unordered_set>

#define DEBUG 1
#define TYPE uint64_t

using namespace std;

int main() {

    string infile ="B-large.in";
    string outfile ="B-large.out";

    ifstream in(infile);
    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to input.txt

#ifdef DEBUG
    std::ofstream out(outfile);
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

    TYPE T,i,j,n,ans;
    cin >> T;
    string s;

    for(i = 1; i <= T; ++i){
        cin >> s;
        n = s.length();
        ans= 0;
        for(j = 0 ; j < n - 1; ++j){
            if(s[j] != s[j+1])++ans;
        }
        if(s[j] == '-')++ans;

        cout << "Case #"<< i <<": " << ans << endl;
    }
    cin.rdbuf(cinbuf);   //reset to standard input again

#ifdef DEBUG
    std::cout.rdbuf(coutbuf); //reset to standard output again
#endif

    return 0;
}