#include <iostream>
#include <vector>
using namespace std;
int f, s;
vector<int> fv, sv;
void input() {
    fv.clear(); sv.clear();
    int temp;

    cin >> f;
    for(int i = 1; i <= 4; i++) {
        for(int j = 0; j < 4; j++) {
            cin >> temp;
            if(i == f) {
                fv.push_back(temp);
            }
        }
    }

    cin >> s;
    for(int i = 1; i <= 4; i++) {
        for(int j = 0; j < 4; j++) {
            cin >> temp;
            if(i == s) {
                sv.push_back(temp);
            }
        }
    }
}

int main() {
    int T; cin >> T;
    for(int t = 1; t <= T; t++) {
        input();
        int ret = 0, ans;
        for(vector<int>::iterator it_f = fv.begin(); it_f != fv.end(); ++it_f)
            for(vector<int>::iterator it_s = sv.begin(); it_s != sv.end(); ++it_s)
                if(*it_s == *it_f) {ret++; ans = *it_s;}

        if(ret == 1) {
            cout << "Case #" << t << ": " << ans << endl;
        }else if(ret == 0) {
            cout << "Case #" << t << ": Volunteer cheated!" << endl;
        }else {
            cout << "Case #" << t << ": Bad magician!" << endl;
        }
    }
    return 0;
}
