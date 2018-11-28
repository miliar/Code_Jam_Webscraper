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
using namespace std;

ifstream cin("/Users/Nagi2/Downloads/D-small-attempt0.in");
ofstream cout("/Users/Nagi2/Downloads/GCJ2016/dddS.txt");

long long basek(vector <long long> vl, long long k){
    long long ans = 0;
    for(int i=0;i<vl.size();i++){
        ans = ans*k + vl[i];
    }
    return ans;
}


int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for(int t =0;t<T;t++){
        int K,C,S;
        cin >> K >> C >> S;
        int z = (K+C-1)/C;
        int j=0;
        vector <long long> values;
        for(int i=0;i<z;i++){
            vector <long long> digits;
            for(int k=0;k<C;k++){
                digits.push_back(j);
                j = (j+1)%K;
            }
            //sort(digits.begin(),digits.end());
            long long val = basek(digits,K);
            val++;
            values.push_back(val);
            
        }
        if(z<=S){
        cout << "Case #" << t+1 << ": ";
        for(int i=0;i<values.size();i++){
            cout << values[i];
            if(i!=values.size()-1) cout << " ";
            else cout << endl;
        }
        }
        else{
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
 
        }
    }
    return 0;
}
