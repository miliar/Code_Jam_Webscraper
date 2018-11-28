#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <climits>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;

int l;
unordered_map<char, int> m;
vector<int> n;

bool walk(){
    if (l > 0 && l < 3)
        return false;
    if (l == 0){
        return true;
    }
    
    if (m['Z'] > 0 && m['E'] > 0 && m['R'] > 0 && m['O'] > 0){
        m['Z']--;
        m['E']--;
        m['R']--;
        m['O']--;
        l -= 4;

        n.push_back(0);
        if (walk())
            return true;
        n.pop_back();

        m['Z']++;
        m['E']++;
        m['R']++;
        m['O']++;
        l += 4;
    }
    if (m['O'] > 0 && m['N'] > 0 && m['E'] > 0){
        m['O']--;
        m['N']--;
        m['E']--;
        l -= 3;

        n.push_back(1);
        if (walk())
            return true;
        n.pop_back();

        m['O']++;
        m['N']++;
        m['E']++;
        l += 3;
    }
    if (m['T'] > 0 && m['W'] > 0 && m['O'] > 0){
        m['T']--;
        m['W']--;
        m['O']--;
        l -= 3;

        n.push_back(2);
        if (walk())
            return true;
        n.pop_back();

        m['T']++;
        m['W']++;
        m['O']++;
        l += 3;
    }
    if (m['T'] > 0 && m['H'] > 0 && m['R'] > 0 && m['E'] > 1){
        m['T']--;
        m['H']--;
        m['R']--;
        m['E'] -= 2;
        l -= 5;

        n.push_back(3);
        if (walk())
            return true;
        n.pop_back();

        m['T']++;
        m['H']++;
        m['R']++;
        m['E'] += 2;
        l += 5;
    }
    if (m['F'] > 0 && m['O'] > 0 && m['U'] > 0 && m['R'] > 0){
        m['F']--;
        m['O']--;
        m['U']--;
        m['R']--;
        l -= 4;

        n.push_back(4);
        if (walk())
            return true;
        n.pop_back();

        m['F']++;
        m['O']++;
        m['U']++;
        m['R']++;
        l += 4;
    }
    if (m['F'] > 0 && m['I'] > 0 && m['V'] > 0 && m['E'] > 0){
        m['F']--;
        m['I']--;
        m['V']--;
        m['E']--;
        l -= 4;

        n.push_back(5);
        if (walk())
            return true;
        n.pop_back();

        m['F']++;
        m['I']++;
        m['V']++;
        m['E']++;
        l += 4;
    }
    if (m['S'] > 0 && m['I'] > 0 && m['X'] > 0){
        m['S']--;
        m['I']--;
        m['X']--;
        l -= 3;

        n.push_back(6);
        if (walk())
            return true;
        n.pop_back();

        m['S']++;
        m['I']++;
        m['X']++;
        l += 3;
    }
    if (m['S'] > 0 && m['E'] > 1 && m['V'] > 0 && m['N'] > 0){
        m['S']--;
        m['E'] -= 2;
        m['V']--;
        m['N']--;
        l -= 5;

        n.push_back(7);
        if (walk())
            return true;
        n.pop_back();

        m['S']++;
        m['E'] += 2;
        m['V']++;
        m['N']++;
        l += 5;
    }
    if (m['E'] > 0 && m['I'] > 0 && m['G'] > 0 && m['H'] > 0 && m['T'] > 0){
        m['E']--;
        m['I']--;
        m['G']--;
        m['H']--;
        m['T']--;
        l -= 5;

        n.push_back(8);
        if (walk())
            return true;
        n.pop_back();

        m['E']++;
        m['I']++;
        m['G']++;
        m['H']++;
        m['T']++;
        l += 5;
    }
    if (m['N'] > 1 && m['I'] > 0 && m['E'] > 0){
        m['N'] -= 2;
        m['I']--;
        m['E']--;
        l -= 4;

        n.push_back(9);
        if (walk())
            return true;
        n.pop_back();

        m['N'] += 2;
        m['I']++;
        m['E']++;
        l += 4;
    }

    return false;
}

int main(){
    ifstream fin("in1");
    ofstream fout("out1");
    int T;

    fin >> T;
    for (int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";

        string S;
        fin >> S;
        n.clear();
        m.clear();

        l = S.length();
        for (int i = 0; i < S.length(); i++){
            m[S[i]]++;
        }
        walk();
        sort(n.begin(), n.end());
        for (int i = 0; i < n.size(); i++)
            fout << n[i];
        fout << endl;
    }

    fin.close();
    fout.close();
}
