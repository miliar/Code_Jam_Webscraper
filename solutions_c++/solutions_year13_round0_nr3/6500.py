#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool v[1008];

bool is_square(int x) {
    float root = sqrt(x);

    return (root == ceil(root));
}

bool is_palindrom(int x) {
    int rev = 0, aux = x;
    while(aux) {
        rev = rev * 10 + aux % 10;
        aux /= 10;

    }
    return rev == x;
}

void solve() {
    int T, A, B, count = 0;
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    fin >> T;
    for(int i = 0; i < T; ++i) {
        fin >> A >> B;
        count = 0;
        for(int k = A; k <= B; ++k) {
            if(is_square(k) && is_palindrom(k)) {
                float root = sqrt(k);
                if(is_palindrom(root))
                    count++;

            }

        }
        fout << "Case #" << i + 1 << ": " << count << "\n";
    }
}


int main() {
    solve();

    return 0;
}
