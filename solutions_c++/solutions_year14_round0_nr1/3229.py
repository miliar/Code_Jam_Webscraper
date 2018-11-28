#include <iostream>
#include <set>
#include <vector>

using namespace std;

int first(set<int> s) {
    set<int>::const_iterator it;
    for (it = s.begin(); it != s.end(); ++it) {
        return (*it);
    }
    return -1;
}
set<int> set_intersection(set<int> l1, set<int> l2) {
    set<int> inter;
    set<int>::const_iterator it;
    for (it = l1.begin(); it != l1.end(); ++it) {
        if(l2.count((*it)) > 0) {
            inter.insert((*it));
        }
    }
    return inter;
}
int main(int argc, const char * argv[])
{
    int nb_examples;
    cin >> nb_examples;
    for(int nb = 1; nb <= nb_examples; nb++) {
        int first_r, second_r, x;
        vector<set<int>> table1(4);
        vector<set<int>> table2(4);
        cin >> first_r;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> x;
                table1[i].insert(x);
            }
        }
        cin >> second_r;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> x;
                table2[i].insert(x);
            }
        }
        set<int> inter = set_intersection(table1[first_r-1], table2[second_r-1]);
        cout << "Case #" << nb << ": ";
        if(inter.empty()) {
            cout << "Volunteer cheated!" << endl;
        }
        else if(inter.size() > 1) {
            cout << "Bad magician!" << endl;
        }
        else {
            cout << first(inter) << endl;
        }
    }
}

