#include <bits/stdc++.h>

#define cin fin
#define cout fout

using namespace std;

int T, N, K;
string S;
int minmoves;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

bool iscorrect() {
    for (int i=0; i<S.size(); i++)
        if (S[i] != '+')
            return false;
    return true;
}

int main()
{
    cin >> T;

    for (int caseno=1; caseno<=T; caseno++) {
        cin >> S >> K;
        minmoves = 0;
        N = S.size();

        for (int i=0; i<=N-K; i++) {
            if (S[i] == '-') {
                minmoves ++;
                for (int j=0; j<K; j++)
                    S[i+j] = (S[i+j] == '+' ? '-' : '+');
            }
        }

        cout << "Case #" << caseno << ": ";
        if (iscorrect())
            cout << minmoves << endl;
        else cout << "IMPOSSIBLE\n";
    }


    return 0;
}
