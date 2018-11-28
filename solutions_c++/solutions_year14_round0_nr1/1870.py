#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

void read(vector<int> &row) {
    int r;
    cin >> r;
    --r;
    for (int i = 0; i < 16; ++i) {
        int a;
        cin >> a;
        if (i >= r*4 && i < r*4 + 4) row.push_back(a);
    }
}

string calc()
{
    vector<int> row;
    read(row);
    read(row);

    /*
    for (int i = 0; i < row1.size(); ++i) {
        cerr << row1[i] << ' ';
    }
    cerr << endl;
    */

    vector<int> num(17, 0);
    int two = -1;
    for (int i = 0; i < row.size(); ++i) {
        num[row[i]]++;
        if (num[row[i]] == 2) {
            if (two != -1) {
                return "Bad magician!";
            }
            two = row[i];
        }
    }

    if (two == -1) {
        return "Volunteer cheated!";
    }

    stringstream ss;
    ss << two;
    return ss.str();
}

int main(void)
{
	int T;
	cin >> T;
	//getline(cin, line);
	for (int ca=1; ca<=T; ++ca) {
		//getline(cin, line);
		cout << "Case #" << ca << ": " << calc() << endl;
	}
	return 0;
}
