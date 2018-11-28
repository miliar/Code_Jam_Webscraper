//Eldar Gaynetdinov
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        int N; cin >> N;

        vector< pair<int, char> > v(N);

        int sum = 0;

        for(int i = 0; i < N; i++)
        {
            cin >> v[i].first;

            sum += v[i].first;

            v[i].second = 'A' + i;
        }

        sort(begin(v), end(v));

        vector<string> ans;

        while(v.back().first)
        {
            assert(v[N - 2].first);

            if(sum % 2)
            {
                ans.push_back(string(1, v[N - 1].second));

                v[N - 1].first--;

                sum--;
            }
            else
            if(v[N - 1].first == v[N - 2].first)
            {
                string k;

                k += v[N - 1].second;
                k += v[N - 2].second;

                ans.push_back(k);

                v[N - 1].first--;
                v[N - 2].first--;
            }
            else
            {
                assert(v[N - 1].first >= 2);

                ans.push_back(string(2, v[N - 1].second));

                v[N - 1].first -= 2;
            }

            sort(begin(v), end(v));

            int acc = 0;
            for(auto& pr : v)
                acc += pr.first;

            assert(v.back().first <= acc / 2);
        }

        cout << "Case #" << t << ": ";

        for(auto& x : ans) cout << x << ' ';
        cout << endl;
    }

    return 0;
}
