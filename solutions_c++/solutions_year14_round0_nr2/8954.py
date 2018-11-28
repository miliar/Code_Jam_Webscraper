#include<bits/stdc++.h>
using namespace std;

#define LL long long int
#define ULL unsigned LL
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
#define INF 1000000000
#define MOD 1000000007

int main(){
    int t;
    int cs = 0;
    cin >> t;
    while(t--){
        printf("Case #%d: ", ++cs);
        double c,f,x;
        cin >> c >> f >> x;
        double lb = 0, ub = 1e16, mid;
        int tries = 1000;
        while(lb <= ub && tries --){
            mid = (lb + ub)/2;
            double cf = 2, ct = 0;
            while(mid >= ct){
                if((mid - ct)*cf >= x){
                    ub = mid;
                    break;
                }
                if(ct + c/cf > mid){
                    lb = mid;
                    break;
                }
                ct += c/cf;
                cf += f;
            }
        }
        printf("%.7lf\n", mid);
    }
    return 0;
}
