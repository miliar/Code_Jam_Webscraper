#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    
    int T;
    in>>T;
    for(int k=0;k<T;k++) {
        int N;
        in>>N;
        vector<pair<double, bool> > naomiblocks;
        vector<pair<double, bool> > kenblocks;
        for(int i=0;i<N;i++) {
            double tmp;
            in>>tmp;
            naomiblocks.push_back(pair<double,bool>(tmp,false));
        }
        for(int i=0;i<N;i++) {
            double tmp;
            in>>tmp;
            kenblocks.push_back(pair<double,bool>(tmp,false));
        }
        sort(naomiblocks.begin(),naomiblocks.end());
        sort(kenblocks.begin(),kenblocks.end());
        
        
        int normal_war = 0;
        for(vector<pair<double,bool> >::iterator iter = naomiblocks.begin();iter!=naomiblocks.end();iter++) {
            vector<pair<double, bool> >::iterator kenloc = lower_bound(kenblocks.begin(), kenblocks.end(), *iter);
            while(kenloc != kenblocks.end() && kenloc->second)
                kenloc++;
            if(kenloc == kenblocks.end())
                normal_war++;
            else
                kenloc->second = true;
        }
        for(vector<pair<double,bool> >::iterator iter = kenblocks.begin();iter!=kenblocks.end();iter++)
            iter->second = false;
        
        
        int special_war = 0;
        vector<pair<double,bool> >::iterator naomiiter = naomiblocks.begin();
        for(vector<pair<double,bool> >::iterator iter = kenblocks.begin();iter!=kenblocks.end();iter++) {
            while(naomiiter != naomiblocks.end() && naomiiter->first < iter->first)
                naomiiter++;
            if(naomiiter != naomiblocks.end()) {
                special_war++;
                naomiiter++;
            }
        }
        out<<"Case #"<<(k+1)<<": "<<special_war<<" "<<normal_war<<"\n";
    }
}