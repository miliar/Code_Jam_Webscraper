#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

    ifstream in("input.txt");
    ofstream out("output.txt");

vector<int> rdClm() {
    vector<int> res = vector<int>();
    for (int i = 0; i < 4; i++) {
        int t;
        in >> t;
        res.push_back(t);
    }
    return res;
}

bool isIn(vector<int> a, int t) {
    for (int i = 0; i < a.size(); i++)
        if (a[i] == t)
            return true;
    return false;
}

int main()
{
    int t;
    in >> t;
    for (int i = 0; i < t; i++) {
        int a1, a2;
        in >> a1; a1--;
        vector<int> a = vector<int>();
        vector<int> b = vector<int>();
        vector<int> tmp;
        for (int i = 0; i < 4; i++) {
            tmp = rdClm();
            if (i == a1)
                a = tmp;
        }
        in >> a2; a2--;
        for (int i = 0; i < 4; i++) {
            tmp = rdClm();
            if (i == a2)
                b = tmp;
        }
        vector<int> res = vector<int>();
        for (int j = 0; j < a.size(); j++)
            if (isIn(b, a[j]))
                res.push_back(a[j]);
        out << "Case #" << i + 1 << ": ";
        if (res.size() == 0)
            out << "Volunteer cheated!" << endl;
        if (res.size() == 1)
            out << res[0] << endl;
        if (res.size() > 1)
            out << "Bad magician!" << endl;
    }

    in.close();
    out.close();
    return 0;
}
