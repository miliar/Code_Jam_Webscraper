#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "B.in"
#define FILEOUT "B.out"



int main(){
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_){
    	
        double X;
        double V;
        cin >> V >> X;

        int N;
        cin >> N;
        double R[N];
        double XX[N];
        for (int i = 0; i < N; ++i) {
            cin >> R[i] >> XX[i];
        }

        double left = 0.0;
        double right = 1000000000.0 * 100000.0;

        for (int it = 0; it < 500; ++it) {
            double vsum = 0;
            double xsum  = 0;
            double mid = (left + right) / 2.0;
            for (int i = 0; i < N; ++i) {
                vsum += R[i]*mid;
                xsum += R[i]*mid*
            }

        }


        cout << "Case #" << _ << ": ";
        //Output answer 
        
        
        cout << "\n";
    }
    return 0;
}