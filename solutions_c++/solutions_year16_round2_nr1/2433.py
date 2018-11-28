#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

#undef int
int main()
{
#define int long long
    freopen("in", "r", stdin); freopen("out","w", stdout);
    int t; cin >> t;
    string num;
    getline(cin,num);
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        getline(cin, num);
        cerr << num << endl;
        int occ[26], n = num.size();
        for (int i = 0; i < 26; i++) occ[i] = 0;
        for (int i = 0; i < n; i++){
            int cur = num[i] - 'A';
            occ[cur]++;
        }
        vector <int> number;
        while(n > 2){
            cerr << n << endl;
            if(occ['Z'-'A'] > 0){
                number.push_back(0);
                occ['Z'-'A']--; occ['E'-'A']--; occ['R'-'A']--; occ['O'-'A']--;
                n -= 4;
                continue;
            }
            if(occ['W' - 'A'] > 0){
                number.push_back(2);
                occ['T'-'A']--;occ['W'-'A']--;occ['O'-'A']--;
                n -= 3;
                continue;
            }
            if(occ['U'-'A'] > 0){
                number.push_back(4);
                occ['F'-'A']--;occ['O'-'A']--;occ['U'-'A']--;occ['R'-'A']--;
                n -= 4;
                continue;
            }
            if(occ['F'-'A'] > 0){
                number.push_back(5);
                occ['F'-'A']--;occ['V'-'A']--;occ['I'-'A']--;occ['E'-'A']--;
                n -= 4;
                continue;
            }
            if(occ['X'-'A'] > 0){
                number.push_back(6);
                occ['S'-'A']--;occ['I'-'A']--;occ['X'-'A']--;
                n -= 3;
                continue;
            }
            if(occ['S'-'A'] > 0){
                number.push_back(7);
                occ['S'-'A']--;occ['E'-'A']--;occ['V'-'A']--;occ['E'-'A']--;occ['N'-'A']--;
                n -= 5;
                continue;
            }
            if(occ['G'-'A'] > 0){
                number.push_back(8);
                occ['E'-'A']--;occ['I'-'A']--;occ['G'-'A']--;occ['H'-'A']--;occ['T'-'A']--;
                n -=5;
                continue;
            }
            if(occ['T'-'A'] > 0){
                number.push_back(3);
                occ['T'-'A']--;occ['H'-'A']--;occ['R'-'A']--;occ['E'-'A']--;occ['E'-'A']--;
                n -= 5;
                continue;
            }
            if(occ['O'-'A'] > 0){
                number.push_back(1);
                occ['O'-'A']--;occ['N'-'A']--;occ['E'-'A']--;
                n -= 3;
                continue;
            }
            if(occ['N'-'A'] > 0){
                cerr << "kekekek\n";
                number.push_back(9);
                occ['N'-'A']--;occ['I'-'A']--;occ['N'-'A']--;occ['E'-'A']--;
                n -= 4;
                continue;
            }
        }
        sort(number.begin(), number.end());
        wcout << "Case #" << tt << ": ";
        for (int i = 0; i < number.size(); i++){
            cout << number[i];
        }
        cout << endl;
    }
    return 0;
}
