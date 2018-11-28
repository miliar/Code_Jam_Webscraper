#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

void work() {
    int row1, row2;
    set<int> row1Cards;
    set<int> row2Cards;
    set<int> intersection;
    cin >> row1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int card;
            cin >> card;
            if (i + 1 == row1)
                row1Cards.insert(card);
        }
    }
    cin >> row2;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int card;
            cin >> card;
            if (i + 1 == row2)
                row2Cards.insert(card);
        }
    }
    set_intersection(row1Cards.begin(), row1Cards.end(),
                     row2Cards.begin(), row2Cards.end(),
                     std::inserter(intersection, intersection.begin()));
    if (intersection.size() == 0)
        cout << "Volunteer cheated!" << endl;
    else if (intersection.size() == 1) 
        cout << *intersection.begin() << endl;
    else
        cout << "Bad magician!" << endl;
}

int main(void) {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        cout << "Case #" << i << ": ";
        work();
    }
    return 0;
}