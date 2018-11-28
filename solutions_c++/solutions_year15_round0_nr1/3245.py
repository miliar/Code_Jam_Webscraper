#include <iostream>
#include <map>
#include <vector>
using namespace std;
map<int,int> M;
int min2(int x, int y) {
        return (x<y)?x:y;
}
int F(int k ) {
        if (M.find(k)!=M.end()) return M[k];
        if (k<=2) return M[k] = k;
        M[k] = min2(F(k-1)+1,F((k+1)/2)+1);
}
const int shift = 10000;
int G(int k , int l ) {
       if ( l >= k ) return 0;
        if (M.find(k*shift+l)!=M.end()) return M[k*shift+l];
        int p1 = k/2;
        int p2 = k-p1;
        M[k*shift+l] = min2(G(k-l,l),G(p1,l)+G(p2,l))+1;
        return M[k*shift+l];
}
int main(){
        int NN;
        cin >> NN;
        for (int nn0 = 1; nn0 <= NN; nn0++) {
                cout <<"Case #"<<nn0<<": ";
                int w;
                string t;
                cin >> w >> t;
                int ans = 0;
                int curr = t[0]-'0';
                for (int j = 1 ; j <=w ;j++) {
                        int nn = t[j] -'0';
                        if (curr < j) {
                                ans += (j-curr);
                                curr = j;
                        }
                        curr += nn;
                }
                cout <<ans << endl;

        }
}
