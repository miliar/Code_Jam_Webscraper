//Jakub Sygnowski
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
#define F first
#define S second
#define MAXN 1006
typedef long long ll;
typedef pair<int,int> pii;
int n, tab[MAXN], best;
int left[MAXN], right[MAXN];
int howManyLeft(int x){
    int res = 0;
    for(int i = 0; i < x; i++){
        if (tab[i] > tab[x])
            res++;
    }
    return res;
}
int howManyRight(int x){
    int res = 0;
    for(int i = x+1; i < n; i++){
        if (tab[i] > tab[x])
            res++;
    }
    return res;
}

void count(){
    for(int i = 0 ; i < n; i++){
        left[i] = howManyLeft(i);
        right[i] = howManyRight(i);
    }
}

void solve(int test){
    scanf("%d",&n);
    best = 1000000007;
    int biggest = -1;
    for(int i = 0; i < n; i++){
        scanf("%d",&tab[i]);
    }
    count();
    int sol = 0;
    for(int i = 0; i < n; i++){
        sol += min(left[i], right[i]);
    }

    printf("Case #%d: %d\n", test, sol);

}

int main(){
    int t;
    scanf("%d",&t);
    int test;
    while(test++ < t){
        solve(test);
    }
}
