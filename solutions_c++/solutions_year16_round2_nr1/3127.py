#include <iostream>
#include <map>
#include <cstdlib>
using namespace std;
map<int, string> spell;
map<char, int> frequent;
string s;
void decrease(int i) {
    for (int j=0; j < spell[i].length(); j++) {
        if (frequent.count(spell[i][j]))
            frequent[spell[i][j]]--;
    }
}
int main() {
    spell[0] = "ZERO";
    spell[1] = "ONE";
    spell[2] = "TWO";
    spell[3] = "THREE";
    spell[4] = "FOUR";
    spell[5] = "FIVE";
    spell[6] = "SIX";
    spell[7] = "SEVEN";
    spell[8] = "EIGHT";
    spell[9] = "NINE";
    int t;
    cin>>t;
    int f = 0;
    while(t--)  {
        for(char x='A';x<'Z';x++)   {
            frequent[x] = 0;
        }
        cin>>s;
        int l = s.length();
        for(int i=0;i<l;i++)    {
                frequent[s[i]]++;
        }
        string ans;
        while (frequent['Z'] > 0) {
            decrease(0);
            ans += '0';
        }
        while (frequent['O']-frequent['W']-frequent['U']>0) {
            decrease(1);
            ans += '1';
        }
        while (frequent['W'] > 0) {
            decrease(2);
            ans += '2';
        }
        while (frequent['H'] - frequent['G'] > 0) {
            decrease(3);
            ans += '3';
        }
        while (frequent['U'] > 0) {
            decrease(4);
            ans += '4';
        }
        while (frequent['F'] - frequent['U'] > 0) {
            decrease(5);
            ans += '5';
        }
        while (frequent['X'] > 0) {
            decrease(6);
            ans += '6';
        }
        while (frequent['S'] - frequent['X'] > 0) {
            decrease(7);
            ans += '7';
        }
        while (frequent['G'] > 0) {
            decrease(8);
            ans += '8';
        }
        while (frequent['I'] > 0) {
            decrease(9);
            ans += '9';
        }
        cout<<"Case #"<<++f<<": ";
        cout << ans << endl;
    }
    return 0;
}

