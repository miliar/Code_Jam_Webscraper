#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define MAX 1006

bool compare(const int a,const int b){
    return (a>b);
}
int main(){
    #ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    #endif // ONLINE_JUDGE
    int T, n;
    vector <int> a;
    scanf("%d",&T);
    for(int iT = 1; iT <= T; iT++){
        scanf("%d",&n);
        a.clear();
        for(int i = 0; i<n; i++){
            int tmp;
            scanf("%d",&tmp);
            a.push_back(tmp);
        }
        sort(a.begin(),a.end(),compare);
        int res = a[0];
        for(int i = a[0]-1; i>=1; i--){
            int tong = i;
            for(int j = 0; j < n; j++){
                if (a[j] <= i) break;
                tong += a[j]/i;
                if (a[j]%i ==0) tong = tong-1;
            }
            //cout << tong <<"\n";
            if (tong < res) res = tong;
        }
        printf("Case #%d: %d\n",iT,res);
    }
    return 0;
}
