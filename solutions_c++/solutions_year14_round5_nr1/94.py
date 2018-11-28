#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<set>
#include<iomanip>
using namespace std;

long long int nums[1000000];
long long int psum[1000001];
long long int N,p,q,r,s;
long long int sum;

long long int pans(int i){
    //0<=i<=N-1
    long long int total_sum = psum[i+1];
    if (2 * psum[i] <= total_sum) return nums[i];
    int lo = 0, hi = i;
    while(lo<hi){
        int mid = (lo+hi)>>1;
        if (2*psum[mid] <= total_sum){
            lo = mid + 1;
        }
        else{
            hi = mid;
        }
    }
    return min(psum[lo], total_sum - psum[lo-1]);
}

long long int solve(){
    long long int ans = psum[N];
    for (int i=0;i<N;i++){
        ans = min(ans, max(pans(i), psum[N] - psum[i+1]));
    }
    return ans;
}

int main(){
    ifstream in("A.in"); ofstream out("A.out");
    int T;
    in>>T;
    out<<setprecision(10);

    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        in>> N >> p>>q>>r>>s;

        psum[0] = 0;
        for (int i=0;i<N;i++){
            nums[i] = s + (i*p + q) % r;
            psum[i+1] = psum[i] + nums[i];
        }


        out<<1.0 - (solve()*1.0)/psum[N]<<"\n";
    }
}
