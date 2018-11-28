#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

char buf[32];

bool inline is_pal(long long v) {
    sprintf(buf, "%lld", v);
    size_t len = strlen(buf);
    for(int i = 0; i < len/2; ++i) {
        if(buf[i] != buf[len - i - 1])
            return false;
    }
    v *= v;
    sprintf(buf, "%lld", v);
    len = strlen(buf);
    for(int i = 0; i < len/2; ++i) {
        if(buf[i] != buf[len - i - 1])
            return false;
    }
    return true;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    
    vector <long long> ans;
    
    for(int i = 1; i <= 10000000; ++i)
        if(is_pal(i))
            ans.push_back(1ll * i * i);
    
    long long a, b;
    for(int t = 1; t <= T; ++t) {
        cin >> a >> b;
        cout << "Case #" << t << ": " <<
            lower_bound(ans.begin(), ans.end(), b + 1) -
            lower_bound(ans.begin(), ans.end(), a) << endl;
    }
    
    return 0;
}
