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
    freopen("d.in","r",stdin); 
    freopen("d.out","w",stdout); 
    int T ; 
    cin >> T;
    for(int Cas = 1; Cas <= T ; ++Cas){ 
        int n;
        cin >> n ; 
        vector< double > x(n),y(n); 
        for(int i = 0 ; i < n ; ++i)
            cin >> x[i]; 
        for(int i = 0 ; i < n ; ++i)
            cin >> y[i];
        sort(x.begin(),x.end());
        sort(y.begin(),y.end());
       
        int cur = 0,ans1=0 ; 
        for(int i =  0 ; i < n ; ++i){ 
            int have = 0 ; 
            for(int j = n - 1-i; j >= 0 ; --j){
                if( y[j] < x[ j + i ])
                    ++have; 
            }
            ans1 = max(ans1,cur+have);
            cur += x[i] > y[n-i-1]; 
        }
        cur = 0; 
        int  ans2=0;
        vector< bool > used(n,false); 
        for(int i=0; i < n; ++i){ 
            for(int j=0; j < n; ++j){
                if(used[j] || y[j] < x[i] ) 
                    continue; 
                else{
                    used[j]=1;
                    ++cur;
                    break;
                }
            }
        }
        ans2 = n - cur; 
        cout << "Case #"<<Cas<<": "<< ans1<<" "<<ans2<<endl; 
    }
    return 0;
}

