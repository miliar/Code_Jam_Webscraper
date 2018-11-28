#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
string tostring(int len, int n){
    string x = "";
    int a = 0;
    while(n){
        x = (char)(n%10 + '0') + x;
        n /= 10;
        a++;
    }
    while(a < len){
        a++;
        x = "0" + x;
    }
    return x;
}
bool ok(string x, string y){
    for(int i = 0; i < x.size(); i++){
        if(x[i] == '?')
            continue;
        if(x[i] != y[i])
            return false;
    }
    return true;
}
int main(){
    int T = 200;
    string C, J;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> C >> J;
        int lc = C.size();
        vector<int>a, b;
        int p = 10;
        if(lc == 2)
            p = 100;
        else if(lc == 3)
            p = 1000;
        for(int i = 0; i < p; i++){
            string c = tostring(lc, i);
            if( ok(C, c) )
                a.push_back(i);
            if( ok(J, c) )
                b.push_back(i);
        }
        int m1 = -10000, m2 = 10000;
        for(int i = 0; i < a.size(); i++){
            for(int j = 0; j < b.size(); j++){
                if( abs(a[i] - b[j]) < abs( m1 - m2  ) ){
                    m1 = a[i], m2 = b[j];
                }
            }
        }
        cout << "Case #" << t << ": " << tostring(lc, m1) << " " << tostring(lc, m2) << endl;
    }
    return 0;
}
