#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;


int main(int argc, char const *argv[]) {
    long long T;
    int c, a1, a2;
    fstream f("in.in");
    f >> T;
    For (t, T) {
        f >> a1;
        vector<int> arr1;
        vector<int> arr2;
        vector<int> v(8);
        vector<int>::iterator it;
        For (i, 4) For (j, 4) {
            f >> c;
            if (i == a1-1) arr1.push_back(c);
        }
        f >> a2;
        For (i, 4) For (j, 4) {
            f >> c;
            if (i == a2-1) arr2.push_back(c);
        }
        sort(arr1.begin(), arr1.end());
        sort(arr2.begin(), arr2.end());
        it = set_intersection (arr1.begin(), arr1.end(), arr2.begin(), arr2.end(), v.begin());
        v.resize(it - v.begin());

        if (v.size() == 1) {
            cout << "Case #"<<t+1<< ": " << v.at(0) << endl;
        } else if (v.size() > 1) {
            cout << "Case #"<<t+1<< ": Bad magician!" << endl;
        } else {
            cout << "Case #"<<t+1<< ": Volunteer cheated!" << endl;
        }
    }
    f.close();
    return 0;
}
