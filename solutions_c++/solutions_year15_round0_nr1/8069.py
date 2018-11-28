/*
ID: gerel1
LANG: C++
TASK:
*/
// Author :
// Date :
// Problem:
// Solution:
// Comment:

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <iomanip>

#define pp push
#define pb push_back
#define mp make_pair
#define xx first
#define yy second

using namespace std;

int k = 1;
void solve(){
    int n;
    int prev=0;
    int add=0;
    
    string str;
    
    cin >> n >> str;
    
    for(int i = 0 ; i <= n ; i++){
        int cur = str[i]-'0';
        //cout << cur << " " << prev << " " << i << endl;
        if(prev >= i){
            //cout << "x" << endl;
            prev+=cur;
        }
        else{
            add+=i-prev;
            prev=i+cur;
        }
    }
    
    cout << "Case #" << k << ": " << add << endl;
    k++;   
}
main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t;
    
    cin >> t;
    
    while(t--){
        solve();
    }
    return 0;
}
