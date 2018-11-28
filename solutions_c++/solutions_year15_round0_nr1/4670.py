#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
string s;
vector<int> v;
int Go(){
    v.clear();
    int maxShyness;
    cin >> maxShyness;
    cin >> s;
    v.resize(maxShyness+1);
    for(int i = 0; i < s.size(); i++){
        v[i] = s[i]-'0';
    }
    int temp = v[0];
    int result=0;
    for(int i = 1; i < v.size(); i++){
        result += max(0, i-temp);
        temp += max(0, i-temp);
        temp += v[i];
    }
    //cout << "\n";
    return result;
}

int main(){
    int t;
    cin >> t;
    for(int _q = 0; _q < t; _q++){
        int res = Go();
        printf("Case #%d: %d\n", _q+1, res);
    }
}
