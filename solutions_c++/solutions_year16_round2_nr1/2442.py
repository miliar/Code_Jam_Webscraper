#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 02345678
int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string s;
        vector<int> v;
        cin >> s;
        // Get zero's
        size_t where;
        while ((where = s.find('Z')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("ERO")) s.erase(s.find(c), 1);
            v.push_back(0);
        }
        //        cerr << s << endl;
        while ((where = s.find('X')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("SI")) s.erase(s.find(c), 1);
            v.push_back(6);
        }
        //        cerr << s << endl;
        // Done with sixes, so only s is seven
        while ((where = s.find('S')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("EVEN")) s.erase(s.find(c), 1);
            v.push_back(7);
        }
        // Done with sevens, so only v is five
        while ((where = s.find('V')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("FIE")) s.erase(s.find(c), 1);
            v.push_back(5);
        }
        //        cerr << s << endl;
        while ((where = s.find('W')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("TO")) s.erase(s.find(c), 1);
            v.push_back(2);
        }
        //        cerr << s << endl;
        while ((where = s.find('G')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("EIHT")) s.erase(s.find(c), 1);
            v.push_back(8);
        }
        //        cerr << s << endl;
        while ((where = s.find('F')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("OUR")) s.erase(s.find(c), 1);
            v.push_back(4);
        }
        //        cerr << s << endl;
        while ((where = s.find('R')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("THEE")) s.erase(s.find(c), 1);
            v.push_back(3);
        }
        //        cerr << s << endl;
        while ((where = s.find('O')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("NE")) s.erase(s.find(c), 1);
            v.push_back(1);
        }
        //        cerr << s << endl;
        while ((where = s.find('I')) != string::npos) {
            s.erase(where, 1);
            for (char c : string("NNE")) s.erase(s.find(c), 1);
            v.push_back(9);
        }
        //        cerr << s << endl;
        sort(v.begin(), v.end());
        cout << "Case #" << i+1 << ": ";
        for (int i : v) cout << i;
        cout << endl;
    }
}
