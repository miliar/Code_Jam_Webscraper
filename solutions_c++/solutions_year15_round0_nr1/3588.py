#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <tuple>
#include <stack>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
 
 
using namespace std;
 
int main(int, char** ){
    cin.tie(nullptr); ios::sync_with_stdio(false);
    //cout << fixed <<  std::setprecision(10) ;
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i){
        int smax; string s;
        cin >> smax >> s;
        
        vector<int> si(smax+1,0);
        for(int j = 0; j < smax+1; ++j){
            si[j]=s[j]-'0';   
        }

        int suma = 0, ans = 0;
        for(int j = 0; j < smax+1; ++j){
            
            if(si[j]==0) continue;

            if(suma<j){
                ans += j-suma;
                suma=j;
            }

            suma += si[j];
        }

        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}