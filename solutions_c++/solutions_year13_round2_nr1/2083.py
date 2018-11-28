#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

bool cmp(int a, int b) {
    return a>b;
}

struct mote {
    int a;
    int steps;
    vector <int> o;
};



int main()
{
    int T;
    cin >> T;
    for (int t=0; t<T; t++) {
        int a,N;
        cin >> a >> N;
        mote m;
        int ans;
        m.a = a;
        m.steps = 0;
        for (int i=0; i<N; i++) {
            int x;
            cin >> x;
            m.o.push_back(x);
        }
        sort(m.o.begin(),m.o.end(),cmp);
        queue <mote> q;
        q.push(m);
        while (!q.empty()) {
            mote mm = q.front();
            q.pop();
            while (!mm.o.empty() && mm.a > mm.o.back()) {
                mm.a += mm.o.back();
                mm.o.pop_back();
            }
            if (mm.o.empty()) {
                ans = mm.steps;
                break;
            }
            mote mm1(mm);
            mote mm2(mm);
            mm1.steps++;
            mm2.steps++;

            mm1.o.push_back(mm1.a - 1);
            mm2.o.erase(mm2.o.begin());

            q.push(mm1);
            q.push(mm2);
        }

        cout << "Case #"<<(t+1)<<": " << ans << endl;
    }
    return 0;
}

