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



using namespace std;


int n; 
int maxk = 0;
vector <int> list1;
vector <int> list2;

string a[5];
int x[20];
int d[5][5];

bool FAIL = false;

void rec(int k) {
    bool fail = true;
    if (k == n) return;
    for (int i = 0; i < n; i++) {
        bool z = true;
        for (int j = 0; j < list1.size(); j++)
            if (list1[j] == i) z = false;
        if (z) {
            for (int j = 0; j < n; j++) 
                if (d[i][j])
            {
                bool z2 = true;
                for (int j1 = 0; j1 < list2.size(); j1++)
                    if (list2[j1] == j) z2 = false;
                if (z2) {
                    list1.push_back(i);
                    list2.push_back(j);
                    fail = false;
                    rec(k+1);
                    list1.pop_back();
                    list2.pop_back();
                }
            }
                
        }
    }
    
    if (fail) FAIL = true;
        
}


int main() {
    

    cin.sync_with_stdio(false);
    cin.tie(0);
    
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cout.setf(ios::fixed);
    cout.precision(10);
           
    int t;
    cin >> t;
    
    for (int i1 = 0; i1 < t; i1++) {
        
        int ans = 1000000;
        
        cin >> n;
        
        for (int j = 0; j < n; j++)
            cin >> a[j];
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++) {
//                cout << a[j][k];
                x[j*n+k] = a[j][k]-'0';
            }
        
//        for (int j = 0; j < n*n; j++)
//            cout << x[j] << " ";
//        cout << "\n";
        
        for (int j = 0; j < (1<<n*n); j++) {
            bool z = true;
            int cnt = 0;            
            for (int k = 0; k < n*n; k++) {
                if (((1<<k)&j) < x[k]) z = false;
                if ((((1<<k)&j) > 0) && (x[k] == 0)) cnt++;
                
            }
//            if (z) cout << j << "\n";
            
            if (z) {
                for (int j1 = 0; j1 < n; j1++) {
                    for (int j2 = 0; j2 < n; j2++) {
                        d[j1][j2] = ((1<<(j1*n+j2))&(j))>0;
//                        cout << d[j1][j2] << " ";
                    }
//                    cout << "\n";
                }
                

                bool z = true;
                maxk = 0;
                FAIL = false;
                rec(0);
                if (!FAIL) ans = min(ans,cnt);
//                cout << cnt << " " << FAIL << "!\n";
                
                
                
            }
//            
        }
        cout << "Case #" << i1+1 << ": " << ans << "\n";
    }
    
    return 0;
}
