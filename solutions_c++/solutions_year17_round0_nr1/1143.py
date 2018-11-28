#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
    int T, K;
    vector<bool> p;
    cin >> T; //Test cases
    for(int t = 0; t < T; t++) {
        cin >> ws; //New line
        string temp;
        cin >> temp;
        p.clear();
        for(char &c : temp) {
            //Happy = 1, Sad = 0
            p.push_back(c == '+');
        }

        cin >> ws; //Space
        cin >> K; //Paddle size
        bool success = true;
        int flips = 0;
        int L = p.size();
        for(int l = 0; l < L; l++) {
            //If current element is not in order
            if(!p[l]) {
                //And we can do a flip
                if(l + K <= L) {
                    //Flip!
                    for(int k = 0; k < K; k++) {
                        p[l+k] = !p[l+k];
                    }
                    flips++;
                } else {
                    success = false;
                    break;
                }
            }
        }
        cout << "Case #" << (t+1) << ": ";
        if(success) {
            cout << flips;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
}
