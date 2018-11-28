#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <math.h>
using namespace std;


int main(){

  //  freopen("DATA.txt","r",stdin);
  //  freopen("DATA2.txt","w",stdout);
    int T; cin>>T;
    for(int i = 0; i < T; i++){
        int m; cin>>m;
        string s; cin>>s;
        int total = 0;
        int add = 0;
        vector<int> vec;
        for(int j = 0; j <s.size(); j++){
            vec.push_back(s[j]-'0');
        }
        total = vec[0];
        for(int j = 1; j < s.size(); j++){
            if(j>total){
                add+=(j-total);
                total+=(j-total);
            }
                total+=vec[j];
        }
        cout<<"Case #"<<i+1<<": "<<add<<endl;
    }
    return 0;
}

