#include <iostream>
#include <vector>
#include <algorithm>

//#define DEBUG

using namespace std;

void solve(int t){
    int N; cin >> N;
    vector<double> naomis;
    for(int i=0; i < N; i++){
        double tmp; cin >> tmp;
        naomis.push_back(tmp);
    }
    vector<double> kens;
    for(int i=0; i < N; i++){
        double tmp; cin >> tmp;
        kens.push_back(tmp);
    }
    sort(naomis.begin(), naomis.end());
    sort(kens.begin(), kens.end());

#ifdef DEBUG
    cout << "Naomi's: ";
    for(auto it = naomis.begin(); it != naomis.end(); ++it){
        cout << *it << ", ";
    }
    cout << endl;
    cout << "  Ken's: ";
    for(auto it = kens.begin(); it != kens.end(); ++it){
        cout << *it << ", ";
    }
    cout << endl;
#endif

    int count;
    vector<double>::iterator nit, kit;

    // Deceitful War
    count = 0;
    nit = naomis.begin();
    for(auto kit = kens.begin(); kit != kens.end(); ++kit){
        for(; nit != naomis.end(); ++nit) {
            if(*kit < *nit){
                #ifdef DEBUG
                cout << "  pair(N,K): " << *nit << ", " << *kit << endl;
                #endif
                ++count;
                ++nit;
                break;
            }
        }       
    }
    int y = count;

    // War
    count = 0;
    kit = kens.begin();
    for(auto nit = naomis.begin(); nit != naomis.end(); ++nit){
        for(; kit != kens.end(); ++kit) {
            if(*nit < *kit){
                #ifdef DEBUG
                cout << "  pair(N,K): " << *nit << ", " << *kit << endl;
                #endif
                ++count;
                ++kit;
                break;
            }
        }       
    }
    int z = N - count;

    cout << "Case #" << t + 1 << ": " << y << " " << z << endl;
}

int main(void) {
    int T; cin >> T;
    for(int t = 0; t < T; t++){
        solve(t);
    }
    return 0;
}
