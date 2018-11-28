#include <iostream>

using namespace std;

void small(int k, int c, int s) {
    for (int i=1; i<=k; ++i) {
        cout << " " << i;
    }
}

int main(){
    int tmax, k, c, s;
    cin >> tmax;
    for (int t=1; t<=tmax; ++t) {
        cin >> k >> c >> s;
        cout << "Case #" << t << ":";
        small(k, c, s);
        cout << endl;
    }
    return 0;
}
