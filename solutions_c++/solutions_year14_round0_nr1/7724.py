#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define sz(v) ((int)(v).size())
#define pb push_back
#define clr(x,a) memset(x,a,sizeof(x))
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
int a[22][22];
int main() {
    int casenum;
    cin >> casenum;
    for(int ca = 1; ca <= casenum; ca++)
    {
        int n;
        cin >> n;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &a[i][j]);
        vector<int> vec;
        for(int i = 1; i <= 4; i++)
            vec.pb(a[n][i]);
        cin >> n;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &a[i][j]);
        int tag = 0;
        int cur;
        for(int i = 1; i <= 4; i++)
            for(int j = 0; j < 4; j++)
                if(a[n][i] == vec[j])
                    tag++, cur = a[n][i];
        cout << "Case #" << ca << ": ";
        if(tag == 0) cout << "Volunteer cheated!" << endl;
        if(tag == 1) cout << cur << endl;
        if(tag > 1) cout << "Bad magician!" << endl;
    }
    return 0;
}

