#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <tuple>
#include <cmath>
#include <climits>
using namespace std;

#define SORT(l) std::sort(l.begin(), l.end())
#define IS_ALPH(c) ((c>='a' && c<='z') || (c>='A' && c<='Z'))
#define IS_NUM(c) (c>='0' && c<='9')
#define FOR(a, min, max) for(int a=min; a<max; ++a)
#define FORS(a, str) for(int a=0; a<str.length(); ++a)
#define FORV(a, vec) for(int a=0; a<vec.size(); ++a)
#define MAX(a, b) ((a > b) ? (a) : (b))
#define MIN(a, b) ((a < b) ? (a) : (b))
#define COUTV(v) FORV(i,v) { cout << v[i]; if(i<v.size()-1) cout << ","; else cout << endl; }
#define mp(a,b) make_pair(a,b)

map<char, int> ind;
pair<char, bool> quant[4][4] = {   { make_pair('1', false), make_pair('i', false), make_pair('j', false), make_pair('k', false) },
                                    { make_pair('i', false), make_pair('1', true), make_pair('k', false), make_pair('j', true) },
                                    { make_pair('j', false), make_pair('k', true), make_pair('1', true), make_pair('i', false) },
                                    { make_pair('k', false), make_pair('j', false), make_pair('i', true), make_pair('1', true) } };

int main() {
    ind['1'] = 0;
    ind['i'] = 1;
    ind['j'] = 2;
    ind['k'] = 3;

    int cur_case=1;

    int T;
    cin >> T;
    while(T--) {
        
       int L, X;
       cin >> L >> X;

        string input;
        cin >> input;
        string repeated;
        for(int i=0; i<X; ++i) {
            repeated += input;
        }
       
        if(repeated.length() < 3) {
            cout << "Case #" << cur_case++ << ": NO" << endl;
            continue;
        }

        vector<int> left_indices;
        vector<int> right_indices;

        //fill the left indices
        char cur_char = repeated[0];
        bool is_neg = false;
        if(cur_char=='i') left_indices.push_back(0);
        for(int i=1; i<repeated.size()-2; ++i) {
            if(cur_char=='i' && !is_neg) {
                left_indices.push_back(i-1);
            }

            bool cur_char_neg = quant[ind[cur_char]][ind[repeated[i]]].second;
            cur_char = quant[ind[cur_char]][ind[repeated[i]]].first;

            if(cur_char_neg && is_neg) is_neg = false;
            else if(cur_char_neg || is_neg) is_neg = true;
        }

        set<int> k_positions;
        cur_char = repeated[repeated.length()-1];
        is_neg = false;
        if(cur_char=='k') k_positions.insert(repeated.length()-1);
        for(int i=repeated.length()-2; i>2; --i) {
            if(cur_char=='k' && !is_neg) {
                k_positions.insert(i+1);
            }

            bool cur_char_neg = quant[ind[repeated[i]]][ind[cur_char]].second;
            cur_char = quant[ind[repeated[i]]][ind[cur_char]].first;

            if(cur_char_neg && is_neg) is_neg = false;
            else if(cur_char_neg || is_neg) is_neg = true;
        }

        bool success = false;
        for(int i=0; !success && i<left_indices.size(); ++i) {
           //cout << "here" << endl; 
            cur_char = repeated[left_indices[i]+1];

            if(cur_char=='j' && k_positions.count(left_indices[i]+2)) {
                success = true;
                break;
            }

            is_neg = false;
            for(int m=left_indices[i]+2; m<repeated.size(); ++m) {
                //cout << "at pos: " << m << ": " << repeated[m] << " cur char: " << (is_neg ? "-" : "") << cur_char << endl;

                bool cur_char_neg = quant[ind[cur_char]][ind[repeated[m]]].second;
                cur_char = quant[ind[cur_char]][ind[repeated[m]]].first;

                if(cur_char_neg && is_neg) is_neg = false;
                else if(cur_char_neg || is_neg) is_neg = true;

                if(cur_char=='j' && !is_neg && k_positions.count(m+1)) {
                    //cout << left_indices[i] + 1 << " - " << m << " - " << repeated.length()-1 << endl;

                    success = true;
                    break;
                }
            }
        }

        cout << "Case #" << cur_case++ << ": ";
        if(success)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
