#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <functional>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
 
#define rep(i, a) REP(i, 0, a)
#define REP(i, a, b) for(int i = a; i < b; ++i)
#define rrep(i, a) RREP(i, a, 0)
#define RREP(i, a, b) for(int i = a; i >= b; --i)
#define repll(i, a) REPLL(i, 0, a)
#define REPLL(i, a, b) for(ll i = a; i < b; ++i)
#define rrepll(i, a) RREPLL(i, a, 0)
#define RREPLL(i, a, b) for(ll i = a; i >= b; --i)
 
typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> P;
typedef std::pair<int, P> PP;
const double PI = 3.14159265358979323846;
const double eps = 1e-9;
const int infi = (int)1e+9 + 10;
const ll infll = (ll)1e+17 + 10;

typedef std::pair<int, char> MP;

int main(){
    int n;
    std::cin >> n;
    
    rep(i, n){
        int k, sum;
        std::cin >> k;
        
        MP p[30];
        rep(j, k){
            std::cin >> p[j].first;
            p[j].second = 'A' + j;
            sum += p[j].first;
        }
        
        std::cout << "Case #"  << i + 1 << ": "; 
        
        bool f = true;
        while(sum){
            if(!f)std::cout << " ";
            f = false;
            
            std::sort(p, p + k, std::greater<MP>());
                   
            if(p[0].first == 1 && p[1].first == 1 && p[2].first == 1){
                --p[0].first;
                --sum;
                std::cout << p[0].second;
            }
            else if(p[0].first == p[1].first){
                --p[0].first;
                --p[1].first;
                sum -= 2;
                
                std::cout << p[0].second << p[1].second;
            }
            else{
                --p[0].first;
                --sum;
                std::cout << p[0].second;
            }
            
        }
        std::cout << std::endl;
    }
    
    return 0;
}