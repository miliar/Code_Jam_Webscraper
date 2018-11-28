#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
using namespace std;

set<int> read_line(int number)
{
    set<int> result;
    int curr;

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> curr;
            if (i == number) {
                result.insert(curr);
            }
        }
    }

    return result;
}

int main(int argc, char **argv)
{
    int ncases;
    cin >> ncases;

    for (int i = 0; i < ncases; ++i) {
        int first;
        cin >> first;
        auto one = read_line(first-1);
        
        int second;
        cin >> second;
        auto two = read_line(second-1);

        vector<int> result;
        set_intersection(one.begin(), one.end(), two.begin(), two.end(),
            back_inserter(result));

        cout << "Case #" << i+1 << ": ";
        if (result.size() == 1) {
            cout << result[0] << endl;
        } else if (result.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        } else {
            cout << "Bad magician!" << endl;
        }
    }
}