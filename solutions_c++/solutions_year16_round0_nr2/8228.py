#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>



using namespace std;

int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    char c;
    cin >> t;
    string str;
    for (int i = 0;i < t;i++){
        cin >> str;
        int ans = 0;
        if (str.size() == 1){
            if (str[0] == '-'){
                printf ("Case #%d: %d\n", i + 1, 1);
            }
            else{
                printf ("Case #%d: %d\n", i + 1, 0);
            }
        }
        else {
            for (int j = 0; j < str.size() - 1; j++) {
                if (str[j] != str[j + 1]){
                    ans++;
                }
            }
            if (str[str.size() - 1] == '-'){
                ans++;
            }
            printf ("Case #%d: %d\n", i + 1, ans);
        }
    }
    return 0;
}