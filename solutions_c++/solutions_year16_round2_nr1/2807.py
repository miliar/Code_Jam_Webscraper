#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int letters[30];
int nums[11];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outLarge.txt", "w", stdout);

    int n = 0;
    cin >> n;
    //ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE
    for (int i = 1; i <= n; i++){
        string s = "";
        cin >> s;
        for (int j = 0; j < s.length(); j++){
            char c = s[j] - 'A';
            //int pos = (int)c;
            letters[c] ++;
            //cout << pos << " ";
        }
        //for(int j = 0; j < 27; j++){
        //    cout << letters[j];
        //}
        //cout << endl;

        //000000000000000000
        nums[0] = letters['Z'-'A'];
        letters['Z'-'A'] -= nums[0];
        letters['E'-'A'] -= nums[0];
        letters['R'-'A'] -= nums[0];
        letters['O'-'A'] -= nums[0];


        //666666666666666666
        nums[6] = letters['X'-'A'];
        letters['S'-'A'] -= nums[6];
        letters['X'-'A'] -= nums[6];
        letters['I'-'A'] -= nums[6];


        //777777777777777777
        nums[7] = letters['S'-'A'];
        letters['S'-'A'] -= nums[7];
        letters['E'-'A'] -= nums[7];
        letters['V'-'A'] -= nums[7];
        letters['E'-'A'] -= nums[7];
        letters['N'-'A'] -= nums[7];


        //888888888888888888
        nums[8] = letters['G'-'A'];
        letters['E'-'A'] -= nums[8];
        letters['I'-'A'] -= nums[8];
        letters['G'-'A'] -= nums[8];
        letters['H'-'A'] -= nums[8];
        letters['T'-'A'] -= nums[8];


        //555555555555555555
        nums[5] = letters['V'-'A'];
        letters['F'-'A'] -= nums[5];
        letters['I'-'A'] -= nums[5];
        letters['V'-'A'] -= nums[5];
        letters['E'-'A'] -= nums[5];


        //999999999999999999
        nums[9] = letters['I'-'A'];
        letters['N'-'A'] -= nums[9];
        letters['I'-'A'] -= nums[9];
        letters['N'-'A'] -= nums[9];
        letters['E'-'A'] -= nums[9];


        //444444444444444444
        nums[4] = letters['F'-'A'];
        letters['F'-'A'] -= nums[4];
        letters['O'-'A'] -= nums[4];
        letters['U'-'A'] -= nums[4];
        letters['R'-'A'] -= nums[4];


        //222222222222222222
        nums[2] = letters['W'-'A'];
        letters['T'-'A'] -= nums[2];
        letters['W'-'A'] -= nums[2];
        letters['O'-'A'] -= nums[2];


        //333333333333333333
        nums[3] = letters['T'-'A'];
        letters['T'-'A'] -= nums[3];
        letters['H'-'A'] -= nums[3];
        letters['R'-'A'] -= nums[3];
        letters['E'-'A'] -= nums[3];
        letters['E'-'A'] -= nums[3];


        //111111111111111111
        nums[1] = letters['O'-'A'];
        letters['O'-'A'] -= nums[1];
        letters['N'-'A'] -= nums[1];
        letters['E'-'A'] -= nums[1];

        cout << "Case #" << i << ": ";
        for (int j = 0; j<10; j++){
            //cout << nums[j] << ": ";
            for (int k = 0; k<nums[j]; k++){
                cout << j;
            }
            nums[j] = 0;
            //cout << ", ";
        }
        for (int j = 0; j < 26; j++){
            if (letters[j] != 0)
                cout << "----------------------------------";
        }
        cout << endl;
    }


    return 0;
}
