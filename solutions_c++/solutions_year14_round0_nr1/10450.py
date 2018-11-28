#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

using namespace std;
set<int> set1, set2;
int main() {

    int test, a, b, x, kase=1;
    cin >> test;
    while (test--) {
        set1.erase(set1.begin(), set1.end());
        set2.erase(set2.begin(), set2.end());
        cin >> a;
        for (int i=0 ; i<4 ; i++) {
            for (int j=0 ; j<4 ; j++) {
                cin >> x;
                if (i==a-1) {
                    set1.insert(x); 
                }
            }
        }
        cin >> b;
        for (int i=0 ; i<4 ; i++) {
            for (int j=0 ; j<4 ; j++) {
                cin >> x;
                if (i==b-1) {
                    set2.insert(x); 
                }
            }
        }
        vector<int> common;
        for (set<int>::iterator i=set1.begin() ; i!=set1.end() ; i++) {
            int v = (*i);
            if (set2.count(v)>0) {
                common.push_back(v);
            }
        }

        cout << "Case #" << kase++ <<": ";
        switch(common.size()) {
            case 1:
                cout << common[0] << endl;
                break;
            case 0:
                cout << "Volunteer cheated!" << endl;
                break;
            default:
                cout << "Bad magician!" << endl;
                break;
        }
    }

    return 0;
}
