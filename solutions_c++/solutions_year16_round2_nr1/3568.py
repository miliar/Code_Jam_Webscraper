#include<cstdio>
#include<iostream>
#include<string>
#include<map>

using namespace std;

int t, casei;

int main() {
    casei = 0;
    scanf("%d", &t);
    while(t--) {
        string s;
        cin >> s;
        map<char, int> m;
        map<int, int> number;
        int n = s.length();
        for (int i = 0; i < n; ++i)
            ++m[s[i]];

        if(m['Z'] > 0) { //0
            int tmp = m['Z'];
            number[0] = tmp;
            m['Z'] -= tmp; m['E'] -= tmp; m['R'] -= tmp; m['O'] -= tmp;
            n -= 4*tmp;
        }
        if(m['W'] > 0) { //2
            int tmp = m['W'];
            number[2] = tmp;
            m['T'] -= tmp; m['W'] -= tmp; m['O'] -= tmp;
            n -= 3*tmp;
        }
        if(m['U'] > 0) { //4
            int tmp = m['U'];
            number[4] = tmp;
            m['F'] -= tmp; m['O'] -= tmp; m['U'] -= tmp; m['R'] -= tmp;
            n -= 4*tmp;
        }
        if(m['X'] > 0) { //6
            int tmp = m['X'];
            number[6] = tmp;
            m['S'] -= tmp; m['I'] -= tmp; m['X'] -= tmp;
            n -= 3*tmp;
        }
        if(m['G'] > 0) { //8
            int tmp = m['G'];
            number[8] = tmp;
            m['E'] -= tmp; m['I'] -= tmp; m['G'] -= tmp; m['H'] -= tmp; m['T'] -= tmp;
            n -= 5*tmp;
        }
        while(n > 0) {
            if(m['O'] > 0 && m['N'] > 0 && m['E'] > 0) {
                ++number[1];
                --m['O']; --m['N']; --m['E'];
                n -= 3;
            }
            if(m['T'] > 0 && m['H'] > 0 && m['R'] > 0 && m['E'] > 1) {
                ++number[3];
                --m['T']; --m['H']; --m['R']; m['E'] -= 2;
                n -= 5;
            }
            if(m['F'] > 0 && m['I'] > 0 && m['V'] > 0 && m['E'] > 0) {
                ++number[5];
                --m['F']; --m['I']; --m['V']; --m['E'];
                n -= 4;
            }
            if(m['S'] > 0 && m['V'] > 0 && m['N'] > 0 && m['E'] > 1) {
                ++number[7];
                --m['S']; --m['V']; --m['N']; m['E'] -= 2;
                n -= 5;
            }
            if(m['N'] > 1 && m['I'] > 0 && m['E'] > 0) {
                ++number[9];
                --m['I']; --m['E']; m['N'] -= 2;
                n -= 4;
            }
        }
        cout << "Case #" << ++casei << ": ";
        for(auto it = number.begin(); it != number.end(); it++)
            for(int i = 0; i < it->second; i++)
                cout << it->first;
        cout << "\n";
    }
    return 0;
}
