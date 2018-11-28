#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <vector> 
#include <cstdio>
#include <stack>
#include <cassert>
#include <sstream>
using namespace std;  


int main (){ 
    freopen("a.in","r",stdin); 
    freopen("a.out","w",stdout);  
    int T ; 
    cin >> T ; 
    for(int Cas = 1 ; Cas <= T ; ++Cas){  
        map< int,int> mp; 
        for(int i = 0 ; i < 2 ; ++i){
            int x; 
            cin >> x; 
            for(int j = 0; j < 4; ++j){
                for(int k = 0 ; k< 4; ++k){ 
                    int val; 
                    cin >> val; 
                    if( x == j+1 ){ 
                        mp[val]++; 
                    }
                } 
            }
        }
            int ans = -1,cnt=0; 
            for(map<int,int>::iterator it = mp.begin(); it != mp.end(); ++it){ 
                if(it->second==2){ 
                    ans = it->first; 
                    ++cnt; 
                }
            }
            cout <<"Case #"<<Cas<<": ";
            if(cnt == 1 ){ 
                cout <<ans<<endl; 
            }else if(cnt == 0 ){
                cout <<"Volunteer cheated!"<<endl; 
            }else{
                cout <<"Bad magician!"<<endl;
            }
    }
    return 0;
}





