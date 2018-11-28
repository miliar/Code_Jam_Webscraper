#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<char, int> ci;
typedef vector<ci> vii;
typedef vector<int> vi;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int v[26];

int i, j, k, m, n, l;

int findMax(int v[]){
    int maxElement = 0;
    F0(i, 26){
        if (v[i]>v[maxElement]){
            maxElement = i;
        }
    }
    return maxElement;
}

bool largerThanHalf(int v[], int total, int maxE){
    F0(i, 26){
        if (i == maxE){
            if (v[i]-1 > total/2){
                return true;
            }
            continue;
        }
        if (v[i] > total/2){
            return true;
        }
    }
    return false;
}

int main() {
    
//    freopen("x.in", "r", stdin);
//    freopen("x.out", "w", stdout);
    
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tt, tn; cin >> tn;
    F1(tt,tn) {
        memset(v, 0, sizeof v);
        int n; cin >> n;
        int t = 0;
        
        for(i=0; i < n; i++){
            scanf("%d", &v[i]);
            t += v[i];
        }
        int total = t;
        printf("Case #%d: ", tt);
        int temp = 2;
        while (total > 0){
            int maxE = findMax(v);
 
            
            if (temp == 1){
                if (largerThanHalf(v, total-1, maxE)){
                    temp = 2;
                    printf(" ");
                    continue;
                }
            }
            
            v[maxE]--; temp--; total--;
            cout << char('A' + maxE);
            if (temp == 0){
                temp = 2;
                printf(" ");
                continue;
            }
        }
        
        cout << endl;
    }
    return 0;
}
