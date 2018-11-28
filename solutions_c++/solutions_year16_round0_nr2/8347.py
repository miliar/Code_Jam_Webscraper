#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <deque>

using namespace std;

int main (){
    freopen("b.in","r", stdin);
    freopen("b.out","w", stdout);
    
    int T;
    cin >> T;
    
    for (int cas = 1; cas <= T; ++cas){
        string str;
        cin >> str;
        cout <<"Case #"<< cas <<": ";
        
        int res = 0; 
        
        for (int i = 1; i < str.length(); ++i)
            res += str[i] != str[i-1];
        res++;  
        if (str[str.length()-1] == '+')
            res--;
        cout << res << endl; 
    }
    return 0;
}





