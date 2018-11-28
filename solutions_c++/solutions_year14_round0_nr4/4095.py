#include <iostream>
#include <set>
using namespace std;

int deceitfullWar(set<double> n, set<double> k){
    int dw = 0;
        for (set<double>::iterator itK = k.begin(); itK != k.end(); ++itK) {
            set<double>::iterator itN = n.upper_bound(*itK);
            if (itN == n.end()) return dw;
            else {
                ++dw;
                n.erase(itN);
            }
        }
    return dw;
}


int war(set<double> n, set<double> k) {
    int w = 0;
    for (set<double>::iterator itN = n.begin(); itN != n.end(); ++itN) {
        set<double>::iterator itK = k.upper_bound(*itN);
        if (itK == k.end()) {
            ++w;
            k.erase(k.begin());
        }
        else k.erase(itK);
    }
    return w;
}

int main()
{
    int T;
    cin >> T;
    for (int x = 1;x <= T; ++x) {
        int n;
        cin >> n;
        set<double> naomi;
        set<double> ken;
        for (int i = 0; i < n; ++i) {
            double aux;
            cin >> aux;
            naomi.insert(aux);
        }
        for (int i = 0; i < n; ++i) {
            double aux;
            cin >> aux;
            ken.insert(aux);
        }
        int dw,w;
        dw = deceitfullWar(naomi,ken);
        w = war(naomi,ken);
        cout << "Case #" << x << ": " << dw << " " << w << endl;
    }
}
