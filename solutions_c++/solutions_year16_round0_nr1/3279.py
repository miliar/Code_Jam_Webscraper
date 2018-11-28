//Eldar Gaynetdinov

#include <bits/stdc++.h>
using namespace std;

void f(set<uint64_t>& st, uint64_t n)
{
    while(n > 0)
    {
        st.insert(n % 10);

        n /= 10;
    }
}

int main()
{
    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        uint64_t N; cin >> N;

        if(!N)
        {
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
            continue;
        }

        set<uint64_t> st;

        uint64_t k = N;
        while(true)
        {
            f(st, k);

            if(st.size() == 10) break;

            k += N;
        }

        cout << "Case #" << t << ": " << k << endl;
    }

    return 0;
}
