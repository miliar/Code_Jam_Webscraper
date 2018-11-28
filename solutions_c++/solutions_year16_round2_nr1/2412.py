#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <map>
#include <cstring>

using namespace std;

int main()
{

    int t;
    cin >> t;
    for (int c=1; c<=t; ++c)
    {
        string input;
        vector<int> count(10);
        map<char,int> freq;
        freq['E'] = 0;
        freq['F'] = 0;
        freq['G'] = 0;
        freq['H'] = 0;
        freq['I'] = 0;
        freq['N'] = 0;
        freq['O'] = 0;
        freq['R'] = 0;
        freq['S'] = 0;
        freq['T'] = 0;
        freq['U'] = 0;
        freq['V'] = 0;
        freq['W'] = 0;
        freq['X'] = 0;
        freq['Z'] = 0;

        cin >> input;
        for(unsigned int i = 0; i<input.length(); i++) {
            char c = input[i];
            freq[c]++;
        }

        /*
         first parse unique
         Z - 0
         W - 2
         U - 4
         X - 6
         G - 8
        */

        // ZERO
        count[0] = freq['Z'];
        count[2] = freq['W'];
        count[4] = freq['U'];
        count[6] = freq['X'];
        count[8] = freq['G'];

        // ZERO
        freq['E'] -= freq['Z'];
        freq['R'] -= freq['Z'];
        freq['O'] -= freq['Z'];
        freq['Z'] -= freq['Z'];

        // TWO
        freq['T'] -= freq['W'];
        freq['O'] -= freq['W'];
        freq['W'] -= freq['W'];

        // FOUR
        freq['F'] -= freq['U'];
        freq['O'] -= freq['U'];
        freq['R'] -= freq['U'];
        freq['U'] -= freq['U'];

        // SIX
        freq['S'] -= freq['X'];
        freq['I'] -= freq['X'];
        freq['X'] -= freq['X'];

        // EIGHT
        freq['E'] -= freq['G'];
        freq['I'] -= freq['G'];
        freq['H'] -= freq['G'];
        freq['T'] -= freq['G'];
        freq['G'] -= freq['G'];


        /*
         second parse unique
         O - 1
         H - 3
         F - 5
         S - 7
        */
        count[1] = freq['O'];
        count[3] = freq['H'];
        count[5] = freq['F'];
        count[7] = freq['S'];

        // ONE
        freq['I'] -= freq['F'];

        count[9] = freq['I'];

        cout << "Case #" << c << ": ";
        for(int i=0;i < count.size();++i) {
            while(count[i]--)
            cout << i;
        }
        cout << endl;
     //    << answer << endl;
    }

    return 0;
}
