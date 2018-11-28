#include <bits/stdc++.h>
#define ll long long
#define MOD 1000000007
#define s(x) scanf("%d", &x);

using namespace std;
int a[100005];
int main() {
    ios::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large_output.txt", "w", stdout);
    int test;
    cin >> test;
    int testcases = 0;
    string s;
    int n , solution,i ;
    while(test--) {
        cin>>s;
        testcases++;
        n = s.size();
        i = 0;
        if( s == "-") {
            solution = 1;
        } else if( s == "+") {
            solution = 0;
        }else {
            solution = 0;
            if( s[0] == '+') {
                for(int i = 1; i < n; i++) {
                    if( s[i-1] == '+' && s[i] == '-')
                        solution = solution+ 2;
                }
            }else if( s[0] == '-') {
                solution = 1;
                for(int i = 1; i < n; i++) {
                    if( s[i-1] == '+' && s[i] == '-')
                        solution = solution+2;
                }
            }
        }
        cout << "Case #"<<testcases<<": " << solution << endl;
    }
    return 0;
}
