#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int bit[1001];

void update(int x, int val){
    for(int idx = x;idx <= 1000;idx += (idx & -idx))
        bit[idx] += val;
}

int query(int x){
    int ret = 0;
    
    for(int idx = x;idx > 0;idx -= (idx & -idx))
        ret += bit[idx];
    
    return ret;
}

int main(){
    ios::sync_with_stdio(0);
    
    int TC;
    
    cin >> TC;
    
    int N;
    pair<int, int> A[1000];
    int pos[1001];
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> N;
        
        for(int i = 0;i < N;++i){
            cin >> A[i].first;
            A[i].second = i + 1;
        }
        
        sort(A,A + N);
        
        for(int i = 0;i < N;++i)
            A[i].first = i + 1;
        
        for(int i = 0;i < N;++i)
            for(int j = i + 1;j < N;++j)
                if(A[i].second > A[j].second)
                    swap(A[i],A[j]);
        
        for(int i = 0;i < N;++i) pos[ A[i].first ] = A[i].second;
        for(int i = 1;i <= N;++i) update(pos[i],1);
        
        int ans = 0;
        
        for(int i = 1,have = N;i <= N;++i,--have){
            int x = query(pos[i]);
            ans += min(x - 1,have - x);
            update(pos[i],-1);
        }
        
        
        cout << "Case #" << tc << ": " << ans << endl;
    }
    
    return 0;
}
