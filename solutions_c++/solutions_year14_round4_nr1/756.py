//Jakub Sygnowski
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define F first
#define S second
#define MAXN 1005
typedef long long ll;
typedef pair<int,int> pii;
int n, x;
multiset<int> tab;
void solve(int test){
    scanf("%d%d",&n, &x);
    tab.clear();
    for(int i = 0; i < n; i++){
        int a;
        scanf("%d",&a);
        tab.insert(a);
    }
    int res = 0;
    while(!tab.empty()){
        int big = *(tab.rbegin());
        tab.erase(tab.find(big));
        set<int>::iterator small = tab.upper_bound(x - big);
        res++;
        if (small == tab.begin()){
            continue;
        }
        small--;
        tab.erase(tab.find(*small));
    }
    printf("Case #%d: ", test);
    printf("%d\n", res);
}

int main(){
    int t;
    scanf("%d",&t);
    int test;
    while(test++ < t){
        solve(test);
    }
}
