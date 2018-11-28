#include <iostream>
#include <cstdio>
using namespace std;
struct elem {
    int p,r,s;
    string seq;
};
void print (elem e) {
    cout << "<" << e.seq << ">" << endl;
}


int n;
int p0,r0,s0;

elem fun (int depth, char left, char right) {
    if (depth == 0) {
        elem ans;
        ans.p = 0; ans.r = 0; ans.s = 0;
        if (left == 'P') ans.p++;
        if (left == 'S') ans.s++;
        if (left == 'R') ans.r++;
        if (right == 'P') ans.p++;
        if (right == 'S') ans.s++;
        if (right == 'R') ans.r++;
        ans.seq = string(1, left) + string(1, right);
        if (left > right) ans.seq = string(1, right) + string(1, left);
        if (ans.p > p0 || ans.r > r0 || ans.s > s0) ans.p = -1;
        return ans;
    }

    elem ans1, ans2;
    if (left == 'P') ans1 = fun (depth - 1, 'P', 'R');
    if (left == 'S') ans1 = fun (depth - 1, 'P', 'S');
    if (left == 'R') ans1 = fun (depth - 1, 'R', 'S');
    if (right == 'P') ans2 = fun (depth - 1, 'P', 'R');
    if (right == 'S') ans2 = fun (depth - 1, 'P', 'S');
    if (right == 'R') ans2 = fun (depth - 1, 'R', 'S');

    //print(ans1); print(ans2);

    elem ans;
    ans.p = -1;
    if (ans1.p == -1 || ans2.p == -1) { ans.seq = "aa"; return ans; }

    ans.p = ans1.p + ans2.p;
    ans.r = ans1.r + ans2.r;
    ans.s = ans1.s + ans2.s;

    if (ans.p > p0 || ans.r > r0 || ans.s > s0) { ans.p = -1; return ans; }

    ans.seq = ans1.seq + ans2.seq;
    if (ans1.seq > ans2.seq) ans.seq = ans2.seq + ans1.seq;

    return ans;
}

int main()
{
    //r0 = 100; p0=100; s0=100;
    //print( fun (1, 'S', 'R') );



    //return 0;


    int cnt; scanf("%d", &cnt);

    for (int task = 1; task <= cnt; task ++) {
        scanf("%d%d%d%d", &n, &r0, &p0, &s0); n--;

        string sol = "";

        elem ans = fun (n, 'P', 'R'); //print(ans);
        if (ans.p >= 0) if (ans.seq < sol || sol == "") sol = ans.seq;

        ans = fun (n, 'P', 'S'); //print(ans);
        if (ans.p >= 0) if (ans.seq < sol || sol == "") sol = ans.seq;

        ans = fun (n, 'S', 'R'); //print(ans);
        if (ans.p >= 0) if (ans.seq < sol || sol == "") sol = ans.seq;

        if (sol == "") sol = "IMPOSSIBLE";

        cout << "Case #" << task << ": " << sol << endl;
    }

    return 0;
}
