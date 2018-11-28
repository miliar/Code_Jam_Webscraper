#include <iostream>
#include <queue>

#define mp make_pair
#define fi first
#define se second

using namespace std;

int T;
int n;

int db[1000];
int div[1000];
priority_queue<pair<int,int> > sset;

int main()
{
    cin >> T;
    for(int t=1; t<=T; t++) {
        while(!sset.empty()) sset.pop();

        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> db[i];
            sset.push(mp(db[i],i));
            div[i] = 1;
        }

        int sol = sset.top().fi;
        int ma = 0;
        while(sset.top().fi > 1) {
            int p = sset.top().se;
            sset.pop();
            div[p]++;
            int nv = (db[p]+div[p]-1)/div[p];
            sset.push(mp(nv,p));
            ma++;
            sol = min(sol,sset.top().fi + ma);
        }

        cout << "Case #" << t << ": " << sol << endl;
    }

    return 0;
}
