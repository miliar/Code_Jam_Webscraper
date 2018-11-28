#include<iostream>
#include<cstring>
#include<cstdio>
#include<deque>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Outlarge.out", "w", stdout);
    int tt, maxi;
    string s;
    deque<int> res;
    cin >> tt;
    for(int t = 0; t < tt; t++){
        cout << "Case #" << t + 1 << ": ";
        res.clear();
        cin >> s;
        res.push_back((int)(s[0] - 'A'));
        for(int i = 1; i < s.size(); i++) {
            if(int(s[i] - 'A') >= res.at(0)){
                res.push_front((int)(s[i] - 'A'));
            } else {
                res.push_back((int)(s[i] - 'A'));
            }
        }
        for(int i = 0; i < res.size(); i++) {
            cout << char(char(res.at(i)) + 'A');
        }
        cout << endl;
    }
    return 0;
}
