
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int main( void ) {

    freopen("input_b.txt", "r", stdin);
    freopen("output_b.txt", "w", stdout);

    int t;
    cin >> t;

    for(int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);

        string s;
        cin >> s;

        s += "#";

        vector< pair<char, int> > A;
        char cur_sym = s[0];
        int cur_count = 1;

        for(int i = 1; i < (int)s.size(); i++) {
            if(s[i] == cur_sym) cur_count += 1;
            else {
                A.push_back({cur_sym, cur_count});
                cur_sym = s[i];
                cur_count = 1;
            }
        }

        reverse(A.begin(), A.end());

        long long answer = 0;

        while((int)A.size() > 1) {
            auto p = A.back(); A.pop_back();
            auto q = A.back(); A.pop_back();
            q.second += p.second;
            answer += 1;
            A.push_back(q);
        }

        if(A[0].first == '-')
            answer += 1;

        cout << answer << endl;
    }
    return 0;
}
