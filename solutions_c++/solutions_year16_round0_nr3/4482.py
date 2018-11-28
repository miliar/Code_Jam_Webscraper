#include <iostream>
#include <vector>
using namespace std;

int main(){
    long long n = 16, j = 50, cnter = 0;
    freopen("gulight.txt", "w", stdout);
    cout << "Case #1:" << endl;
    for (long long g=(1<<(n-1)); g<(1<<n); g++){if (cnter == j) break;
        if (g%2==0) continue; vector <long long> gu;
        for (long long y=2; y<=10; y++){
            long long lo = g; long long ans = 0, cur = 1;
            while (lo){
                ans+=cur*(lo%2); cur*=y;
                lo/=2;
            }
            bool flag = 0;
            for (long long z=2; z*z<=ans; z++){
                if (ans%z==0){flag = 1; gu.push_back(z); break;}
            }
        }long long cp = g;
        if (gu.size() == 9) {vector <long long>bin; while(cp){bin.push_back(cp%2);cp/=2;}reverse(bin.begin(),bin.end());for(long long z:bin)cout<<z;cout << ' ';for (long long y : gu) cout << y << ' '; cout << '\n'; cnter++;}
    }
}
