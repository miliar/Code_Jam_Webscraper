#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

int main(void){
    int T;
    cin>>T;
    for(int tcase = 1; tcase <= T; ++tcase){
        long long A, N;
        cin>>A>>N;
        vector<long long> motes(N);
        for(int i=0;i<N;i++) cin>>motes[i];
        sort(motes.begin(), motes.end());
        
        vector<vector<pair<long long, long long> > > DP(N+5);
        DP[0].push_back(make_pair(A,0));
        
        for(int i=0;i<motes.size();i++){
            for(int j=0;j<DP[i].size();++j){
                pair<long long, long long> prev = DP[i][j];
                //consume
                if(prev.first > motes[i]){
                    DP[i+1].push_back(make_pair(prev.first+motes[i], prev.second));
                }
                
                //insert
                long long size = prev.first;
                long long count = 0;
                while(size>1 && size <= motes[i]){
                    size += size-1;
                    ++count;
                }
                if(count > 0){
                    DP[i+1].push_back(make_pair(size+motes[i], prev.second+count));
                }
                
                //skip
                DP[i+1].push_back(make_pair(prev.first, prev.second+1));
            }
        }

        long long result = 1e14;
        for(int i=0;i<DP[N].size();++i){
            if(DP[N][i].second<result) result = DP[N][i].second;
        }
        
        cout<<"Case #"<<tcase<<": "<<result<<endl;
    }
}