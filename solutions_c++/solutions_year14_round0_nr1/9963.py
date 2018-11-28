#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_set>
using namespace std;

inline vector<int> split(string &a, char delim)
{
    vector<int> elems;
    stringstream ss(a);
    string e;
    int i;
    while (getline(ss, e, delim)) {
        istringstream is(e);
        is >> i;
        elems.push_back(i);
    }
    return elems;
}

/*
 return 1-16:    return actual intersection
 return -1:      Badmagician!
 return -2:      Volunteer cheated!
 return -3       Unknow
 */
inline int intersec(vector<int> &a, vector<int> &b)
{
    vector<int> ret;
    unordered_set<int> us;
    for (int i = 0; i < a.size(); i++) {
        us.insert(a[i]);
    }

    for (int i = 0; i < b.size(); i++) {
        if (us.find(b[i]) != us.end()) {
            ret.push_back(b[i]);
        }
    }

    if (ret.size() == 1) return ret[0];
    else if (ret.size() > 1) return -1;
    else if (ret.size() == 0) return -2;
    else return -3;
    
}

int main(int argc, char *argv[])
{
    string size_str;
    int size = 0;
    
    getline(cin, size_str);
    istringstream is0(size_str);
    is0 >> size;
    
    vector<string> output;
    for (int i = 1; i <= size; i++) {
        string line1_str;
        string line2_str;
        int line1 = 0;
        int line2 = 0;
        vector<vector<int> > mat1;
        vector<vector<int> > mat2;
        
        getline(cin, line1_str);
        istringstream is1(line1_str);
        is1 >> line1;
        for (int i = 0; i < 4; i++) {
            string temp1;
            getline(cin, temp1);
            vector<int> seg1 = split(temp1, ' ');
            mat1.push_back(seg1);
        }
        getline(cin, line2_str);
        istringstream is2(line2_str);
        is2 >> line2;
        for (int i = 0; i < 4; i++) {
            string temp2;
            getline(cin, temp2);
            vector<int> seg2 = split(temp2, ' ');
            mat2.push_back(seg2);
        }
        int res = intersec(mat1[line1-1], mat2[line2-1]);

        cout << "Case #";
        cout << i;
        cout << ": ";
        if (res >=1 && res <= 16) {
            cout << res;
        } else if (res == -1) {
            cout << "Bad magician!";
        } else if (res == -2) {
            cout << "Volunteer cheated!";
        }
        cout << endl;;
    }
    
    return 0;
}