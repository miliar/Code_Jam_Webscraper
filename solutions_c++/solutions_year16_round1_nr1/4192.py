#include <bits/stdc++.h>
using namespace std;



int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    string S;
    for(int i = 1; i <= t; ++i) {
        deque<char> V;
        cin>>S;
        V.push_back(S[0]);
        int l = S.length();
        for(int j=1;j<l;++j) {
            if(int(S[j])>=int(V[0]))
                V.push_front(char(S[j]));
            else
                V.push_back(char(S[j]));
        }

        cout << "Case #" << i << ": ";
        for(int j=0;j<l;++j)
            cout<<V[j];
        cout<<'\n';

    }

	return 0;
}