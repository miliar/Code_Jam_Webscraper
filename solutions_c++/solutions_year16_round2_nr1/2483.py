#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-result.txt", "w", stdout);

    int T; cin >> T;

    char evenChar[5] = {'Z', 'W', 'U', 'X', 'G'};
    char oddChar[5] = {'O', 'R', 'F', 'S', 'I'};
    vector<vector<int>> oddMap;
    oddMap.push_back(vector<int>({0, 2, 4}));
    oddMap.push_back(vector<int>({0, 4}));
    oddMap.push_back(vector<int>({4}));
    oddMap.push_back(vector<int>({6}));
    oddMap.push_back(vector<int>({5, 6, 8}));

    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;

        int characters[26]; for (int i = 0; i < 26; i++) characters[i] = 0;
        int nums[10]; for (int i = 0; i < 10; i++) nums[i] = 0;

        for (char c : s) {
            characters[c - 'A']++;
        }

        for (int i = 0; i < 5; i++) {
            nums[i*2] = characters[evenChar[i] - 'A'];
        }

        for (int i = 0; i < 5; i++) {
            nums[1+2*i] = characters[oddChar[i] - 'A'];
            for (int j : oddMap[i]) {
                nums[1+2*i] -= nums[j];
            }
        }
        cout << "Case #" << t << ": ";

        for (int i = 0; i < 10; i++)
            for (int j = 0; j < nums[i]; j++)
                cout << i;
        cout << endl;

    }

    return 0;
}
