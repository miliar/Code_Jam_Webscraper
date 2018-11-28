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
int N;
int A[1010];
int L[1010], R[1010];

void solve(int caseNum){
    //solve problem here
    int res = 0;
    vector<pair<int, int> > v;
    memset(L, 0, sizeof(L));
    memset(R, 0, sizeof(R));
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < i; ++j)
            if(A[j] > A[i]) L[i]++;
        for(int j = N-1; j > i; --j)
            if(A[j] > A[i]) R[i]++;
    }
    for(int i = 0; i < N; ++i){
        res += min(L[i], R[i]);
    }
    cout << "Case #" << caseNum << ": " << res << endl;
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        cin >> N;
        for(int i = 0; i < N; ++i)
            cin >> A[i];

        solve(t);
    }
    return 0;
}
