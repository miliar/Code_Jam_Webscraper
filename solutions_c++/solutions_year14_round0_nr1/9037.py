#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>
#define FOR(i,a,b) for(int i = a; i< b; i++)
#define READ(x) freopen(x,"r",stdin)
#define WRITE(x) freopen(x,"w",stdout)

using namespace std;

int main(){
    READ("A.txt");
    WRITE("Aout.txt");
    int test; scanf("%d",&test);
    set<int> hold;
    vector<int> common;
    int tc = 1;
    while(test--){
        cout<<"Case #"<<tc++<<": ";
        int n1; cin>>n1;n1--;
        int grid[4][4];
        hold.clear(); common.clear();
        FOR(i,0,4) FOR(j,0,4) cin>>grid[i][j];
        FOR(i,0,4) hold.insert(grid[n1][i]);
        cin>>n1;n1--;
        FOR(i,0,4) FOR(j,0,4) cin>>grid[i][j];

        FOR(i,0,4) {
            int x = grid[n1][i];
            if(hold.count(x)>0) common.push_back(x);
        }
        if(common.size()==0) cout<<"Volunteer cheated!\n";
        else if(common.size()==1) cout<<common[0]<<endl;
        else if(common.size()>1) cout<<"Bad magician!\n";
    }
    return 0;
}
