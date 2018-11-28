#include <iostream>
#include <string>
#include <sstream>
#include <set>
using namespace std;

void print_set(int max, set<char> group_counts[1100]) {
    for(int i = 0; i < max; ++i) {
        cout << i << ":" ;
        for (auto it = group_counts[i].begin(); it != group_counts[i].end(); ++it) {
            cout << *it;
        }
        cout << endl;
    }
}

int main() {
    int t;
    cin >> t;
    string output = "";
    for (int round = 1; round <= t; ++round) {
        int max = 0;
        int total = 0;
        set<char> group_counts[1100];
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            int count = 0;
            cin >> count;
            if (count > max) {
                max = count;
            }
            total += count;
            group_counts[count].insert('A' + i);
        }
//        print_set(max, group_counts);
        cout << "Case #" << round << ": "; 

        int printed = 0;
        while(max > 0) {
            if (group_counts[max].size() == 0){
                max--;
                continue;
            }
            char tar = *group_counts[max].begin();
            total--;
            if(group_counts[max].size() == 2) {
                if (printed > 0){
                if (max > total / 2) {
                    cout << " ";
                    printed = 0;
                }
                }
            }
            if (printed == 2) {
                cout << " ";
                printed = 0;
            }
            cout << tar;
            printed++;

            group_counts[max].erase(tar);
            group_counts[max - 1].insert(tar);
        }
        cout << endl;
    }
return 0;
}
