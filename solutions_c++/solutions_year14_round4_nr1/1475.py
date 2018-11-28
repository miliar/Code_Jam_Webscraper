// clang++ -std=c++11 -fsanitize=undefined -Weverything -Wno-sign-conversion -Wno-sign-compare -Wno-c++98-compat -Wno-missing-prototypes -Wno-c++98-compat-pedantic -Wno-shorten-64-to-32 -Wno-missing-variable-declarations -Wno-exit-time-destructors -Wno-global-constructors
#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

int T;

vector<int> S;
int N;
int X;

int solve(){
    sort(S.begin(),S.end());
    int res=0;
    int l=0;
    int r=S.size()-1;
    while(l<=r){
        if(l==r){
            res++;
            l++;
        }
        else if(S[r]+S[l]<=X){
            res++;
            r--;
            l++;
        }
        else{
            r--;
            res++;
        }
    }
    return res;
}

int main(){
    cin>>T;
    for(int t=1;t<=T;t++){
        
        S.clear();
        cin>>N>>X;
        for(int i=0;i<N;i++){
            int temp;
            cin>>temp;
            S.emplace_back(temp);
        }
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}
