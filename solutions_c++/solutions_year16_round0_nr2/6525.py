#include <bits/stdc++.h>

using namespace std;


int main() {

    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    int t;
    string seq;
    cin >> t;

    for(int ti = 1; ti <= t; ti++){

        cin >> seq;

        int flips = 0;

        for(int i = 0; i < seq.size() - 1; i++){

            if (seq[i] != seq[i + 1]) flips++;
        }

        if(seq[seq.size() - 1] == '-') flips++;


        cout <<"Case #"<< ti <<": " << flips<<"\n";
    }

    return 0;
}

