#include <iostream>
#include <vector>

using namespace std;

vector<uint64_t> solveInstance(int K, int C, int S);

vector<int> getEmptyLocation(int K, int C);

void getNextLocation(vector<int> &currentLocation, int K, int C);

uint64_t locationToIndex(const vector<int> &loc, int K);

int main() {
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        int K = 0, C = 0, S = 0;
        cin >> K >> C >> S;
        vector<uint64_t> v = solveInstance(K,C,S);
        if(v.size() == 0){
            cout << "Case #" << i << ": IMPOSSIBLE"<< endl;
        } else {
            cout << "Case #" << i << ": ";
            for (int i = 0, s = v.size(); i < s; ++i){
                cout << v[i] + 1;
                if(i != (s-1)){
                    cout << ' ';
                }
            }
            cout << endl;
        }
    }
    return 0;
}

vector<uint64_t> solveInstance(int K, int C, int S){
    vector<uint64_t> solution = vector<uint64_t>();
    if(K > (S*C)){
        return solution;
    }

    vector<int> currentLocation = getEmptyLocation(K, C);
    while(currentLocation.size() != 0){
        solution.push_back(locationToIndex(currentLocation, K));
        getNextLocation(currentLocation, K, C);
    };

    return solution;
}

vector<int> getEmptyLocation(int K, int C){
    vector<int> loc = vector<int>();
    //cout<< "K = " << K << " C = " << C <<": ";
    for (int i = 0; (i < C) && (i < K); i++){
        loc.push_back(i);
        //cout << i << ' ';
    }
    //cout << endl;
    return loc;
}
uint64_t locationToIndex(const vector<int> & loc, int K){
    uint64_t index = 0;
    for(int i : loc){
        index = index*(uint64_t)K + i;
    }
    return index;
}

void getNextLocation(vector<int> & currentLocation, int K, int C){
    if(currentLocation.size() == 0){
        return;
    } else {
        int curr = currentLocation[currentLocation.size() - 1] + 1;
        currentLocation.clear();
        for (int i = 0; (curr < K) && (i < C); i++, curr++){
            //cout << curr << ' ';
            currentLocation.push_back(curr);
        }
        //cout << endl;
    }
}