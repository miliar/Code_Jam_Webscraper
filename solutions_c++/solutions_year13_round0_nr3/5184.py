#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <cstring>
#include <cmath>
#include <functional>
#include <set>
#include <sstream>

using namespace std;
#define foreach(x,v) for( typeof(v.begin()) x = v.begin(); x != v.end(); x++)
#define For(i,n) for(int i = 0; i < n; i++)
#define pf printf
#define sc scanf
#define pb push_back

bool isPalindome(long long n){
    stringstream ss;
    ss << n;
    string number;
    ss >> number;
    bool flag = true;
    For(i,number.size()){
        if( number[i] != number[number.size()-1-i]){
            flag = false;
            break;
        }
    }
    return flag;
}
int main (int argc, char const* argv[])
{
    int sum,T;
    vector<long long> palindromes;
    For(i,10000000){
        long long t = i+1;
        long long r = sqrt(t);
        
        if(isPalindome(t) && r*r == t && isPalindome(r)){

            palindromes.pb(t);
        }
    }
    
    sc("%d",&T);
    For(cases,T){
        
        int a, b;
        sum = 0;
        sc("%d %d", &a,&b);
        foreach(x,palindromes){
            
            if( (*x) >= a && (*x) <= b){
                sum++;
            }
        }
        pf("Case #%d: %d\n",cases+1,sum);
    }
    
    return 0;
}
