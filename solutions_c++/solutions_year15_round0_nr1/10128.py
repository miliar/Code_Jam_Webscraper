#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;
//Samir Musali

vector<int> inttodigits(int num, int dignum);
int numneeded(vector<int> S, int num);

vector<int> inttodigits(int num, int dignum){
    vector<int> revresult, result;
    int cur = num, dnum = dignum;
    while (dignum > 0) {
        int ready = cur%10;
        cur = cur/10;
        revresult.push_back(ready);
        dignum--;
    }
    for (int i = 0; i < dnum; i++) {
        result.push_back(revresult[dnum-i-1]);
    }
    return result;
}

int numneeded(vector<int> S, int num){
    int result = 0, psum = 0;
    for (int i = 0; i < num; i++) {
        if (psum < i) {
            int diff = i-psum;
            result += diff;
            psum += diff;
        }
        psum += S[i];
    }
    return result;
}

int main(void){
    int testnum = 0;
    cin >> testnum;
    for (int i = 1; i <= testnum; i++){
        int levnum = 0, in = 0;
        cin >> levnum;
        cin >> in;
        vector<int> ready = inttodigits(in,levnum+1);
        int res = numneeded(ready, levnum+1);
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
