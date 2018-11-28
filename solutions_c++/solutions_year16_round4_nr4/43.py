#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    
    cout << setprecision(9);
    for(int t=1;t<=T;t++){
        int N;
        cin >> N;
        vector<bool> arow(N, false);
        vector<vector<bool> > adjmat(N, arow);
        
        for(int i=0;i<N;i++){
            string row;
            cin >> row;
            for(int j=0;j<N;j++) adjmat[i][j] = (row[j]=='1');
        }
        
        int initwt = 0;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(adjmat[i][j]) initwt++;
            }
        }
        
        vector<int> cworks;
        vector<int> cmachs;
        
        queue<int> bfs;
        queue<int> type;
        
        vector<bool> usedrow(N, false);
        vector<bool> usedcol(N, false);
        
        int eqcomps = 0;
        int excess = 0;
        
        for(int i=0;i<N;i++){
            if(!usedrow[i]){
                bfs.push(i);
                type.push(0);
                usedrow[i] = true;
                
                int nwork = 0;
                int nmach = 0;
                while(!bfs.empty()){
                    int cur = bfs.front();
                    bfs.pop();
                    int ctype = type.front();
                    type.pop();
                    
                    if(ctype==0) nwork++;
                    else if(ctype==1) nmach++;
                    
                    for(int j=0;j<N;j++){
                        if(ctype==0){
                            //row
                            if(adjmat[cur][j] && !usedcol[j]){
                                usedcol[j] = true;
                               bfs.push(j);
                               type.push(1);
                            }
                        }else{
                            //col
                            if(adjmat[j][cur] && !usedrow[j]){
                                usedrow[j] = true;
                                bfs.push(j);
                                type.push(0);
                            }
                        }
                    }
                }
                if(nwork==nmach){
                    eqcomps += nwork*nwork;
                }else if(nwork==1 && nmach==0){
                    excess++;
                }else{
                    cworks.push_back(nwork);
                    cmachs.push_back(nmach);
                }
//                cout << nwork << " " << nmach << endl;
            }
        }
        
        int M = cworks.size();
        
//         for(int i=0;i<M;i++){
//             cout << i << ": " << cworks[i] << " " << cmachs[i] << endl;
//         }
        
        vector<int> wt(1<<M, -1);
        vector<int> ex(1<<M, 0);
        wt[0] = 0;
        
//         cout << "weights" << endl;
        
        for(int i=1;i<(1<<M);i++){
            int nwork = 0;
            int nmach = 0;
            for(int j=0;j<N;j++){
                if(((1<<j)&i)!=0){
                    nwork += cworks[j];
                    nmach += cmachs[j];
                }
            }
            wt[i] = max(nwork, nmach)*max(nwork, nmach);
            ex[i] = max(0, nmach-nwork);
            
//             cout << i << ": " << wt[i] << endl;
        }
        
        vector<int> dprow(excess+1, 1000000);
        vector<vector<int> > dp(1<<M, dprow);
        for(int r=0;r<=excess;r++){
            dp[0][r] = r;
        }
        
        for(int i=1;i<(1<<M);i++){
            for(int j=0;j<=i;j++){
                if((j&i)==j){
                    for(int r=ex[j];r<=excess;r++){
                        dp[i][r] = min(dp[i][r], dp[i-j][r-ex[j]] + wt[j]);
                    }
                }
            }
        }
        
        
//         cout << "initwt: " << initwt << endl;
        int ans = dp[(1<<M)-1][excess] + eqcomps - initwt;
        
        
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}