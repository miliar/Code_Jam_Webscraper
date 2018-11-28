
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

int dscore(vector<double> &mine, vector<double> &other) {
    int score=0,j=0;
    for (int i=0; i<mine.size(); i++) {
        if (mine[i] > other[j]) {
            score++;
            j++;
        }
    }
    return score;
}

int normal_score(vector<double> &mine, vector<double> &other) {
    int ans=0;
    set<double> oset(other.begin(),other.end());
    for (int i=0; i<mine.size(); i++) {
        set<double>::iterator it = oset.upper_bound(mine[i]);
        if (it == oset.end()) {
            ans++;
            oset.erase(oset.begin());
        } else {
            oset.erase(it);
        }
    }
    return ans;
}

pair<int,int> score(vector<double> &mine, vector<double> &other) {
    sort(mine.begin(), mine.end());
    sort(other.begin(), other.end());
    return make_pair(dscore(mine,other),normal_score(mine,other));
}

int main(int argc, char **argv) {
    int T,N; double x;
    cin >> T;
    rep(tc, T) {
        cin >> N;
        vector<double> mine,other;
        rep(i,N) {cin >> x; mine.push_back(x);}
        rep(j,N) {cin >> x; other.push_back(x);}
        pair<int,int> ans = score(mine,other);
        printf("Case #%d: %d %d\n",tc+1,ans.first,ans.second);
    }
}

