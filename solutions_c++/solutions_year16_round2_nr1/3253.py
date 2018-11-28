#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("output_large.txt", "w", stdout);
    int t;
    string s;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++) {
        cin >> s;
        int len = s.length();
        int alphabet[26] = {0};
        vector <int> v;
        for(int i = 0; i < len; i++)
            alphabet[s[i]-65]++;

        while(alphabet['Z'-65]) {
            v.push_back(0);
            alphabet['Z'-65]--;
            alphabet['E'-65]--;
            alphabet['R'-65]--;                
            alphabet['O'-65]--;

        }
                
        while(alphabet['W'-65]) {
            v.push_back(2);
            alphabet['T'-65]--;
            alphabet['W'-65]--;
            alphabet['O'-65]--;
        }
            
        while(alphabet['U'-65]) {
            v.push_back(4);
            alphabet['F'-65]--;
            alphabet['O'-65]--;
            alphabet['U'-65]--;
            alphabet['R'-65]--;
        }
            
        while(alphabet['X'-65]) {
            v.push_back(6);
            alphabet['S'-65]--;
            alphabet['I'-65]--;
            alphabet['X'-65]--;
        }
            
        while(alphabet['G'-65]) {
            v.push_back(8);
            alphabet['E'-65]--;
            alphabet['I'-65]--;
            alphabet['G'-65]--;
            alphabet['H'-65]--;
            alphabet['T'-65]--;
        }

        while(alphabet['O'-65]) {
            v.push_back(1);
            alphabet['O'-65]--;
            alphabet['N'-65]--;
            alphabet['E'-65]--;
        }
        while(alphabet['R' - 65]) {
            v.push_back(3);
            alphabet['T'-65]--;
            alphabet['H'-65]--;
            alphabet['R'-65]--;
            alphabet['E'-65]--;
            alphabet['E'-65]--;
        }
        while(alphabet['F' - 65]) {
            v.push_back(5);
            alphabet['F'-65]--;
            alphabet['I'-65]--;
            alphabet['V'-65]--;
            alphabet['E'-65]--;
        }
        while(alphabet['S' - 65]) {
            v.push_back(7);
            alphabet['S'-65]--;
            alphabet['E'-65]--;
            alphabet['V'-65]--;
            alphabet['E'-65]--;
            alphabet['N'-65]--;

        }

        int all = 0;
        for(int i = 0; i < 26; i++)
            all += alphabet[i];

        int times = all/4;
        while(times > 0) {
            times--;
            v.push_back(9); 
        }
        sort(v.begin(), v.end());
        cout << "Case #" << k << ": ";
        for(int i = 0; i < v.size(); i++)
            cout << v[i];

        cout << "\n";
    }

    return 0;
}

//g++ a.cpp -std=c++11 -o a