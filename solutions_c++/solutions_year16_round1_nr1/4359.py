#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in1.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    string s;
    list<char> l;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        cin >> s;
        l.clear();
        l.insert(l.begin(), s[0]);
        for(int j = 1; j < s.size(); j++){
            if(s[j] < *l.begin())l.push_back(s[j]);
            else l.push_front(s[j]);
        }
        string nsr(l.begin(), l.end());
        printf("Case #%d: %s\n", i, &nsr[0]);
    }
    return 0;
}
