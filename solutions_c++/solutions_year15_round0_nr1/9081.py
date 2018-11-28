#include <cstdio>
#include <iostream>

using namespace std;

string s;
int input[1010];

int main() {
    int t;
    cin>>t;
    int n,ans,people;
    for(int testNO = 1; testNO <= t; testNO++) {
        cin>>n;
        cin>>s;

        for (int i = 0; i <= n; ++i) {
            input[i] = s[i] - '0';
        }

        ans = 0,people = input[0];

        for(int i = 1; i <= n; i ++) {
            if(people < i && input[i] > 0) {
                ans += (i - people);
                people += (i-people);
            }

            people += input[i];
        }

        printf("Case #%d: %d\n",testNO,ans);

    }
    return 0;
}