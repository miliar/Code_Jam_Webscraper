#include <bits/stdc++.h>

using namespace std;

int main() {
    int T = 0;
    cin >> T;

    for(int t = 1; t <= T; t++) {
        string buffer;
        cin >> buffer;

        map<char, int> count;
        for(size_t i = 0; i < buffer.size(); i++) {
            count[buffer[i]]++;
        }

        vector<int> number(10, 0);
        if (count['Z'] != 0) {
            number[0] = count['Z'];
            count['E'] -= count['Z'];
            count['R'] -= count['Z'];
            count['O'] -= count['Z'];
            count['Z'] = 0;
        }

        if(count['W'] != 0) {
            number[2] = count['W'];
            count['T'] -= count['W'];
            count['O'] -= count['W'];
            count['W'] = 0;
        }


        if (count['G'] != 0) {
            number[8] = count['G'];
            count['E'] -= count['G'];
            count['I'] -= count['G'];
            count['H'] -= count['G'];
            count['T'] -= count['G'];
            count['G'] = 0;
        }

        if (count['X'] != 0) {
            number[6] = count['X'];
            count['S'] -= count['X'];
            count['I'] -= count['X'];
            count['X'] = 0;
        }

        if (count['S'] != 0) {
            number[7] = count['S'];
            count['E'] -= count['S'];
            count['V'] -= count['S'];
            count['E'] -= count['S'];
            count['N'] -= count['S'];
            count ['S'] = 0;
        }

        if (count['V'] != 0) {
            number[5] = count['V'];
            count['F'] -= count['V'];
            count['I'] -= count['V'];
            count['E'] -= count['V'];
            count['V'] = 0;
        }

        if(count['U'] != 0) {
            number[4] = count['U'];
            count['F'] -= count['U'];
            count['O'] -= count['U'];
            count['R'] -= count['U'];
            count['U'] = 0;
        }

        if(count['I'] != 0) {
            number[9] = count['I'];
            count['N'] -= count['I'];
            count['N'] -= count['I'];
            count['E'] -= count['I'];
            count['I'] = 0;
        }
        number[1] = count['O'];
        number[3] = count['T'];

        cout << "Case #" << t << ": ";

        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < number[i]; j++) {
                cout << i;
            }
        }
        cout << endl;
    }


    return 0;
}
