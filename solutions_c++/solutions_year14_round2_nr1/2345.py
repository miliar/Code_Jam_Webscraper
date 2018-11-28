#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attemt0.out", "w", stdout);
    int T;
    cin>>T;
    string cad[105];
    for(int i=1;i<=T;i++){
        int N;
        cin>>N;
        for(int j=0;j<N;j++) cin>>cad[j];
        int res=0;
        vector<pair<char, int> > subun;
        vector<pair<char, int> > subdos;
        for(int j=0;j<cad[0].size();j++){
            if(subun.empty()||subun[subun.size()-1].first!=cad[0][j]){
                pair<char, int> Npar;
                Npar.first=cad[0][j];
                Npar.second=1;
                subun.push_back(Npar);
            } else {
                subun[subun.size()-1].second++;
            }
        }
        for(int j=0;j<cad[1].size();j++){
            if(subdos.empty()||subdos[subdos.size()-1].first!=cad[1][j]){
                pair<char, int> Npar;
                Npar.first=cad[1][j];
                Npar.second=1;
                subdos.push_back(Npar);
            } else {
                subdos[subdos.size()-1].second++;
            }
        }
        if(subun.size()!=subdos.size()){
            cout<<"Case #"<<i<<": Fegla Won"<<endl;
            continue;
        }
        bool nofunc=false;
        for(int j=0;j<subun.size();j++){
            if(subun[j].first!=subdos[j].first){
                nofunc=true;
                break;
            } else {
                res+=abs(subun[j].second-subdos[j].second);
            }
        }
        if(nofunc){
            cout<<"Case #"<<i<<": Fegla Won"<<endl;
            continue;
        } else {
            cout<<"Case #"<<i<<": "<<res<<endl;
        }
    }
    return 0;
}
