#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define MAX 1006

bool compare(const int a, const int b){
    return (a > b);
}
int main(){
    #ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    #endif // ONLINE_JUDGE
    int T;
    int n, c[MAX];
    vector <int> a;
    scanf("%d",&T);
    for(int iT = 0; iT < T; iT++){
        scanf("%d",&n);
        a.clear();
        for(int i = 0; i<MAX; i++) c[i] = 0;
        for(int i = 0; i<n; i++){
            int x;
            scanf("%d",&x);
            a.push_back(x);
        }
        sort(a.begin(), a.end(),compare);
        int ans = a[0];
        for(int i = a[0]; i>=1; i--){
            int sum = i;
            for(int j = 0; j < n; j++){
                if (a[j] <= i) break;
                if (a[j]%i ==0) sum+=a[j]/i-1;
                else sum+=a[j]/i;
            }
            ans = min(ans,sum);
        }
        printf("Case #%d: %d\n",iT+1,ans);
    }
    return 0;
}
