#include <string> 
#include <algorithm> 
#include <cfloat> 
#include <climits> 
#include <cmath> 
#include <complex> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <functional> 
#include <iostream> 
#include <map> 
#include <memory> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 

#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define ALL(x) (x).begin(),(x).end() 
using namespace std;
const double eps = 1e-10;

//input data
int X, N, S[10010];

void solve(int caseNum){
    //solve problem here
    int res = 0;
    sort(S, S+N);
    int l = 0, r = N - 1;
    while(l <= r){
        if(S[l] + S[r] <= X){
            res++;
            l++; r--;
        }
        else{
            res++;
            r--;
        }
    }
    cout << "Case #" << caseNum << ": " << res << endl;
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        cin >> N >> X;
        for(int i = 0; i < N; ++i){
            cin >> S[i];
        }
        solve(t);
    }
    return 0;
}
