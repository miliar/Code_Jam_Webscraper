#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <string>
#include <iomanip>
#include <cstdio>

using namespace std;
typedef long double DOUBLE;

bool solve2(DOUBLE tm, DOUBLE V, DOUBLE X, vector<DOUBLE>& R, vector<pair<DOUBLE,int> >& J){
    DOUBLE volume = 0.0;
    DOUBLE min_jule = 0.0;
    DOUBLE max_jule = 0.0;
    for(int i = 0; i < J.size(); i++){
        int cur = J[i].second;
        DOUBLE use_time = min(tm, (V - volume) / R[cur]);
        volume += R[cur] * use_time;
        min_jule += J[i].first * R[cur] * use_time;
    }
    if(volume < V - 1.0e-12) return false;
    volume = 0.0;
    for(int i = (int)(J.size())-1; i >= 0; i--){
        int cur = J[i].second;
        DOUBLE use_time = min(tm, (V - volume) / R[cur]);
        volume += R[cur] * use_time;
        max_jule += J[i].first * R[cur] * use_time;
    }
    //cerr << min_jule << " : " << V*X << " : " << max_jule << " : " << tm << endl;
    //return (min_jule - 1.0e-12 <= V*X) && (V*X <= max_jule + 1.0e-12);
    return (min_jule / V - 1.0e-12 <= X) && (X <= max_jule / V + 1.0e-12);
}

DOUBLE solve(int N, DOUBLE V, DOUBLE X, vector<DOUBLE>& R, vector<DOUBLE>& C){
    vector<pair<DOUBLE, int> > J(N);
    for(int i = 0; i < N; i++){
        J[i] = pair<DOUBLE, int>(C[i], i);
    }
    sort(J.begin(), J.end());
    DOUBLE left = 0;
    DOUBLE right = 1000000000.0;
    if(!solve2(right, V, X, R, J)) return -1.0;
    for(int e = 0; e < 1000; e++){
        DOUBLE middle = (left+right) / 2.0;
        if(solve2(middle, V, X, R, J)){
            right = middle;
        }else{
            left = middle;
        }
        //cerr << left << " : " << right << endl;
    }
    return left;
}



int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N;
        DOUBLE V, X;
        cin >> N >> V >> X;
        vector<DOUBLE> R(N);
        vector<DOUBLE> C(N);
        for(int i = 0; i < N; i++){
            cin >> R[i] >> C[i];
        }
        DOUBLE ans = solve(N, V, X, R, C);
        if(ans >= -1.0e-9){
            //cout << setprecision(20) << "Case #" << t <<": " << ans << endl;
            printf("Case #%d: %.9Lf\n", t, ans);
        }else{
            cout << "Case #" << t <<": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

