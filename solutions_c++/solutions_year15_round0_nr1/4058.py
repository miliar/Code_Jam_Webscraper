#include <bits/stdc++.h>
#define optimizar ios_base::sync_with_stdio(0); cin.tie(0)
using namespace std;

int n;
string people;

int solved() {
    int cuantos = 0;
    int resp = 0;
    for(int i=0; i <= n; i++) {
        people[i]-= '0';
        if(people[i] != 0) {
            while(cuantos < i) {
                resp++;
                cuantos++;
            }
        }
        cuantos+= people[i];
    }
    return resp;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    optimizar;
    int T;
    cin >> T;
    for(int cases = 1; cases <= T; cases++) {
        cin >> n;
        cin >> people;
        cout << "Case #" << cases << ": " << solved() << "\n";
    }
    return 0;
}
