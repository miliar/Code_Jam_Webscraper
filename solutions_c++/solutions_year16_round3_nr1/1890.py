#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <cstdlib>
#include <functional>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        int n;
        cin >> n;

        char name = 'A';
        multimap<int, char, greater<int> > senats;
        int all_senats = 0;
        for (int j = 0; j < n; ++j) {
            int x;
            cin >> x;
            all_senats += x;
            senats.insert(pair<int, char>(x, name++));
        }

        stringstream answer;
        while (!senats.empty()) {
            auto first = senats.begin();
            int count = first->first;
            char first_name = first->second;
            senats.erase(first);
            if (count > 1) {
                senats.insert(pair<int, char>(count - 1, first_name));
            }
            all_senats--;

            if (all_senats == 2) {
                answer << " " << first_name;
                continue;
            }

            auto second = senats.begin();
            count = second->first;
            char second_name = second->second;
            senats.erase(second);
            if (count > 1) {
                senats.insert(pair<int, char>(count - 1, second_name));
            }
            all_senats--;
            answer << " " << first_name << second_name;
        }

        cout << "Case #" << i << ":" << answer.str() << endl;
    }

    return 0;
}
