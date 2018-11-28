#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;


double compute() {
    int k, n;
    cin >> n >> k;
    vector<double> probs(n);
    for (int i = 0; i < n; i++)
        cin >> probs[i];
    vector<int> cand(n, 0);
    for (int i = n-k; i < n; i++)
        cand[i] = 1;
    double ans = 0;
    do {
        vector<double> prob(k/2 + 1, 0);
        prob[0] = 1;
        for (int i = 0; i < n; i++) {
            if (not cand[i]) continue;
            vector<double> newprob(k/2+1, 0);
            for (int j = 0; j <= k/2; j++) {
                newprob[j] += prob[j] * (1-probs[i]);
                if (j < k/2)
                    newprob[j+1] += prob[j] * probs[i];
            }
            prob = newprob;
        }
//         cout << "A" << endl;
        ans = max(ans, prob[k/2]);
    } while(next_permutation(cand.begin(),cand.end()));
    return ans;
}

int main() {
    int nc;
    cin >> nc;
    for (int caso = 1; caso <= nc; caso++) {
        double d = compute();
        cout.setf(ios::fixed);
        cout.precision(10);
        cout << "Case #" << caso << ": " << d << endl;
    }
}