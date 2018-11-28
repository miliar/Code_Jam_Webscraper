#include <iostream>
#include <cstdio>
#include <string>
#include <utility> // pair
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring> //memset
using namespace std;
  
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define rep(i,n) for (i=0; i<n ; i++)
#define rep1(i,n) for (i=1; i<=n ; i++)
#define MAX 111111
#define MOD 10000000007
int a[MAX];

int main() {

    freopen ("d.in", "r", stdin);
    freopen ("d.out", "w", stdout);
    
    int t, x, r, c, z = 0, flag, size;
    // flag = 1 (R), 0(G)
    scanf("%d", &t);
    while(t--) {
        scanf("%d %d %d", &x, &r, &c);
        size = r*c;
        if(x == 1) flag = 0;
        else if(x == 2){
            if(size % 2 )
                flag = 1;
            else flag = 0;
        }
        else if(x == 3) {
            if(size == 6 || size == 9 || size == 12) {
                flag = 0;
            }
            else flag = 1;
        }
        else {
            if(size == 12 || size == 16) {
                flag = 0;
            }
            else flag = 1;
        }
        if(flag)
            printf("Case #%d: RICHARD\n", ++z);
        else printf("Case #%d: GABRIEL\n", ++z);
    }
    return 0;
}
