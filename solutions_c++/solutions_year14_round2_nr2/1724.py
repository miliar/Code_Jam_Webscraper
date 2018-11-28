#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <limits>
#include <string>
#include <queue>
#include <cstdio>
using namespace std;

int main(){
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");
    int t; fin>>t;
    for (int c=1;c<=t;++c){
        long long a,b,k,res=0;
        fin>>a>>b>>k;
        for (int i=0;i<a;++i){
            for (int j=0;j<b;++j){
                if ((i&j)<k) res++;
            }
        }
        fout<<"Case #"<<c<<": "<<res<<endl;
    }
    return 0;
}
