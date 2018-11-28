#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
//#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
using namespace std;

ifstream cin("/Users/Nagi2/Downloads/GCJ2016/B-small-attempt0.in");
ofstream cout("/Users/Nagi2/Downloads/mnbvcxzBxx.txt");


double dp[30][30];
double f( vector <double> &vp,int i, int k){
    if(i== vp.size()){
        if(k==0) return 1.0;
        else return 0.0;
    }
    if(dp[i][k] !=-1.0) return dp[i][k];
    dp[i][k] =  vp[i]*f(vp,i+1,k-1) + (1.0-vp[i])*f(vp,i+1,k);
    return dp[i][k];
}
int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    int ans = 0;
    for(int t =0;t<T;t++){
        int N,K;
        cin >> N >> K;
        vector <double> p;
        for(int i=0;i<N;i++){
            double z ;
            cin >> z;
            p.push_back(z);
            //cout << "FDSFS" << z << endl;
        }
        vector <int> msk;
        for(int i=0;i<N;i++) msk.push_back(0);
        for(int i=0;i<K;i++) msk[i] = 1;
        sort(msk.begin(),msk.end());
        bool b = true;
        double bestX = 0;
        while(b){
            for(int i=0;i<30;i++) for(int j=0;j<30;j++) dp[i][j] = -1;
            vector <double> vp2;
            for(int i=0;i<N;i++){
                if(msk[i] == 1) vp2.push_back(p[i]);
            }
            double x = f(vp2,0,K/2);
            bestX = max(x,bestX);
            b = next_permutation(msk.begin(),msk.end());
            
        }
        cout<< fixed <<setprecision(9)<< "Case #" << t+1 << ": " << bestX << endl;
    }
    return 0;
}
