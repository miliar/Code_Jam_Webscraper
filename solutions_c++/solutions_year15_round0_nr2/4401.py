#include<bits/stdc++.h>
using namespace std;
vector<int> data;
vector<int> p;
vector<int> q;
int cmp(const int &a, const int &b) {
    return (int)ceil((double)p[a]/q[a]) > (int)ceil((double)p[b]/q[b]);
}

int main() {
    int t;
    cin >> t;
    for(int _t = 1; _t <= t; _t++) {
        int d, m = 0;
        int ans, nans;
        p.clear();
        q.clear();
        data.clear();
        cin >> d;
        for(int i=0;i<d;i++) {
            int a;
            cin >> a;
            p.push_back(a);
            q.push_back(1);
            data.push_back(i);
        }
        sort(data.begin(),data.end(),cmp);
        ans = p[data[0]];
        nans = ans;
        while(q[data[0]]!=p[data[0]]) {
            m += 1;
            nans = m;
            q[data[0]] += 1;
            sort(data.begin(),data.end(),cmp);
            nans += (int)ceil((double)p[data[0]]/q[data[0]]);

//            cout << "\t->";
//            for(int i=0;i<d;i++)
//                cout << p[data[i]] << " ";
//            cout << endl;
//            cout << "\t->";
//            for(int i=0;i<d;i++)
//                cout << q[data[i]] << " ";
//            cout << endl;
//            cout << "\t->Nans: " << nans << endl;

            if(nans < ans)
                ans = nans;
//            else if(nans > ans)
//                break;
        }
        printf("Case #%d: %d\n", _t, ans);
    }
    return 0;
}
