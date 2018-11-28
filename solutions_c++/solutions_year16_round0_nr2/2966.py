#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

void getCnt(int c, const string& s){
    int i=0;
    int cnt = 0;
    int n = s.size();
    if(s[0] == '-'){
        ++cnt;
        while(i < n && s[i] == '-'){
            ++i;
        }
    }
    while(i < n){
        while(i < n&& s[i] == '+') ++i;
        if(i >= n) break;
        cnt += 2;
        while(i < n&& s[i] == '-') ++i;
    }
    cout << "Case #" << c <<": " << cnt << endl;
}

int main()
{
    int cnt;
    cin >> cnt;
    string s;
    for(int i=1; i<=cnt; i++){
        cin >> s;
        getCnt(i, s);
    }
    return 0;
}
