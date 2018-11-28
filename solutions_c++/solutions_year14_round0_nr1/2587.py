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
int row[2];
int c[2][4][4];

void solve(int caseNum){
    //solve problem here
    int cnt[17];
    int res;
    memset(cnt, 0, sizeof(cnt));

    for(int k = 0; k < 2; ++k){
        int r = row[k] - 1;
        for(int j = 0; j < 4; ++j)
            cnt[c[k][r][j]]++;
    }
    res = 0;
    for(int i = 1; i <= 16; ++i){
        if(cnt[i] == 2){
            res = res ? -1: i;
        }
    }
    cout << "Case #" << caseNum << ": ";
    if(res < 0){
        cout << "Bad magician!";
    }
    else if(res == 0){
        cout << "Volunteer cheated!";
    }
    else{
        cout << res;
    }
    cout << endl;
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        for(int k = 0; k < 2; ++k){
            cin >> row[k];
            for(int i = 0; i < 16; ++i){
                cin >> c[k][i/4][i%4];
            }
        }

        solve(t);
    }
    return 0;
}
