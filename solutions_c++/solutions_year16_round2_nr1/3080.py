#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;
using ull = unsigned long long;

std::string number[10] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
};

int toInt(double d){
    int i = int(d);
    if(d - i > 0.5){
        i += 1;
    }
    return i;
}

std::string toStr(double a[26][11]){
    std::stringstream oss;
    for(int i = 0; i < 26; ++i){
        for(int j = 0; j < 10; ++j){
            oss << a[i][j] << " ";
        }oss << endl;
    }
    return oss.str();
}

int main(){
    
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        
        sort(s.begin(), s.end());
        
        double a[26][10 + 1] = {0};
        
        for(int i = 0; i < 10; ++i){
            for(int j = 0; j < number[i].size(); ++j){
                a[number[i][j] - 'A'][i] += 1;
            }
        }
        for(int i = 0; i < s.size(); ++i){
            a[s[i] - 'A'][10] += 1;
        }
        
        int M = 26, N = 10;
        int mrk[26] = {0};
        //cerr << toStr(a);
        for (int j = 0; j < N; ++j){
            int m = 0;
            while(a[m][j] == 0 || mrk[m]){
                ++m;
                // cerr << m << " " << a[m][j] << " " << mrk[m] << endl;
                // assert(m < 26);
            }
            mrk[m] = 1;
            double pivot = a[m][j];
            for (int n = 0; n < N + 1; ++n){
                a[m][n] /= pivot;
            }
            for (int k = 0; k < M; ++k){
                if(k != m){
                    double mul = a[k][j];
                    for (int n = 0; n < N + 1; ++n)
                    {
                        a[k][n] -=  mul * a[m][n];
                    }
                }
            }
            //cerr << toStr(a);
        }
        //cerr << endl;
        
        int ret[10] = {0};
        for(int i = 0; i < 10; ++i){
            for(int m = 0; m < 26; ++m){
                if(toInt(a[m][i])){
                    ret[i] += toInt(a[m][10]);
                }
            }
        }
        for(int i = 0; i < 10; ++i){
            for(int j = 0; j < ret[i]; ++j){
                cout << i;
            }
        }
        cout << endl;
    }
    return 0;
}