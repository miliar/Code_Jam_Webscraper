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
    for(int i=0;i<T;i++){
        ll N;
        cin >> N;
        if(N == 0){
            printf("Case #%d: INSOMNIA\n", i+1);
        }else{
            ll j = 1;
            set<int> s;
            while(1){
                ll Nj = N * j;
                while(Nj > 0){
                    s.insert(Nj%10);
                    Nj /= 10;
                }
                if(s.size() == 10){
                    printf("Case #%d: %lld\n", i+1, N*j);
                    break;
                }
                j++;
            }
        }
    }
}