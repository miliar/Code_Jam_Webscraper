#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

int trii(priority_queue<int> q){
    priority_queue <int> q1,q2;
    q1 = q;
    q2 = q;
    int x = q1.top();
    //cout << "X" << x << endl;
    if (!x) {
        //cout << "V" << 0 << endl;
        return 0;
    }
    if (x == 1 || x == 2 || x == 3){
        //cout << "V" << x << endl;
        return x;
    }
    q1.pop();
    q1.push((x+1)/2);
    q1.push(x / 2);
    q2.pop();
    q2.push((x+2)/3);
    q2.push((x+1)/3);
    q2.push(x/3);
    int x1 = trii(q1);
    int x2 = trii(q2);
    //cout << "VV" << x << " " << x1 << " " << x2 << endl;
    return min(x,min(1+x1,2+x2));
}

int cmp(int a, int b){
    return a > b;
}

int main(){
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt){
        int n;
        cin >> n;
        int x;
        priority_queue<int> q;
        for (int i = 0; i < n; ++i){
            cin >> x;
            q.push(x);
        }
        printf("Case #%d: %d\n", (tt+1), trii(q));
    }
    return 0;
}
