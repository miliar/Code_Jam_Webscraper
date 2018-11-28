#include <iostream>
#include <set>
#include <string>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <fstream>

using namespace::std;


void second() {
    ifstream file("B-large.in");
    ofstream out("second.out");
    size_t t;
    file >> t;
    for (size_t case_ = 1; case_ <= t; ++case_) {
        int n;
        file >> n;
        int answer = 0;
        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            file >> v[i];
            answer = max(answer, v[i]);
        }
        make_heap(v.begin(),v.end());
        for (int i = 2; i < answer; ++i) {
            int res = 0;
            for (int& a : v) {
                res += a % i == 0 ? a / i - 1 : a / i;
            }
            answer = min(answer, i + res);
        }

        cout << "Case #" << case_ <<": " << answer << endl;
    }
    
}


int main(int argc, const char* argv[]) {
    second();
    return 0;    
}