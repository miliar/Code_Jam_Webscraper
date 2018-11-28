#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<time.h>
#include<stdlib.h>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#define LL long long
using namespace std;
int ans[4][4][4] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1};
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int cse = 1;
    while(T--)
    {
        int x, r, c;
        cin >> x >> r >> c;
        string s;
        if(ans[x - 1][r - 1][c - 1])
            s += "GABRIEL";
        else
            s += "RICHARD";
        cout << "Case #" << cse++ << ": " << s << endl;
    }
    return 0;
}

