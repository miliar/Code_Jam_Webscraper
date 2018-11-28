#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++i){
        int t;
        cin >> t;
        string s;
        cin >> s;
        int standing = 0;
        int need = 0;
        for(int j = 0; j < s.size(); ++j){
            int c = s[j] - '0';
            if(standing < j) need += j - standing, standing = j;
            standing += c;
        }
        printf("Case #%d: %d\n", i, need);
    }
}
