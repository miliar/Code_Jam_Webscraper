#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=0; i<t; i++){
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i+1 << ":";
        unsigned long long power = 1;
        if(c == 1){
            for(int j=1; j<=k; j++) cout << " " << j;
        }else{
            for(int j=1; j<c; j++) power *= k;
            for(int j=0; j<s; j++) cout << " " << (j*power)+j+1;
        }
        cout << endl;
    }
    return 0;
}
