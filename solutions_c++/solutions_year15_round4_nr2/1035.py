#include <iostream> 
#include <map> 
#include <vector> 
#include <string> 
#include <set> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <queue> 
#include <list> 
#include <limits> 
#include <stack> 
#include <sstream> 
#include <fstream> 
#include <ctime> 
#include <cstdlib> 
#include <complex> 
#include <cctype> 
#include <iomanip> 
#include <functional> 
#include <cstring> 
using namespace std; 
 
typedef long long int64 ; 
typedef unsigned long long uint64;

bool check(vector<pair<long double, long double> >& data, vector<long double>& most, long double tar, long double V, long double& left ,long double& right){ 

    long double haveleft = V, haveright = V; 
    left = 0, right = 0;
    for(int i = 0; i < data.size(); ++i){
        left += min(haveleft, most[i]) * data[i].first; 
        right += min(haveright, most[data.size() -i -1]) * data[ data.size() - i -1].first; 
        haveleft -= min(haveleft, most[i]); 
        haveright -= min(haveright, most[data.size() -i-1]); 
    }
    if( fabs(tar - left) < 1e-15 || fabs(tar-right) < 1e-15) return true;
    return tar > left  && tar <  right ;
}

int main (){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int T; 
    cin >> T ; 
    for(int cas  = 1 ; cas <= T ; ++cas){ 

        int N ;
        cin >> N; 
        long double V, C; 
        cin >> V >> C;
        long double minr = 100000000.; 
        vector< pair<long double, long double> > data; 
        for(int i = 0 ; i < N ; ++i){ 
            long double r,c;
            cin >> r >> c; 
            minr =min(r,minr); 
            //Ci, Ri 
            data.push_back(make_pair(c,r));
        }
        sort(data.begin(), data.end()); 
    
        long double l = 0., r = V/minr + 10 ; 
        bool can = false; 
        int cnt = 0 ;
        while( cnt < 30000000&& fabs(r-l) > 1e-10){  

            ++cnt;

            long double mid = (r + l ) /2; 

            vector< long double > most(N); 
            for(int i = 0 ; i < N ; ++i)
                most[i] = data[i].second * mid; 
            long double left, right; 
            bool now = false; 

            if( check( data, most, V*C, V, left, right) ){
                can = true; 
                r = mid; 
            }else{
                l = mid;
            } 
               
        } 

        cout <<"Case #"<<cas <<": "; 
        if(can) printf("%.10Lf\n", r); 
        else puts("IMPOSSIBLE");
    }
    return 0;
}

            
