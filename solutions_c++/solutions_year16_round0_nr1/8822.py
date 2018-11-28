#include <bits/stdc++.h>

using namespace std;

void instance(int T) {
    long long n; cin >> n;
    if(n == 0) {
        cout << "Case #" << T << ": " << "INSOMNIA" << endl;
        return;
    }
    long long sum = n;
    vector<int> seen(10);
    while(std::accumulate(seen.begin(), seen.end(), 0) != 10) {
        string s = std::to_string(sum);
        //cout << s << endl;
        for(char &c : s) seen[c - '0'] = 1;
        sum += n;
    }
    cout << "Case #" << T << ": " << sum - n << endl;
}

int main()  {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        instance(t + 1);
    }
}
