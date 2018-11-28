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

vector<string> V;
vector<vector<int> > occ;
int n;

void init(string s,int ind){
    char c=s[0],cpt=0;
    for (int i=1;i<s.size();++i){
        if (s[i]==c) {
            cpt++;
        } else {
            V[ind].push_back(c);
            c=s[i];
            occ[ind].push_back(cpt);
            cpt=0;
        }
    }
    V[ind].push_back(c);
    occ[ind].push_back(cpt);
}

bool check(){
    for (int i=1;i<n;++i){
        if (V[0]!=V[i]) return false;
    }
    return true;
}

int main(){
    ifstream fin("A-small-attempt0.in");
    ofstream fout(" A-small-attempt0.out");
    int t; fin>>t;
    for (int k=1;k<=t;++k){
        occ.clear();
        V.clear();
        fin>>n;
        V.resize(n);
        occ.resize(n);
        string a;
        for (int i=0;i<n;++i) {
            fin>>a;
            init(a,i);
        }

       // for (int i=0;i<n;++i) {for (int j=0;j<V[i].size();++j) fout<<occ[i][j]<<" "; fout<<endl;}


        if (check()){
            long long res=0;
            for(int i=0;i<occ[0].size();++i){
                int mx=0,mn=numeric_limits<int>::max();
                for (int j=0;j<n;++j){
                    mx=(max(mx,occ[j][i]));
                    mn=(min(mn,occ[j][i]));
                }
                res+=(mx-mn);
            }
            fout<<"Case #"<<k<<": "<<res<<endl;
        } else {
            fout<<"Case #"<<k<<": Fegla Won"<<endl;
        }
    }
    return 0;
}
