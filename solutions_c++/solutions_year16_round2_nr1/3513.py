#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

bool ltchr (char a, char b)
{
    return a < b;
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("a-small.out");

    int T;
    fin >> T;

    for (int i=1; i<=T; i++) {
        string in;
        fin >> in;

        vector<char> letters(26, 0);
        vector<int> nums(10, 0);
        for (auto it=in.begin(); it<in.end(); it++) {
            letters[(*it)-'A']++;
        }

        //zero
        while (letters['Z'-'A'] > 0) {
            nums[0]++;
            letters['Z'-'A']--;
            letters['E'-'A']--;
            letters['R'-'A']--;
            letters['O'-'A']--;
        }

        //two
        while (letters['W'-'A'] > 0) {
            nums[2]++;
            letters['W'-'A']--;
            letters['T'-'A']--;
            letters['O'-'A']--;
        }

        //four
        while (letters['U'-'A'] > 0) {
            nums[4]++;
            letters['U'-'A']--;
            letters['F'-'A']--;
            letters['O'-'A']--;
            letters['R'-'A']--;
        }

        //six
        while (letters['X'-'A'] > 0) {
            nums[6]++;
            letters['X'-'A']--;
            letters['S'-'A']--;
            letters['I'-'A']--;
        }

        //eight
        while (letters['G'-'A'] > 0) {
            nums[8]++;
            letters['G'-'A']--;
            letters['E'-'A']--;
            letters['I'-'A']--;
            letters['H'-'A']--;
            letters['T'-'A']--;
        }

        //three
        while (letters['R'-'A'] > 0) {
            nums[3]++;
            letters['T'-'A']--;
            letters['H'-'A']--;
            letters['R'-'A']--;
            letters['E'-'A'] -= 2;
        }

        //one
        while (letters['O'-'A'] > 0) {
            nums[1]++;
            letters['O'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;
        }

        //five
        while (letters['F'-'A'] > 0) {
            nums[5]++;
            letters['F'-'A']--;
            letters['I'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
        }

        //seven
        while (letters['S'-'A'] > 0) {
            nums[7]++;
            letters['S'-'A']--;
            letters['E'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
            letters['N'-'A']--;
        }

        //nine
        while (letters['N'-'A'] > 0) {
            nums[9]++;
            letters['N'-'A']--;
            letters['I'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;
        }

        fout << "Case #" << i << ": ";
        for (int k=0; k<10; k++) {
            for (int j=0; j<nums.at(k); j++) {
                fout << k;
            }
        }
        fout << "\n";
    }

    return 0;
}
