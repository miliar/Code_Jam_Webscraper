#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    ifstream in("in.txt");
    if (!in.is_open()) {
        cerr << "File not opened\n";
        return -1;
    }
    int T = 0;
    in >> T;
    for (int i = 0; i < T; i++) {
        int firstReply = 0;
        in >> firstReply;
        vector<int> firstArea;
        for (int j = 0; j < 16; j++) {
            int tmp;
            in >> tmp;
            firstArea.push_back(tmp);
        }
        int secondReply = 0;
        in >> secondReply;
        vector<int> secondArea;
        for (int j = 0; j < 16; j++) {
            int tmp;
            in >> tmp;
            secondArea.push_back(tmp);
        }
        vector<int> firstRow(4);
        for (int i2 =0; i2<4;i2++) {
            firstRow[i2] = firstArea[(firstReply-1)*4+i2];
        }
        vector<int> secondRow(4);
        for (int i2 =0; i2<4;i2++) {
            secondRow[i2] = secondArea[(secondReply-1)*4+i2];
        }
        sort(firstRow.begin(), firstRow.end());
        sort(secondRow.begin(), secondRow.end());
        vector<int> intersect(16);
        vector<int>::iterator it;
        it = set_intersection(firstRow.begin(), firstRow.end(), secondRow.begin(), secondRow.end(), intersect.begin());
        intersect.resize(it - intersect.begin());
        cout << "Case #" << i+1 << ": ";
        if (intersect.size() > 1) {
            cout << "Bad magician!";
        }
        else if (intersect.size() == 0)
            cout << "Volunteer cheated!";
        else
            cout << intersect[0];
        cout << endl;

    }
    return 0;
}

