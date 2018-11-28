#include<iostream>
#include<string>

using namespace std;

int main() {
    int stand = 0, invite = 0;
    int round = 0;
    string line, sub1, sub2;
    getline(cin, line);

    while (getline(cin, line)) {
        sub1 = line.substr(0, line.find(' '));
        sub2 = line.substr(line.find(' ') + 1);
        stand = invite = 0;
        for (int level = 0; level != sub2.length(); level++) {
            if (level == 0) {
                stand += sub2.at(level) - '0';
                continue;
            }

            if ((sub2.at(level) - '0') > 0 && (stand + invite) < level) {
                invite = level - stand;
            }
            stand += sub2.at(level) - '0';
        }
        cout << "Case #" << ++round << ": " << invite << endl;
    }

    return 0;
}
