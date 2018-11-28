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

bool cons(char c){
    if(c == 'a' || c == 'e' || c == 'i' || c == 'u' || c == 'o')
        return false;
    return true;
}

bool good(string s, int n){
int k = 0;
//bool flag = true;
    for(int i = 0; i < s.size(); ++i){
        if(cons(s[i])){
            k++;
            if(k >= n)  return true;
         }
        else {
//            flag = false;
            k = 0;
        }
    }
    return false;
}

int main(){
int T;
string s;
int n;
        ifstream fin("A-small-attempt0.in");
        ofstream fout("1.out");
        
        fin>>T;
        for(int i = 1; i <= T; ++i){
            fin>>s;
            fin>>n;
            int num = 0;
            for(int j = 0; j < s.size(); ++j){
                for(int k = 0; k <= j; ++k){
                    string str = s.substr(k, j-k+1);
                    if(good(str, n))   num++;
                }
            }
            fout<<"Case #"<<i<<": "<<num<<endl;
        }
return 0;
}
