#include <iostream>
#include <vector>
#include <set>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int i = 0; i < t; ++i) {
        cout<<"Case #"<<i+1<<": ";
        int a,b;
        int q[4][4];
        int w[4][4];
        cin>>a;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin>>q[i][j];
            }
        }
        cin>>b;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin>>w[i][j];
            }
        }
        --a,--b;
        set<int> cute;
        for(int i = 0; i < 4; ++i) {
            cute.insert(q[a][i]);
        }
        vector<int> lol;
        for(int i = 0; i < 4; ++i) {
            if(cute.count(w[b][i])) lol.push_back(w[b][i]);
        }
        if(lol.size() == 0) {
            cout<<"Volunteer cheated!\n";
        }
        else if(lol.size() > 1) {
            cout<<"Bad magician!\n";
        }
        else {
            cout<<lol[0]<<'\n';
        }
    }
}
