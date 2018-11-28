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
        for (int nn = 1; nn <= NN; nn++) {
                cout <<"Case #"<<nn<<": ";
                int w; cin >> w;
                vector<int> V;
                for (int i = 0 ; i < w; i++) {
                        int t; cin >> t;
                        V.push_back(t);
                }
                int ans = w*1000;
                for (int l = 1; l<=1000; l++) {
                        int tmp = 0;
                        for (int j  = 0 ; j < w; j++)
                                tmp += G(V[j],l);
                        tmp+=l;
                        if (tmp<ans) ans = tmp;
                }
                
                cout <<ans << endl;

        }
}
