#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

int main (){
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T;
    
    cin >> T;
    


    for (int cas = 1; cas <= T; ++cas){

        string s; 
        int k;
        cin >> s >> k;
        int res = 0;
        for (size_t i = 0; i < 1 + s.size() - k ; ++i){
            if (s[i] =='-'){
                ++res;
                for (int j = i; j < i + k; ++j)
                    s[j] = s[j]=='+'?'-':'+';
            }
        } 
        
        bool can = true;
        for (size_t i = 0; i < s.size(); ++i)
            if (s[i] == '-')
                can = false;

        cout <<"Case #" << cas <<": ";
        if (can) 
            cout << res << endl;
        else
            cout << "IMPOSSIBLE" << endl; 
    }
    
    return 0;
}

                

