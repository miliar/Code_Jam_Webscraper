#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

string solve(){
    int line;
    int A, B, C, D;
    vector<int> a, b;

    // process first set of possible numbers
    cin >> line;
    for (int i = 0; i < 4; i++) {
        cin >> A >> B >> C >> D;
        if (line == (1+i)) {
            a.push_back(A);
            a.push_back(B);
            a.push_back(C);
            a.push_back(D);
        }
    }

    // check intersection of previous list
    cin >> line;
    for (int i = 0; i < 4; i++) {
        cin >> A >> B >> C >> D;
        if (line == (1+i)) {
            b.push_back(A);
            b.push_back(B);
            b.push_back(C);
            b.push_back(D);
        }
    }

    int intersect = 0, match;
    for (int i : a) {
        for (int j : b) {
            if (i == j) {
                match = i;
                intersect++;
                //cout << "i: " << i << " j: " << j << endl;
            }
        }
    }

    string answer;
    switch (intersect) {
        case 0:
            answer.assign("Volunteer cheated!");
            break;
        case 1:
            answer.assign(to_string(match));
            break;
        default:
            answer.assign("Bad magician!");
            break;
    }
    return answer;
}

int main()
{
    int T, prob = 1;
    for(cin >> T; T--;)
    {
        printf("Case #%d: %s\n", prob++, solve().c_str());
    }
    return 0;
}

