#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <utility>
#include <stack>
#include <string.h>
#include <complex>
using namespace std;

const long long MOD = 1000000007;
const int INF = 1<<29;
const double EPS = 1e-8;
typedef vector<int> vec;
typedef pair<int,int> P;
typedef long long ll;

ll divisor(ll target){
    if(target%2 == 0) return 2;
    for(ll i=3;i*i<=target;i+=2){
        if(target%i == 0) return i;
    }
    return 0;
}

int main(){
    int T, N, J;
    cin >> T >> N >> J;
    int count = 0;
    cout << "Case #1:" << endl;
    for(int i=(1<<(N-1))+1;count<J;i+=2){
        if(i < 0) break;
        vector<int> ibit;
        int iCopy = i;
        while(iCopy>0){
            ibit.push_back(iCopy&1);
            iCopy >>= 1;
        }

        vector<int> ans;
        for(int j=2;j<=10;j++){
            ll p = 1;
            ll jJamcoin = 0;
            for(int v: ibit){
                jJamcoin += v*p;
                p *= j;
            }
            ll jDivisor = divisor(jJamcoin);
            if(jDivisor == 0){
                break;
            }else{
                ans.push_back(jDivisor);
            }
        }
        if(ans.size() == 9){
            count++;
            for(int j=ibit.size()-1;j>=0;j--){
                cout << ibit[j];
            }
            for(int j=0;j<9;j++){
                cout << " " << ans[j];
            }
            cout << endl;
        }
    }

}