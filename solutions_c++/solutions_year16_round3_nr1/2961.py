#include <bits/stdc++.h>
using I64 = long long;
using U64 = unsigned long long;
using namespace std;
#define FOR(i, n) for(size_t i = 0; i < n; ++i)
#define FOR1(i, n) for(size_t i = 1; i < n; ++i)
#define FORN(i, M, n) for(size_t i = M; i < n; ++i)
U64 senators[30];
I64 N;
bool done(){
    FOR(i, N){
        if (senators[i] != 0)
            return false;
    }

    return true;
}
bool check(){
    I64 cur = senators[0];
    bool ok = false;
    FOR1(i, N){
        if (senators[i] == cur)
            ok = true;
        else if (senators[i] > cur){
            cur = senators[i];
            ok = false;
        }
    }

    return ok;
}
int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    assert(in.is_open() && out.is_open());
    U64 T;
    in >> T;
    FOR(test, T){

        in >> N;
        FOR(i, N)
            in >> senators[i];

        cout << "Case #" << test + 1 << ": ";
        out << "Case #" << test + 1 << ": ";
        while(!done()) {

            FOR(i, N) {
                if (senators[i] == 0)
                    continue;

                bool found = false;
                senators[i]--;
                if (check()) {
                    cout << char(i + 65) << " ";
                    out << char(i + 65) << " ";
                    found = true;
                    break;
                } else {
                    FORN(j, i + 1, N) {
                        if (senators[j] == 0)
                            continue;

                        senators[j]--;
                        if (check()) {
                            cout << char(i + 65) << char(j + 65) << " ";
                            out << char(i + 65) << char(j + 65) << " ";
                            found = true;
                            break;
                        } else
                            senators[j]++;
                    }
                }
                if (!found) {
                    senators[i]--;
                    if (check()) {
                        cout << char(i + 65) << char(i + 65) << " ";
                        out << char(i + 65) << char(i + 65) << " ";
                        found = true;
                    }
                }
                if (!found)
                    senators[i] += 2;
            }
        }



        cout << "\n";
        out << "\n";
    }
    return 0;
}