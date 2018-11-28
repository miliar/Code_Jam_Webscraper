//Eldar Gaynetdinov
#include <bits/stdc++.h>
using namespace std;

void print_list(int S)
{
    for(int i = 1; i <= S; i++)
    {
        cout << i;

        if(i != S) cout << ' ';
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        int K, C, S; cin >> K >> C >> S;

        assert(K == S);

        cout << "Case #" << t << ": ";

        print_list(S);

        cout << endl;
    }

    return 0;
}
