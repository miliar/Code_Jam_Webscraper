#include <bits/stdc++.h>
using namespace std;
const int N = 1e7 + 5;
long long getinBase10(string cur , int base){
    long long curt = 1;
    long long ret = 0;
    for(int i = cur.size() - 1; i >= 0; --i){
        if(cur[i] == '1'){
            ret += curt;
        }
        curt *= base;
    }
    return ret;
}
int getDivisor(long long int x){
    for(int i = 2; i <= 100; ++i){
        if(x % i == 0) return i;
    }
    return -1;
}
bool composite(long long int x){
    for(int i = 2; i * i <= x; ++i) if(!(x % i)) return true;
    return false;
}
int main(){
    int tt;
    //freopen("mad.txt" , "w" , stdout);
    int n = 16 , j = 50;
    int to = 1 << 14;
    vector < pair < string , vector < int > > > vs;
    for(int i = 0; i < to; ++i){
         string cur = "1";
         for(int j = 0; j < 14; ++j){
            if(i & (1 << j)){
                cur += '1';
            }else cur += '0';
         }
         cur += '1';
         vector < long long int > b10;
         for(int i = 2; i <= 10; ++i){
            b10.push_back(getinBase10(cur , i));
         }
           vector < int > tmp;
           bool ok = true;
            for(int i = 0; i < b10.size(); ++i){
                int y = getDivisor(b10[i]);
                if(y == -1){
                    ok = false;
                    break;
                }
                tmp.push_back(y);
            }
            if(ok)
            vs.push_back(make_pair(cur , tmp) );
    }
         cout << "Case #1:" << endl;
         for(int i = 0; i < vs.size() && i < 50; ++i){
            cout << vs[i].first << " ";
            for(int j = 0; j < vs[i].second.size(); ++j) cout << vs[i].second[j] << " ";
            cout << endl;
         }

    return 0;
}


