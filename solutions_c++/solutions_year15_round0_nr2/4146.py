#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <ctime>
#include <stack>
#include <sstream>
#include <fstream>
#include <limits.h>
using namespace std;

int man, maxval;

void abcx(priority_queue <int> que, int time)
{
    int i,x;
    if(time == maxval) return;

    man = min(man, time+que.top());
    if (que.top() != 1) {
        x = que.top();
        que.pop();
        for (i = 1; i <= x/2; i++) {
            priority_queue <int> tp;
            tp = que;
            tp.push(i);
            tp.push(x-i);
            abcx(tp, time+1);
        }
    }
}

int main()
{
    FILE *fi,*fo;
    int t, n, xo, i, cid;
    fi = fopen("inp_b.txt","r");
    fo = fopen("out_b.txt","w+");
    //freopen("inp_b.txt", "r", stdin);
    //freopen("out_b.txt", "w", stdout);
    //cin >> t;
    fscanf(fi,"%d",&t);
    for (cid = 1; cid <= t; cid++) {
        //cin >> n;
        fscanf(fi,"%d",&n);
        man = INT_MAX;
        priority_queue <int> que;
        for (i = 0; i < n; i++) {
            //cin >> x;
            fscanf(fi,"%d",&xo);
            que.push(xo);
        }
        maxval = que.top();
        abcx(que, 0);
        fprintf(fo,"Case #%d: %d\n",cid,man);
        /*cout << "Case #" << ++u << ": ";
        cout << man << endl;*/
    }
    return 0;
}
