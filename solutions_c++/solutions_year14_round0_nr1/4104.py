#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

string doIt(vector< vector<int> > config1, vector< vector<int> > config2, int ans1, int ans2) {
    --ans1, --ans2;
    int answer;
    bool found1 = false;
    int potential[4];
    for (int i=0; i<4; ++i) {
        potential[i] = config1[ans1][i];
    }

    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            if (potential[j] == config2[ans2][i]) {
                answer = potential[j];
                if (!found1) {
                    found1 = true;
                }
                else {
                    return "Bad magician!";
                }
            }

        }
    }
    char buff[100];
    if (!found1) {
        return "Volunteer cheated!";
    }
    else {
        sprintf(buff, "%d", answer);
        return buff;
    }
}

int main() {
    int T;
    int ans1, ans2;
    vector< vector<int> > config1(4, vector<int>(4));
    vector< vector<int> > config2(4, vector<int>(4));

    cin >> T;

    for (int num = 0; num < T; ++num) {
        cin >> ans1;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                scanf("%d", &config1[i][j]);
            }
        }
        cin >> ans2;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                scanf("%d", &config2[i][j]);
            }
        }
        cout << "Case #" << num+1 << ": " << doIt(config1,config2,ans1,ans2) << endl;
    }


        


    return 0;
}
