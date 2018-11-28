#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

vector<vector<int> > V(4);
set<int> S;

int main (){
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int t,res,sz; fin>>t;
    for (int i=0;i<4;++i) V[i].resize(4);
    for (int cpt=1;cpt<=t;++cpt){
        S.clear();
        for (int k=0;k<2;++k){
            int row; fin>>row;
            for (int i=0;i<4;++i){
                for (int j=0;j<4;++j){
                    fin>>V[i][j];
                    if (i+1==row) {
                        sz=S.size();
                        S.insert(V[i][j]);
                        if (sz==S.size()) res=V[i][j];
                    }
                }
            }
        }
        sz=S.size();
        fout<<"Case #"<<cpt<<": ";
        if (sz==8) fout<<"Volunteer cheated!"<<endl;
        else if (sz==7) fout<<res<<endl;
        else fout<<"Bad magician!"<<endl;
    }
    return 0;
}
