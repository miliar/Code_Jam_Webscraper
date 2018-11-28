#include <bits/stdc++.h>
#define ll long long
#define MOD 1000000007
#define s(x) sanf("%d", &x);
using namespace std;
int a[100005];
int main() {
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large_output.txt", "w", stdout);
    int test,n;
    int testcases = 0;
    set<int> s;
    cin >> test;
    while(test--) {
        s.clear();
        cin >> n;
        testcases++;
        for(int i = 1; i <= 2000005; i++) {
            long long temp = (ll)i*(ll)n;
            while(temp != 0) {
                s.insert(temp%10);
                temp = temp/10;
            }
            if(s.size() == 10) {
                cout << "Case #"<<testcases<<": " << (ll)((ll)i*(ll)n) << endl;
                break;
            }
        }
        if(s.size() != 10) {
            cout << "Case #"<<testcases<<": " << "INSOMNIA" << endl;
        }
    }
    return 0;
}
