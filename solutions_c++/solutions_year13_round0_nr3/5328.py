#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>

#define ll long long int

using namespace std;

ll T;
ll A, B;
ll ans;

bool rCheck(int n){
    stack<int> t;
    queue<int> b;
    int cnt = 0;
    while( n > 0){
        t.push(n%10);
        b.push(n%10);
        n /= 10;
        cnt++;
    }

    for(int i = 0; i * 2 <= cnt; i++){
        if( t.top() != b.front()){
            return false;
        }
        t.pop();
        b.pop();
    }
    return true;
}

int main(){
    
    cin >> T;
    
    for( int t = 0; t < T; t++){
        ans = 0;
        cin >> A >> B;
        for(int i = A; i <= B; i++){
            if(i / 10 == 0){
                if(i == 1 || i == 4 || i == 9){
                    ans++;
                    //cout << 'A' << i << endl;
                }
            }else{
                bool f = false;
                int j = 3;
                for(; j * j <= i; j++){
                    if(j * j == i){
                        f = true;
                        break;
                    }
                }
                if(f && rCheck(i) && rCheck(j)){
                    ans++;
                    //cout << 'A' << i << endl;
                }
            }
        }
        cout << "Case #" << t+1 << ": " << ans <<endl;
    }
    
    return 0;
}