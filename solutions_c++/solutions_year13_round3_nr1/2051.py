#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include<fstream>
 
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long
 
#define For(i, a, b) for ( int i = (a); i < (b); i++ )
#define Fors(i, sz) for ( size_t i = 0; i < sz.size (); i++ )
#define Set(a, s) memset (a, s, sizeof (a))
 
using namespace std;

bool consonant(char ch){
    if(ch == 'a' || ch == 'e' || ch == 'u' || ch == 'o' || ch == 'i')
        return false;
    return true;
}

bool okstring(string s, int n){
int d = 0;
    for(int i = 0; i < s.size(); ++i){
        if(consonant(s[i])){
            d++;
            if(d == n)  return true;
         }
        else 
            d = 0;
    }
    return false;
}

int main(){
int T;
            int max = 0;
string s;
int n;
        ifstream finput("A-small-attempt0(1).in");
        ofstream output("gcj1.out");
        
        finput>>T;
        for(int i = 1; i <= T; ++i){
            finput>>s;
            finput>>n;
			max = 0;
            for(int j = 0; j < s.size(); ++j){
                for(int k = 0; k <= j; ++k){
                    string tstre = s.substr(k, j-k+1);
                    if(okstring(tstre, n))   max++;
                }
            }
            output<<"Case #"<<i<<": "<<max<<endl;
        }
return 0;
}
