#include <string>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::stoi;

int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        int s_max;
        string audience;
        cin >> s_max >> audience;

        int standing = 0;
        int added = 0;

        for(int i = 0; i < audience.length(); ++i) {
            int curr = stoi(audience.substr(i,1));
            if (standing + added < i) {
                added += i - (standing + added);
            }
            standing += curr;
        }
        cout << "Case #" << (i+1) << ": " << added << endl;
    }
    return 0;
}
