#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <time.h>
using namespace std;
#define MAX 105
#define pii pair<long long , long long>
#define mp make_pair
#define psi pair<string , int>

int solve( string s ){
    int n = s.length();
    int ans = 0;
    int i = 0;
    while( i < n ){
        int j = i + 1;
        while( j < n && s[j] == s[i] ){
            j++;
        }
        if( j < n ){
            char next = s[j];
            for( int k = 0 ; k < j ; ++k ){
                s[k] = next;
            }
            ans++;
        }else{
            if(s[0] == '-'){
                ans++;
            }
            break;
        }
    }
    return ans;
}

int main() {
    int t;
    string s;
    scanf("%d" , &t );
    for( int q = 1 ; q <= t && cin>>s ; ++q ){
        printf("Case #%d: %d\n", q, solve(s)  );
    }
    return 0 ;
}
