//
//  main.cpp
//  Standing Ovation
//
//

#include <iostream>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-large.in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, pid=1;
    for (cin>>T;T--;) {
        cout << "Case #" << pid++ << ": ";
        int smax;
        char s[1200];
        int total = 0;
        int au = 0;
        scanf("%d %s", &smax, s);

        if (smax == 0) {
            if (s[0] - '0' <= 0) cout << "1\n";
            else cout << "0\n";
            continue;
        }
        
        for (int i = 1; i <= smax; ++i) {
            total += (s[i-1] - '0');
            if (total < i) au += i - total, total = i;
        }
        cout << au <<"\n";
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
