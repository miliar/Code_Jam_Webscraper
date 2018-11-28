#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <utility>
#include <stack>
#include <string.h>
#include <complex>
using namespace std;

const long long MOD = 1000000007;
const int INF = 1<<29;
const double EPS = 1e-8;
typedef vector<int> vec;
typedef pair<int,int> P;
typedef long long ll;


int Sd[100];

void execManeuver(int size){
    for(int k=0;k<size/2;k++){
        swap(Sd[k], Sd[size-1-k]);
    }
    for(int k=0;k<size;k++){
        Sd[k] = Sd[k] ? 0 : 1;
    }
}

int main(){
    int T;
    cin >> T;
    // T = 1024;
    for(int t=0;t<T;t++){
        string S;
        cin >> S;
        // for(int i=0;i<10;i++){
        //     if((t>>i)&1){
        //         S.push_back('-');
        //     }else{
        //         S.push_back('+');
        //     }
        // }
        int n = S.size();
        for(int j=0;j<n;j++){
            Sd[j] = S[j] == '-' ? 0 : 1;
        }
        int ans = 0;
        while(n > 0){
            while(Sd[n-1] == 1 && n > 0) n--;
            if(n == 0) break;
            if(Sd[0] == 1){
                ans++;
                int j = 1;
                while(Sd[j] == 1) j++;
                execManeuver(j);
            }
            ans++;
            execManeuver(n);
        }
        printf("Case #%d: %d\n", t+1, ans);
        // cout << S << endl;
    }
}