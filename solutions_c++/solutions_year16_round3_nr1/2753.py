#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


class node {
public:
    int k,tp;
    node() {
        k=0,tp=0;
    }
    bool operator < (node b)const {
        return k < b.k;
    }


};

void show(priority_queue<node>& ko) {

    priority_queue<node> tmp;
    while(!ko.empty()) {
        cout << ko.top().k << " ";
        tmp.push(ko.top());
        ko.pop();
    }
    cout << endl;
    ko = tmp;

}



int main() {
    freopen("A-large.in","r",stdin);
    freopen("AAAAA.txt","w",stdout);
    int tests;
    cin >> tests;
    for(int t=1; t<=tests; t++) {
        int n;
        cin >> n;
        priority_queue<node> pq;
        while(!pq.empty()) pq.pop();
        for(int i=0; i<n; i++) {
            int foo;
            cin >> foo;
            node f = node();
            f.k = foo;
            f.tp = i;
            pq.push(f);
        }
        printf("Case #%d: ",t);
        while(1) {
            if(pq.top().k == 1) {
                //cout << endl;
                break;
            }
            node tmp = pq.top();
            pq.pop();
            node tmp2 = pq.top();
            pq.pop();
            if(tmp.k == tmp2.k) {
                cout << (char)(tmp.tp + 'A') << (char) (tmp2.tp + 'A');
                tmp.k--;
                tmp2.k--;
                pq.push(tmp);
                pq.push(tmp2);
            } else {
                for(int j=tmp2.k; j<tmp.k; j++) {
                    cout << (char)(tmp.tp + 'A');
                    if(j != tmp.k-1) cout << " ";
                }
                tmp.k = tmp2.k;
                pq.push(tmp);
                pq.push(tmp2);
            }
            cout <<" ";
        }
        priority_queue<node> dx;
        while(!dx.empty()) dx.pop();
        while(!pq.empty()) {
            node r = pq.top();
            pq.pop();
            if(r.k == 0) break;

            dx.push(r);
        }
        if(dx.empty()) continue;
        if(dx.size()&1) {
            cout << (char)(dx.top().tp + 'A') << " ";
            dx.pop();
        }
        while(!dx.empty()) {
            node tx,pv;
            tx = dx.top();
            dx.pop();
            pv = dx.top();
            dx.pop();
            cout << (char)(tx.tp + 'A') << (char)(pv.tp + 'A');
            if(dx.size()==0) puts("");
            else cout << " ";
        }


    }




}
