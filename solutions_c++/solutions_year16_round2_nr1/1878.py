#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
    ofstream fout("getting the digits large.txt");
    map <char,int> m;
    vector<int> v;
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        m.clear();
        v.clear();
        string s;
        cin >> s;
        for (int i = 0; i < s.size(); i++) {
            m[s[i]]++;
        }
        while (m['Z']--) {
            v.push_back(0);
            m['E']--;
            m['R']--;
            m['O']--;
        }
        while (m['X']--) {
            v.push_back(6);
            m['S']--;
            m['I']--;
        }
        while (m['G']--) {
            v.push_back(8);
            m['E']--;
            m['I']--;
            m['H']--;
            m['T']--;
        }
        while (m['W']--) {
            v.push_back(2);
            m['T']--;
            m['O']--;
        }
        while (m['H']--) {
            v.push_back(3);
            m['T']--;
            m['E']-=2;
            m['R']--;
        }
        while (m['R']--) {
            v.push_back(4);
            m['F']--;
            m['O']--;
            m['U']--;
        }
        while (m['F']--) {
            v.push_back(5);
            m['I']--;
            m['V']--;
            m['E']--;
        }
        while (m['V']--) {
            v.push_back(7);
            m['S']--;
            m['E']-=2;
            m['N']--;
        }
        while (m['O']--) {
            v.push_back(1);
            m['N']--;
            m['E']--;
        }
        while (m['E']--) {
            v.push_back(9);

        }
        sort(v.begin(),v.end());
        fout << "Case #" << cs << ": ";
        for (auto a: v) {
            fout << a;
        }
        fout << endl;

    }
}
