
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector< pair< vector<long long>, vector<long long> > > all;

bool is_prime(long long x) {
    for(int i = 2; i * 1ll * i <= x; i++) {
        if(x % i == 0)
            return false;
    }
    return true;
}

long long get_witness(long long x) {
    for(int i = 2; i * 1ll * i <= x; i++) {
        if(x % i == 0)
            return i * 1ll;
    }
    return 0;
}

void backtrack(vector<long long> &A, int n, int j) {
    if((int)all.size() == j)
        return;

    if((int)A.size() == n - 2) {

        vector<long long> B = A;
        B.push_back(1);
        reverse(B.begin(), B.end());
        B.push_back(1);



        vector<long long> witnesses;

        for(int b = 2; b <= 10; b++) {
            long long number = 0;
            long long shift = 0;
            long long b_pw = 1;
            for(int i = 0; i < n; i++) {
                number += (B[i] * b_pw);
                b_pw *= b;
            }

            if(is_prime(number))
                return;
            witnesses.push_back(get_witness(number));
        }

        if((int)all.size() < j) {
            int m = (int)B.size();
            for(int i = 0; i < m; i++)
                B.push_back(B[i]);

            reverse(B.begin(), B.end());
            all.push_back({B, witnesses});
        }
    }
    else {
        A.push_back(0); backtrack(A, n, j);
        A.pop_back();
        A.push_back(1); backtrack(A, n, j);
        A.pop_back();
    }
}

int main( void ) {

    freopen("input_c.txt", "r", stdin);
    freopen("output_c.txt", "w", stdout);

    int t;
    cin >> t;

    for(int tt = 1; tt <= t; tt++) {
        printf("Case #%d:\n", tt);

        int n, j;
        cin >> n >> j;

        vector<long long> binary;

        all.clear();
        backtrack(binary, n / 2, j);

        for(auto solution: all) {
            for(auto bit: solution.first)
                cout << bit;
            for(auto witness: solution.second)
                cout << " " << witness;
            cout << endl;
        }
    }
    return 0;
}

