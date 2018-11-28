
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
    auto cases = 0;
    cin >> cases;

    for (auto i=0; i < cases; i++) {
        auto max = 0;
        auto audiance = string{""};
        cin >> max >> audiance;
        auto people = 0;
        auto friends = 0;
        for (auto j=0; j < audiance.length(); j++) {
            auto howMany = audiance[j] - '0';
            if (j > people) {
                auto diff = j - people;
                friends += diff;
                people += diff;
            }
            people += howMany;
        }
        cout << "Case #" << i+1 << ": " << friends << endl;
    }
}
