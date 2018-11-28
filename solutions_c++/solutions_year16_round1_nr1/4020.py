#include <bits/stdc++.h>
using namespace std;



int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    string str;
    for(int i = 1; i <= t; ++i) {
        deque<char> dq;
        cin>>str;
        dq.push_back(str[0]);
        int l = str.length();
        for(int j=1;j<l;++j) {
            if(int(str[j])>=int(dq[0]))
                dq.push_front(char(str[j]));
            else
                dq.push_back(char(str[j]));
        }

        cout << "Case #" << i << ": ";
        for(int j=0;j<l;++j)
            cout<<dq[j];
        cout<<'\n';

    }

	return 0;
}