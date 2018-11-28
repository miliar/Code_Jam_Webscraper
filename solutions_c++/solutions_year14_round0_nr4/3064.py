#include <iostream>
#include <math.h>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

//Au départ i = N.
long cheat(long i1, long j1, long i2, long j2, vector<double> &Naomi, vector<double> &Ken) {
    if(i1>j1 || i2 > j2)
        return 0;
    
    if(Naomi[i1]>Ken[i2])
        return 1+cheat(i1+1, j1, i2+1, j2, Naomi, Ken);
    else {
        return cheat(i1+1, j1, i2, j2-1, Naomi, Ken);
    }
    
}

long no_cheat(int i, int j, vector<double> &Naomi, vector<double> &Ken) {
    if(i >= Naomi.size()) {
        return 0;
    }
    //On cherche le plus petit j2 tel que Ken[j2] > Naomi[i]
    int j2 = j;
    while(Ken[j2] <= Naomi[i] && j2 < Ken.size()) {
        j2++;
    }
    if(j2 >= Ken.size()) {
        return Ken.size() - i;
    }
    else {
        return no_cheat(i+1, j2+1, Naomi, Ken);
    }
}
int main(int argc, const char * argv[])
{
    int T;
    cin >> T;
    for(int nb = 1; nb <= T; nb++) {
        int N;
        cin >> N;
        vector<double> Naomi(N);
        vector<double> Ken(N);
        
        for(int i = 0; i < N; i++) {
            cin >> Naomi[i];
        }
        for(int i = 0; i < N; i++) {
            cin >> Ken[i];
        }
        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());
        
        cout << "Case #" << nb << ": ";
        cout << cheat(0, N-1, 0, N-1, Naomi, Ken) << " ";
        cout << no_cheat(0, 0, Naomi, Ken) << endl;
        
    }
    return 0;
}

