#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;

const char FACE[2] = {'-','+'};
const int HAPPY = 1;
const int BLANK = 0;

class B {

private:
    string S;

public:
    void init() {
        cin >> S;
    }
    
    void solution(int x) {
        cout << "Case #" << x << ": ";

        cout << find(S,findLastBlank(S),HAPPY);

        cout << endl;
    }

    int find(string S, int from, int fi) {
        int ret;
        
        if ( from == -1 ) {
            ret = 0;
        }
        else {
            int i;
            for ( i = from; i >= 0; --i ) {
                if ( S[i] == FACE[fi] )
                    break;
            }
            ret= 1 + find(S,i,(fi+1)%2);
        }

        return ret;
    }

    int findLastBlank(const string& S) {
        int len = S.length();
        int i;
        for ( i = len-1; i >= 0; --i ) {
            if ( S[i] == FACE[BLANK] ) break;
        }
        return i;
    }
};

int main() {
    int T;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> T;

    for ( int i = 1; i <= T; ++i ) {
        B sol;
        sol.init();
        sol.solution(i);
    }
}
