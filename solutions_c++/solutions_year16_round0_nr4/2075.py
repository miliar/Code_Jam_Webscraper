#include <stdio.h>
#include<vector>
#include<string>
#include<iostream>
#include<math.h>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

long long findItGio(long long L, long long C, vector<int> v){
    long long ind = v[0];
    for(int i = 1; i < v.size(); i++){
        ind = ind * L + v[i];
    }
    return ind;
}
vector<long long> doit(long long L, long long C){
    C--;
    vector<long long> ans;
    for(int i = 0; i < L; i+=C+1){
        vector<int> v;
        for(int j = i; j <= min(i + C,L - 1); j++){
            v.push_back(j);
        }
        ans.push_back(findItGio(L,C,v));
    }
    return ans;
}

int main(){
    freopen("/Users/gguliash/ClionProjects/untitled/a.in","r",stdin);
    freopen("/Users/gguliash/ClionProjects/untitled/w.out","w",stdout);

    int t;cin>>t;
    for(int i = 1; i<=t;i ++){
        cout<<"Case #"<<i<<": ";
        long long a,b,c;cin>>a>>b>>c;
        vector<long long> v = doit(a,b);
        if(v.size() == 0 || v.size() > c){
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            for(int j = 0; j < v.size(); j++){
                cout<<v[j]+1;
                if(j + 1 != v.size()) cout<<' ';
                else cout<<endl;
            }
        }
    }

    return 0;
}

