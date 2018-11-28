#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <map>

using namespace std;

char *vals[4] = {"1ijk", "i1kj", "jk1i", "kji1"};
bool signs[4][4] = {1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0};

int main(){
    freopen("./input.txt", "r", stdin);
    freopen("./output.txt", "w", stdout);

    map<char, int> m;
    m['1'] = 0;
    m['i'] = 1;
    m['j'] = 2;
    m['k'] = 3;

    int T;
    cin >> T;
    for(int test=1; test<=T; test++){

        bool res;
        string tmp, str;

        long long x;
        int l;
        cin >> l >> x;
        cin >> tmp;


        for(int i=0; i<x; i++){
            str += tmp;
        }

        int sz = str.size();
        if(sz < 3) {
            cout << "Case #" << test << ": " << "NO";
            if(test < T) cout << endl;
            continue;
        }


        long long pos_i = -1, pos_k = str.size();
        bool find_i = false, find_k = false;

        int cur_val = m[str[0]];
        char muti_val = str[0];
        bool sign = true;

        if(str[0] == 'i') {
            pos_i = 0;
            find_i = true;
        }

        for(int i=1; i<sz; i++){
            cur_val = m[str[i]];
            int index = m[muti_val];
            muti_val = vals[index][cur_val];

            sign = !(sign^signs[index][cur_val]);
            if(!find_i && sign == 1 && muti_val == 'i') {
                pos_i = i;
                find_i = true;
            }
        }

        char muti_val_r = str[sz-1];
        bool sign_r = true;

        if(str[sz-1] == 'k') {
            pos_k = sz-1;
            find_k = true;
        }

        for(int i=sz-2; i>=0; i--){
            int cur_val = m[str[i]];
            int index = m[muti_val_r];
            muti_val_r = vals[cur_val][index];

            sign_r = !(sign_r^signs[cur_val][index]);
            if(sign_r == 1 && muti_val_r == 'k') {
                pos_k = i;
                find_k = true;
                break;
            }
        }
//        int temp_index = m[muti_val];
//        bool temp_sign = sign;
//
//        for(int i=1; i<x; i++){
//            int index = m[muti_val];
//
//            muti_val = vals[index][temp_index];
//            sign = !(temp_sign^sign);
//            sign = !(sign^signs[index][temp_index]);
//
//        }
//        cout << (sign ? "" : "-") << muti_val << endl;
        if(sign == 1 || muti_val != '1'){
            res = false;
        }
        else if(find_i && find_k && pos_i < pos_k){
            res = true;
        }
        else
            res = false;

        cout << "Case #" << test << ": " << (res ? "YES" : "NO");
        if(test < T) cout << endl;

    }
    return 0;
}
