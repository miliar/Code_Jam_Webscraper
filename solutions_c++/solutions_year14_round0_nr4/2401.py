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
double ken[1010], nao[1010];

int calc(double *a, double *b){
    int res = 0;
    int pa, pb;
    pa = pb = 0;
    while(pa < N && pb < N){
        if(a[pa] > b[pb]){
            res++; pa++; pb++;
        }
        else{
            pa++;
        }
    }
    return res;
}

void solve(int caseNum){
    //solve problem here
    sort(nao, nao + N);
    sort(ken, ken + N);

    int dw = calc(nao, ken);
    int w = N - calc(ken, nao);

    cout << "Case #" << caseNum << ": " << dw << " " << w << endl;
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        cin >> N;
        for(int i = 0; i < N; ++i) cin >> nao[i];
        for(int i = 0; i < N; ++i) cin >> ken[i];

        solve(t);
    }
    return 0;
}
