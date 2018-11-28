#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cmath> 

using namespace std;

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t, K, C, S;
    cin >> t;
    for(int q=0;q<t;q++){
        cout << "Case #" << q+1 << ":";
        cin >> K >> C >> S;
        for(int i=1;i<=K;i++){
            cout << " " << i;
        }
        cout << endl;
    }


    return 0;
}