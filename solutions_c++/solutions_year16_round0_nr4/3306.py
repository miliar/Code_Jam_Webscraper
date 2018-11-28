#include <bits/stdc++.h>
#define LLI long long int
#define LLUI long long unsigned int
#define LD long double
#define MOD 1000000007LL
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
using namespace std;

int main() {
    int T;
    LLUI i,j,k,K,C,S;
    cin>>T;
    for(i=1;i<=T;i++){
        cin>>K>>C>>S;
        vector<int> vec;
        if(K==S){
            for(j=1;j<=K;j++){
                vec.push_back(j);
            }
        }
        cout<<"Case #"<<i<<": ";
        for(k=0;k<vec.size();k++){
            cout<<vec[k]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
