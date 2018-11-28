#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <vector> 
#include <cstdio>
#include <stack>
#include <cassert>
#include <sstream>
using namespace std;  

#define two(x) ((1)<<(x))
set< string > se[ 1 << 8 ];

inline int lowbit(int x){return x&-x; }
int main (){
    int T ;
    freopen("d.in","r",stdin); 
    freopen("d.out","w",stdout); 
    cin >> T ; 
    for(int Cas = 1 ;Cas <= T ; ++Cas){ 
       int M, N; 
       cin >>M>>N;
       for(int i=0; i < two(M); ++i)
           se[i].clear();
       for(int i= 0 ; i < M; ++i){ 
            string s;
            cin >> s; 
            for(int j = 0 ; j < s.length();++j)
                se[ 1 << i].insert( s.substr(0,j+1)); 
       }
       for(int i=0; i < two(M); ++i){
           if(lowbit(i) == i ) continue; 
           se[ i ] = se[i-lowbit(i)]; 
           int j = lowbit(i); 
           for(set<string>::iterator it = se[j].begin(); it != se[j].end(); ++it){ 
               se[i].insert(*it); 
           }
       }

       int bd = 1; 
       for(int i = 0; i < M; ++i) 
           bd = bd*N ; 
       int most = 0, cnt = 0 ;
       int st[4]; 
       for(int i= 0; i < bd; ++i){ 
           memset(st,0,sizeof(st)); 
           for(int j=i , w = 0; w < M ; ++w){ 
               st[ j%N] |= two(w); 
               j/=N; 
           }
           bool can = true; 
           for(int j=0; j < N ; ++j)
                if(!st[j]) can = false;
           if(!can) continue; 
           int cur = 0 ; 
           for(int j = 0 ; j < N ; ++j)
               cur += se[ st[j]].size();
           if(cur > most){  
               most =cur ;
               cnt = 1; 
           }else if (cur == most){
               ++cnt;
           }
       }
       cout <<"Case #"<<Cas<<": "<< most+N <<" " << cnt <<endl; 
    }
    return 0; 
}

