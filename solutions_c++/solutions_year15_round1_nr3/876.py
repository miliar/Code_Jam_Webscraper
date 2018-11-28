#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;

struct pt {
    double x, y;
    int i;
};

bool cmp (pt a, pt b) {
    return ((a.x < b.x) || ((a.x == b.x) && (a.y < b.y)));
}

bool cw (pt a, pt b, pt c) {
    return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) <= 0;
}

bool ccw (pt a, pt b, pt c) {
    return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) >= 0;
}

void convex_hull (vector<pt> & a) {
    if (a.size() <= 2)  return;
    sort(a.begin(), a.end(), &cmp);
    pt p1 = a[0],  p2 = a.back();
    vector<pt> up, down;
    up.push_back (p1);
    down.push_back (p1);
    for (size_t i=1; i<a.size(); ++i) {
        if (i==a.size()-1 || cw (p1, a[i], p2)) {
            while (up.size()>=2 && !cw (up[up.size()-2], up[up.size()-1], a[i]))
                up.pop_back();
            up.push_back (a[i]);
        }
        if (i==a.size()-1 || ccw (p1, a[i], p2)) {
            while (down.size()>=2 && !ccw (down[down.size()-2], down[down.size()-1], a[i]))
                down.pop_back();
            down.push_back (a[i]);
        }
    }
    a.clear();
    for (size_t i=0; i<up.size(); ++i)
        a.push_back (up[i]);
    for (size_t i=down.size()-2; i>0; --i)
        a.push_back (down[i]);
}

int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ":" << endl;
        int  n;
        cin >> n;
        vector <pt> b, c;
        b.clear();
        c.clear();
        int ans[16];
        for (int i=0;i < n;i++){
            ans[i] = n-1;
            pt tmp;
            cin >> tmp.x >> tmp.y;
            tmp.i = i;
            b.push_back(tmp);
            c.push_back(tmp);
        }
        convex_hull(c);
        for (int l=0;l<c.size();l++)
            ans[c[l].i] = 0;
        for (int i=1;i<(1 << n);i++){
            c.clear();
            bool can[16];
            int w = 0;
            for (int j=0;j<n;j++){
                if (((i >> j) & (1)) == 1){
                    c.push_back(b[j]);
                    can[j] = true;
                }else{
                    can[j] = false;
                    w++;
                }
            }
            convex_hull(c);
            for (int l=0;l<c.size();l++)
                ans[c[l].i] = min(ans[c[l].i], w);
        }
        for (int i=0;i<n;i++)
            cout << ans[i] << endl;
    }
    return 0;
}