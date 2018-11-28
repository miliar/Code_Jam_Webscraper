#include <iostream> 
#include <sstream> 
#include <vector> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <string> 
#include <cstring> 

using namespace std; 

int ttt, tttt;

int n,i;
long long p, l, r, c;

int f(long long x){
    long long P = p;
    for (i=1;i<=n;i++){
        if (x == 0) return 1;
        if (P<=(1LL << (n-i))){
                    return 0;
        }
        P = P - (1LL << (n-i));
        x = (x-1)/2;
    }
    return 1;
}

int ff(long long x){
    long long P = p;
    for (i=1;i<=n;i++){
        if (x == (1LL << (n-i+1))-1){
           if (x+1<=P) return 1; else return 0;
        }
        
        x = (x+1)/2;
    }
    return 1;
}

int main(){
    freopen("b2.dat","r",stdin);
    freopen("b2.sol","w",stdout);
    cin >> ttt;
    for (tttt=1;tttt<=ttt;tttt++){
        cout << "Case #" << tttt << ": ";
        cin >> n >> p;
        l = 0;
        r = (1LL << n);
        while (l+1<r){
              c = (l+r)/2;
              if (f(c)) l = c; else r = c;
        }
        
        cout << l << " ";
        
        l = 0;
        r = (1LL << n);
        while (l+1<r){
              c = (l+r)/2;
              if (ff(c)) l = c; else r = c;
        }
        
        cout << l << endl;
        
    }
//    system("pause");
    return 0;
}

 
