#include <iostream>
#include <fstream>
#include <unordered_set>

#define DEBUG 1
#define TYPE uint64_t

using namespace std;

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

    TYPE T,N,i,n,m;
    unordered_set<TYPE> s;
    cin >> T;

    for(i = 1; i <= T; ++i){
        s.clear();
        cin >> N; cout << "Case #"<< i <<": ";
        if(N == 0) {cout << "INSOMNIA" << endl;
            continue;
        }
        n = N;


        while(s.size() < 10) {
            m = n;
            while (n > 0) {
                s.insert(n % 10);
                n = n / 10;
            }
            n = m + N;
        }
        cout << n - N;

        cout << endl;
    }
#ifdef DEBUG
    cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
#endif

    return 0;
}