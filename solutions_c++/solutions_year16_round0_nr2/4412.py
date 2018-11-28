using namespace std;

#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <typeinfo>

int count(string s) {
    int l = s.length();
    int res = 0;
    
    for (int i = 0; i < l - 1; i++)
        if (s[i] != s[i + 1])
            res++;
    if (s[l - 1] == '-')
        res++;
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    string s;
    
    for (int t = 0; t < T; t++) {
        cin >> s;
        cout << "Case #" << t + 1 << ": ";
        
        int p = count(s);
        cout << p;
        
        cout << endl;
    }
    return 0;
}
