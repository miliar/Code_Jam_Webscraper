#include "1a.h"
#include <set>

using namespace std;

void read_card(set<int> &result){
    int row;
    cin >> row;
    for (int m=0; m<4; m++) {
        for (int n=0; n<4; n++) {
            int x;
            cin >> x;
            if (m+1 == row) {
                result.insert(x);
            }
        }
    }
}

void read_card(set<int> &result, set<int> &result2){
    int row;
    cin >> row;
    for (int m=0; m<4; m++) {
        for (int n=0; n<4; n++) {
            int x;
            cin >> x;
            if (m+1 == row && result.find(x)!= result.end()) {
                result2.insert(x);
            }
        }
    }
}


void check(set<int> &result){
    if (result.empty()) {
        cout << "Volunteer cheated!" << endl;
    } else if (result.size() > 1){
        cout << "Bad magician!" << endl;
    } else {
        cout << *result.begin() << endl;
    }
}


int main(){
    
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        set<int> result1, result2;
        read_card(result1);
        read_card(result1, result2);
        cout << "Case #" << i+1 << ": ";
        check(result2);
        result1.clear();
        result2.clear();
    }
    
    
}