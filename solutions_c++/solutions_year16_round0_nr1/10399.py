#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin;
ofstream fout;

void solve(uint64_t T) {
    uint64_t N;
    fin >> N;
    uint64_t seen = 0b0000000000;
    uint64_t i = 1;
    uint64_t n;
    bool insomnia = false;
    vector<uint64_t> results;
    while(true) {
        n = i * N;
        if(find(results.begin(), results.end(), n) == results.end()) {
            results.push_back(n);
            uint64_t _n = n;
            while(_n) {
                uint64_t digit = _n % 10;
                seen |= 1 << digit;
                _n /= 10;
            }
            if(seen == 0b1111111111) {
                break;
            }
        }
        else {
            insomnia = true;
            break;
        }
        i++;
    }
    fout << "Case #" << (T + 1) << ": ";
    if(insomnia) {
        fout << "INSOMNIA" << endl;
    }
    else {
        fout << n << endl;
    }
}

int main()
{
    fin.open("input.txt");
    fout.open("output.txt");
    uint64_t T;
    fin >> T;
    for(uint64_t i = 0; i < T; i++) {
        solve(i);
    }
    fout.close();
    fin.close();
    return 0;
}
