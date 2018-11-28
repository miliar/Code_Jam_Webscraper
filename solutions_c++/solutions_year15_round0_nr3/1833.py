#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

const int Mn = 10000 + 10;
int map[5][5] = {
                    { 0, 0, 0, 0, 0},
                    { 0, 1, 2, 3, 4},
                    { 0, 2,-1, 4,-3},
                    { 0, 3,-4,-1, 2},
                    { 0, 4, 3,-2,-1}
                };
int s[Mn],a[Mn];
int multi(int x,int y) {
    int flag(1);
    if(x < 0)
        flag = -flag, x = -x;
    if(y < 0)
        flag = -flag, y = -y;
    return flag * map[x][y];
}
int divide(int x,int y) {
    for(int i = -4; i <= 4; ++i)
        if(i != 0) {
            if(multi(x,i) == y)
                return i;
        }
}
int to_num(char c) {
    if(c == '1')
        return 1;
    if(c == 'i')
        return 2;
    if(c == 'j')
        return 3;
    if(c == 'k')
        return 4;
}
bool check(int len) {
    for(int i = 1; i < len; ++i) {
        for(int j = 1; j < i; ++j) {
            if(s[j] == 2 && divide(s[j],s[i]) == 3 && divide(s[i],s[len]) == 4)
                return true;
        }
    }
    return false;
}
int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,L,X;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        cin >> L >> X;
        string str;
        cin >> str;
        for(int i = 0; i < str.size(); ++i) {
            a[i + 1] = to_num(str[i]);
        }
        for(int i = 2; i <= X; ++i)
            for(int j = 1; j <= L; ++j)
                a[j + (i-1) * L] = a[j];
        int len = L * X;
        s[0] = 1;
        for(int i = 1; i <= len; ++i)
            s[i] = multi(s[i - 1], a[i]);
        printf("Case #%d: %s\n",cas,check(len) ? "YES" : "NO");
    }
    return 0;    
}
