#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <vector>
#include <set>
#include <string>

using namespace std;

string s;

void solveIt(){
    cin >> s;
    s += "+";
    int ans = 0;
    char lastsymbol = s[0];
    for (int i = 1; i < s.size(); i++){
        if (s[i] != lastsymbol){
            ans++;
            lastsymbol = s[i];
        }
    }
    printf("%d\n", ans);
}

int main(){
    freopen("B_small.out", "w+", stdout);
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++){
        printf("Case #%d: ", i + 1);
        solveIt();
    }
    return 0;
}
