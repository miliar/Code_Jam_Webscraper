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

int nnodes;
int trie[100][26];

void add(string &s){
    int pos = 0;
    int L = s.size();
    
    for(int i = 0;i < L;++i){
        if(trie[pos][ s[i] - 'A' ] == 0)
            trie[pos][ s[i] - 'A' ] = nnodes++;
        
        pos = trie[pos][ s[i] - 'A' ];
    }
}

int M,N;
string s[8];

int max_nodes,cont;
vector<int> id[4];

void solve(int pos){
    if(pos == M){
        int aux = 0;
        
        for(int i = 0;i < N;++i)
            if(id[i].empty()) return;
        
        for(int i = 0;i < N;++i){
            memset(trie,0,sizeof trie);
            nnodes = 1;
            
            for(int j = id[i].size() - 1;j >= 0;--j)
                add(s[ id[i][j] ]);
            
            aux += nnodes;
        }
        
        if(aux > max_nodes){
            max_nodes = aux;
            cont = 1;
        }else if(aux == max_nodes) ++cont;
    }else{
        for(int i = 0;i < N;++i){
            id[i].push_back(pos);
            
            solve(pos + 1);
            
            id[i].pop_back();
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    
    int TC;
    
    cin >> TC;
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> M >> N;
        
        for(int i = 0;i < M;++i)
            cin >> s[i];
        
        max_nodes = 0;cont = 0;
        
        solve(0);
        
        cout << "Case #" << tc << ": " << max_nodes << " " << cont << endl;
    }
    
    return 0;
}
