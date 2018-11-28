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

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int K, C, S;
        cin >> K >> C >> S;
        printf("Case #%d:", t);
        for(int i=0;i<K;i++){
            ll KC = 1;
            ll idxi = 0;
            for(int j=0;j<C;j++){
                idxi += i*KC;
                KC *= K;
            }
            printf(" %lld", idxi+1);
        }
        printf("\n");
    }
    return 0;
}