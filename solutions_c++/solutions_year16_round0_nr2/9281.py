#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <vector>

#define F first
#define S second

using namespace std;

    int n;
    string s;
    void alpha(string s, int j){
        int k=0;
        for(int i=1; i<s.length(); i++) if(s[i]!=s[i-1]) k++;
        if(s[s.length()-1] == '-') cout << "Case #" << j << ": " << k+1 << "\n";
            else cout << "Case #" << j << ": " << k << "\n";
    }

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> s;
        alpha(s, i+1);
    }
}
