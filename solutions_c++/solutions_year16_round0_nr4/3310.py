#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <vector>
#include <set>
#include <string>

typedef long long int lli;

using namespace std;

lli k, s, c;

void solveit(){
    cin >> k >> c >> s;
    for (int i = 1; i < s + 1; i++){
        cout << i << " ";
    }
    cout << "\n";
}

int main(){
    freopen("D_small.out", "w+", stdout);
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++){
        printf("Case #%d: ", i + 1);
        solveit();
    }
}


