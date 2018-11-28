#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <vector>

#define F first
#define S second

using namespace std;

    long long n, a, b[11];

    bool gama(){
        for(long long i=0; i<10; i++) if(b[i] == 0) return false;
        return true;
    }

    void beta(long long a){
        for(; a!=0; a/=10) b[a%10] = 1;
    }

    void alpha(long long a, long long g){
        for(long long i=0; i<10; i++) b[i]=0;
        long long i=1;
        for(; i<=10000000; i++){
            if(gama()){cout << "Case #" << g << ": " << a*(i-1) << "\n"; return;}
            beta(a*i);
        }
        cout << "Case #" << g << ": INSOMNIA\n";
    }

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for(long long i=0; i<n; i++){cin >> a; alpha(a, i+1);}
}
