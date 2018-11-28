#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <vector> 
#include <cstdio>
#include <stack>
#include <cassert>
#include <sstream>
using namespace std;  

typedef long long int64; 
const int mod = 1e9 + 7;

int main (){ 
    int T; 
    freopen("a.in","r",stdin); 
    freopen("a.out", "w",stdout);
    cin >> T; 
    for(int Cas = 1; Cas <= T; ++Cas){
        int N, X; 
        cin >> N >> X ; 
        vector< int > data(N); 
        for(int i = 0 ;  i < N ; ++i)
            cin >> data[i];
        sort(data.begin(), data.end()); 
        vector< bool > used(N,false);
        int ans = 0; 
        for(int i = N - 1,j=0; i >= j ; --i){
            if(used[i]) continue;
            used[i]=true;
            ++ans;
            if(data[i] + data[j] <= X){
                used[j++]=1;
            }
        }
        cout <<"Case #"<<Cas<<": "<< ans << endl; 
    }
    return 0;
}


