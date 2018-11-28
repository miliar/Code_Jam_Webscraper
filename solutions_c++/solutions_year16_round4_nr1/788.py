#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define mp make_pair
#define ll long long
#define pb push_back

int x,r,p,sc;

using namespace std;


int main() {
    

    cin.sync_with_stdio(false);
    cin.tie(0);
    
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t;
    cin >> t;
    
    for (int i1 = 1; i1 <= t; i1++) {
//        int x,r,p,s;
        cin >> x >> r >> p >> sc;

        string s0 = "R";
        string s1 = "P";
        string s2 = "S";
        
        
        for (int i = 0; i < x; i++) {
            string ss0;
            string ss1;
            string ss2;
            
            if (s0 > s2) ss0 = s2+s0; else ss0 = s0+s2;
            if (s1 > s0) ss1 = s0+s1; else ss1 = s1+s0;
            if (s1 > s2) ss2 = s2+s1; else ss2 = s1+s2;
            s0 = ss0;
            s1 = ss1;
            s2 = ss2;
        }
        int cnt0 = 0;
        int cnt1 = 0;
        int cnt2 = 0;
        string ans = "IMPOSSIBLE";
        bool z = false;
        for (int i = 0; i < s0.length(); i++){
            if (s0[i] == 'R') cnt0++;
            if (s0[i] == 'P') cnt1++;
            if (s0[i] == 'S') cnt2++;
            if (cnt0 == r && cnt1 == p && cnt2 == sc) {
                z = true;
                ans = s0;
            }
        }
        cnt1 = 0;
        cnt2 = 0;
        cnt0 = 0;
        for (int i = 0; i < s1.length(); i++){
            if (s1[i] == 'R') cnt0++;
            if (s1[i] == 'P') cnt1++;
            if (s1[i] == 'S') cnt2++;
            if (cnt0 == r && cnt1 == p && cnt2 == sc) {
                z = true;
                ans = s1;
            }
        }
        cnt1 = 0;
        cnt2 = 0;
        cnt0 = 0;
        for (int i = 0; i < s2.length(); i++){
            if (s2[i] == 'R') cnt0++;
            if (s2[i] == 'P') cnt1++;
            if (s2[i] == 'S') cnt2++;
            if (cnt0 == r && cnt1 == p && cnt2 == sc) {
                z = true;
                ans = s2;
            }
        }        
        cout << "Case #" << i1 << ": " << ans << "\n";
    }

    return 0;
}
