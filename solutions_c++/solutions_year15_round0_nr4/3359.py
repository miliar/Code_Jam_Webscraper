#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main(){
    freopen("/Users/Omar/Desktop/input.txt","rt",stdin);
    freopen("/Users/Omar/Desktop/output.txt","wt",stdout);
    int x, r, c, t;
    scanf("%d",&t);
    
    for (int i=1; i<=t; i++){
        scanf("%d%d%d",&x,&r,&c);
        if (x == 1) cout << "Case #" << i << ": " << "GABRIEL\n";
        else if (x == 2){
            if ((r * c) % 2 == 1){
                cout << "Case #" << i << ": " << "RICHARD\n";
            }
            else cout << "Case #" << i << ": " << "GABRIEL\n";
        }
        else if (x == 3){
            if (r == 1 || c == 1) cout <<"Case #" << i << ": " << "RICHARD\n";
            else if (r == 2 && c == 2)
                cout <<"Case #" << i << ": " << "RICHARD\n";
            else if ((r == 2 && c == 3) || (r == 3 && c == 2))
                cout <<"Case #" << i << ": " << "GABRIEL\n";
            else if ((r == 2 && c == 4) || (r == 4 && c == 2))
                cout <<"Case #" << i << ": " << "RICHARD\n";
            else if (r == 3 && c == 3) cout <<"Case #" << i << ": " << "GABRIEL\n";
            else if ((r == 3 && c == 4) || (r == 4 && c == 3)) cout <<"Case #" << i << ": " << "GABRIEL\n";
            else if (r == 4 && c == 4) cout <<"Case #" << i << ": " << "RICHARD\n";
        }
        else if (x == 4){
            if (r == 1 || c == 1) cout <<"Case #" << i << ": " << "RICHARD\n";
            else if (r == 2 && c == 2) cout <<"Case #" << i << ": " << "RICHARD\n";
            else if ((r == 2 && c == 3) || (r == 3 && c == 2))
                cout <<"Case #" << i << ": " << "RICHARD\n";
            else if ((r == 2 && c == 4) || (r == 4 && c == 2))
                cout <<"Case #" << i << ": " << "RICHARD\n";
            else if (r == 3 && c == 3) cout <<"Case #" << i << ": " << "RICHARD\n";
            else if ((r == 3 && c == 4) || (r == 4 && c == 3))
                cout <<"Case #" << i << ": " << "GABRIEL\n";
            else if (r == 4 && c == 4) cout <<"Case #" << i << ": " << "GABRIEL\n";
            
        }
    }
    
    
    return 0;
}