/* Bismillahir rahmanir rahim */
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define INT_MAX     2147483647
#define INT_MIN     -2147483648
#define pi          acos(-1.0)
#define siz         10000000
#define eps         1e-9;

#define rep(i, n)   for(int i = 0; i < (n); i++)
#define fill(a, v)  memset(a, v, sizeof (a))
#define pb          push_back
#define pf          push_front
#define mp          make_pair
#define all(a)      (a).begin(),(a).end()

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;

LL Square(LL n){
    LL s = sqrt(n);
        if(s*s == n)
            return s;
        else
            return 0;
}

bool isPalindrome(LL n){
    if(n % 10 == 0)
        return false;
    int num[100];
    int i, j;
    i = 0;
    while(n){
        LL m = (n % 10);
        num[i++] = m;
        n /= 10;
    }

    i--;
    j = 0;
    while(j < i){
        if(num[i] != num[j])
            return false;
        i--;
        j++;
    }
    return true;
}

int main(){
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C.txt", "w", stdout);

    LL a, b, i, j, k;
    int t, c = 1;

    cin>>t;
    while(t--){
        cin>>a>>b;
        LL count = 0;
        for(i = a; i <= b; i++){
            if(isPalindrome(i)){
                LL s = Square(i);
                if(s && isPalindrome(s))
                    count++;
            }
        }
        cout<<"Case #"<<c++<<": "<<count<<endl;
    }
    return 0;
}
