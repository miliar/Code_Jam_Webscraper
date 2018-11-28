#include <iostream>
#include <set>
#include <string>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <fstream>

using namespace::std;

void first() {
    ifstream file("A-large.in");
    ofstream out("first.out");
    size_t t;
    file >> t;
    string people;
    for (size_t case_ = 1; case_ <= t; ++case_) {
        size_t shiness;
        file >> shiness;
        file >> people;
        size_t count = (people[0] - '0');
        size_t answer = 0;
        for (size_t i = 1; i < people.size(); ++i) {
            if (i > count) {
                answer += (i - count);
                count = i;
            }
            count += (people[i] - '0');

        }
        //Case #1: 0
        out << "Case #" << case_ <<": " << answer << endl;
    }
}

void second() {
    ifstream file("2.in");
    size_t t;
    file >> t;
    for (size_t case_ = 1; case_ <= t; ++case_) {
        int n;
        file >> n;
        int m = 0;
        int tmp = 0;
        for (int i = 0; i < n; ++i) {
            file >> tmp;
            m = max(m, tmp);
        }
        int answer = m;
        int count = 0;
        while (m) {
            if (m % 2 == 1) {
                m = m / 2  +1;
            }
            else {
                m /= 2;
            }
            ++count;
            answer = min(answer, m + count);
            if (m == 1) {
                break;
            }
        }

        cout << "Case #" << case_ <<": " << answer << endl;
    }

}


int main(int argc, const char* argv[]) {
    first();
    return 0;    
}