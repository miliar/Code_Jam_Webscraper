#include<bits/stdc++.h>
using namespace std;

void update_visited(int& visited, int number) {
    while(number) {
        visited|=(1<<(number%10));
        number/=10;
    }
}

static const int dbg = 0;
#define dout if(dbg)cout

void solve() {
    string pancakes;
    cin >> pancakes;
    int counter = 0;
    bool state = true;
    for(int i=pancakes.length()-1; i>=0; --i) {
        dout << "DEBUG i = " << i << " counter = " << counter << endl; 
        dout << "state = " << state << " pancakes[i] " << pancakes[i] << endl;
        if( (state == true  && pancakes[i] == '-') || 
            (state == false && pancakes[i] == '+')) {
            ++counter;
            state = !state;
        }
    }
    cout << counter << endl; 
}

int main() {
    int n_testcases, start_number;
    scanf("%d", &n_testcases);
    for(int i=1; i<=n_testcases; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
