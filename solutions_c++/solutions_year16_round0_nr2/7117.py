#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve(string& st) {
    int index = st.size()-1;
    int ans = 0;
    while(index >= 0) {
        while(index >= 0 && st[index] == '+')
            index--;
        if(index < 0)
            break;

        for(int i=0;i<=index;++i) {
            if(st[i] == '+')
                st[i] = '-';
            else
                st[i] = '+';
        }
        ++ans;
    }
    return ans;
}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int ii=1;ii<=tc;++ii) {
        string st;
        cin >> st;
        printf("Case #%d: %d\n", ii, solve(st));
    }
    return 0;
}
