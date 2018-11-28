#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <queue>
#include <utility>

#define ll long long

using namespace std;

char getVal(int i) {
    return ('A'+i-1);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("outputA-large.out", "w", stdout);
    priority_queue <pair<int,int> > pq;
    pair<int,int> p;
    int t, n, i, aa;
    cin >> t;
    for (int ij =1; ij<=t;ij++) {
        cout << "Case #" << ij << ":" ;
        cin >> n;
        for (i=1;i<=n;i++) {
            cin >> aa;
            pq.push(make_pair(aa,i));
        }
        p = pq.top();
        while(p.first!=1) {
            int e1f, e1s, e2f, e2s;
            e1f=p.first;
            e1s=p.second;
            pq.pop();
            p=pq.top();
            e2f=p.first;
            e2s=p.second;
            if (e2f==1) {
                while (e1f>=3) {
                    e1f-=2;
                    cout << " " << getVal(e1s) << getVal(e1s);
                }
                if (e1f==2) cout << " " << getVal(e1s);
                e1f=1;
            }
            else if (e1f - e2f>=2) {
                e1f-=2;
                cout << " " << getVal(e1s) << getVal(e1s);
            }
            else {
                cout << " " << getVal(e1s) << getVal(e2s);
                e1f--; e2f--;
                pq.pop();
                pq.push(make_pair(e2f,e2s));
            }
            pq.push(make_pair(e1f,e1s));
            p=pq.top();
        }
        if (n%2==1) {
            cout << " " << getVal(n);
            n--;
        }
        for (i=1;i<n;i=i+2) cout << " " << getVal(i) << getVal(i+1);
        cout << endl;
    }
}
