#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int t;

    cin >> t;


    vector<bool> indicates;
    indicates.reserve(100);

    for (int c = 1; c <= t; ++c)
    {
        int flips = 0;
        string input;

        cin >> input;
        indicates.clear();
        for (auto c : input)
            indicates.push_back(c == '+');

        while (true) {
            bool need_find = !indicates[0];
            auto iter = find(indicates.begin(), indicates.end(), need_find);
            if (iter != indicates.end()) {
                flips++;
                int n = iter - indicates.begin();
                for (int i = 0; i < n; ++i) {
                    indicates[i] = need_find;
                }
            }
            else {
                if (indicates[0] == false)
                    flips++;
                break;
            }
        }
        

        cout << "Case #" << c << ": " << flips << endl;
    }
    return 0;
}