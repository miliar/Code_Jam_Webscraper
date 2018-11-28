#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int testcase(0); testcase != t; ++testcase) {
        cout << "Case #" << testcase + 1 << ": ";
        int a1;
        cin >> a1;
        set<int> feasible1;
        for(int i(0); i != 4; ++i) {
            for(int j(0); j != 4; ++j) {
                int temp;
                cin >> temp;
                if(i == a1 - 1) {
                    feasible1.insert(temp);
                }
            }
        }
        int a2;
        cin >> a2;
        set<int> feasible2;
        for(int i(0); i != 4; ++i) {
            for(int j(0); j != 4; ++j) {
                int temp;
                cin >> temp;
                if(i == a2 - 1) {
                    feasible2.insert(temp);
                }
            }
        }
        set<int> feasible;
        set_intersection(feasible1.begin(),feasible1.end(),feasible2.begin(),feasible2.end(),
                         std::inserter(feasible,feasible.begin()));
        if(feasible.size() == 1) {
            cout << *feasible.begin() << endl;
        } else if (feasible.size() == 0) {
            cout << "Volunteer cheated!" << endl;         
        } else {
            cout << "Bad magician!" << endl;
        }

        
    }
}
