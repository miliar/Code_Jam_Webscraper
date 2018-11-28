#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

vector<long long> palin;

bool chech_pal(long long n) {
    vector<int> a;
    while(n > 0) {
        a.push_back(n % 10);
        n /= 10;
    }
    int i = 0, l = (int)a.size();
    while(i < l && a[i] == a[l - i - 1])
        i++;
    return i == l;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    for(long long i = 1; i <= 10000000; i++)
        if(chech_pal(i) && chech_pal(i * i))
            palin.push_back(i * i);
    int T;
    long long a, b;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> a >> b;
        long long l = palin.size();
        int i = 0, ans = 0;
        while(palin[i] < a && i < l)
            i++;
        while(palin[i] >= a && palin[i] <= b && i < l) {
            i++;
            ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
