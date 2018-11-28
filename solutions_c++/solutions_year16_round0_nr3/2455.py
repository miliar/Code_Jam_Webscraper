#include <bits/stdc++.h>
using namespace std;
int t,n,m,cnt;
vector <int> v,ans;
long long power(long long x, long long y) {
    long long pro=1;
    for (int i=0;i<y;i++) pro*=x;
    return pro;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    n=16,m=50;
    printf("Case #1:\n");
    if (n==16) {
        for (long long i=32768;i<=65535;i++) {
            v.clear();
            ans.clear();
            int k=i;
            while (k) {
                v.push_back(k%2);
                k/=2;
            }
            int size=v.size();
            if (v[0]!=1||v[size-1]!=1) continue;
            for (int j=2;j<=10;j++) {
                long long sum=0,div=-1;
                for (int l=0;l<size;l++) {
                    if (v[l]==1) sum+=power(j,l);
                }
                for (int l=2;l<=sqrt(sum);l++) {
                    if (sum%l==0) {
                        div=l;
                        break;
                    }
                }
                if (div!=-1) ans.push_back(div);
                else break;
                if (j==10) {
                    cnt++;
                    if (cnt>m) return 0;
                    for (int l=size-1;l>=0;l--) {
                        printf("%d",v[l]);
                    }
                    printf(" ");
                    for (int l=0;l<ans.size();l++) {
                        printf("%d%c",ans[l],l==ans.size()-1?'\n':' ');
                    }
                }
            }
        } 
    }
} 
