//
// Google Code Jam 2014
// Qualification Round
// Problem A: Magic Trick
//

#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

void testcase()
{
    int row;
    int tmp;
    vector<int> first(4);
    vector<int> second(4);
    cin >> row;

    for (int i = 1; i <= 4; i++) {
	if (i == row) {
	    for (int j = 0; j < 4; j++) {
		cin >> first[j];
	    }
	} else {
	    for (int j = 1; j <= 4; j++) {
		cin >> tmp;
	    }
	}
    }

    cin >> row;
    for (int i = 1; i <= 4; i++) {
	if (i == row) {
	    for (int j = 0; j < 4; j++) {
		cin >> second[j];
	    }
	} else {
	    for (int j = 1; j <= 4; j++) {
		cin >> tmp;
	    }
	}
    }

    sort(first.begin(), first.end());
    sort(second.begin(), second.end());

    vector<int> inters;
    set_intersection(first.begin(), first.end(), second.begin(), second.end(), back_inserter(inters));

    if (inters.size() == 1) {
	cout << inters[0] << endl;
    } else if (inters.size() == 0) {
	cout << "Volunteer cheated!" << endl;
    } else {
	cout << "Bad magician!" << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);

    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++) {
	cout << "Case #" << i << ": ";
	testcase();
    }
}
