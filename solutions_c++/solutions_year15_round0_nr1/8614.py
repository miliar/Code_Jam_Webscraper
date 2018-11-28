#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int cases;
    ofstream ofs("/Users/Alex/Projects/OJ-C++/output.txt");
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {
        int smax;
        string people;
        cin >> smax >> people;
        int count = people[0] - '0';
        int add = 0;
        for (int j = 1; j < people.size(); ++j) {
            int n = people[j] - '0';
            if (n > 0) {
                if (count < j) {
                    add += j - count;
                    count = j;
                }
                count += n;
            }
        }
        ofs << "Case #" << i << ": " << add << endl;
    }
    ofs.close();
    return 0;
}