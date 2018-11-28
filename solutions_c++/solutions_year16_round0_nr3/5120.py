#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751



vector<int>P = {11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853};


const int NBP = 32;
int main() {
  int T, J, M;
  cin >> T >> J >> M;

  int MOD[11][32][NBP];

    for(int b = 2; b <= 10; b++) 
      for(int i = 0; i < 32; i++)
        for(int j = 0; j < NBP; j++) {
          int m = 1;
          for(int k = 0; k < i; k++) m = (m*b)%P[j];
          MOD[b][i][j] = m;
    }



    int m = (1 << (J-1)) + 1;
    int div[11];

    cout << "Case #1:" << endl;
    for(int n = 0; n < M; m+=2) {

      for(int b = 2; b <= 10; b++) {
        div[b] = 0;
        bool prime = true;
        for(int k = 0; k < NBP; k++) {
          int mod = 0;
          for(int j = 0; j < J; j++) if(m & (1 << j)) mod += MOD[b][j][k];
          if(mod % P[k] == 0) {div[b] = P[k]; break;}
        }
        if(div[b] == 0) break;
        if(b == 10) {
          n++;
          for(int i = J-1; i >= 0; i--) cout << ((m & (1 << i)) ? "1" : "0");
          for(int i = 2; i <= 10; i++) cout << " " << div[i];
          cout << endl;
          break;
        }
      }
    }
}
