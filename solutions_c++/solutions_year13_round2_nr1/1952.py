#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

ll motes[109];

ll best[109];
ll moves[109];

ll solve(ll A, ll N){
    ll ans = 0;

    sort(motes, motes + N);

    ll _A = A;
    ll eaten = 0;

    //greedy
    for (int j = 1; j < N; j++){
        if (_A - 1 <= 0){

            continue;
        }

        while(_A < motes[j]){
            _A += _A - 1;
            eaten++;
        }

        _A += motes[j];

        best[j] = _A;
    }

}


int main(){

    ifstream in("A-small-attempt1.in");
    ofstream out("A-small-attempt1.out");

    //ifstream in("in.txt");
    //ofstream out("out.txt");

    int T, t;
    in >> T;

    for (t = 1; t <= T; t++ ){
        //input
        ll A;
        in >> A;

        int N;
        in >> N;

        for (int i = 0; i < N; i++){
            in >> motes[i];
        }

        ll ans = solve(A, N);

        out << "Case #" << t << ": " << ans << endl;
        cout << "Case #" << t << ": " << ans << endl;
    }



    in.close();
    out.close();

    return 0;
}
