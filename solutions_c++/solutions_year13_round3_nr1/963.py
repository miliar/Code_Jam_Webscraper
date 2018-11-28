#include <algorithm>
#include <iostream>
#include <string.h>
#include <fstream>
#include <sstream>
#include <utility>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>     
#include <stack>
#include <set>
#include <map>

using namespace std;

#define MAXN 2000000
#define xx first 
#define yy second 
#define INF 10000000
#define pb push_back
#define mp make_pair
#define MOD 1000000007

int N , M;
int mem[MAXN] = {0} , beg[MAXN] = {0};
bool vowel[26] = {false};
char vw[] = {'a', 'e', 'i', 'o', 'u'};
int get (int i) {
    if ( i < 0 ) return 0;
    return mem[i];
}
long long solve (char a[MAXN] , int k) {
   memset (mem , 0 , sizeof (mem ) );
   memset (beg , -1, sizeof (beg ));
   
   for (int i = 0; i < N; i ++ ) {
       if ( !vowel[a[i] - 'a'] ) {
            mem[i] = get (i - 1) + 1;
       } else mem[i] = 0;     
   }   
  
   int idx = -1;
   for (int i = 0; i < N; i ++ ) {
        if ( mem[i] >= k ) {
            idx = i - k + 1;        
        }  
        beg[i] = idx;     
   }
   
   long long res = 0LL;
   for (int i = 0; i < N; i ++ ) {
       if (beg[i] != -1 ) {
           res = res + beg[i] + 1;           
       } 
   }
   return res;
}
char a[MAXN];
int T , CASE = 1;
int main() {
    for (int i = 0; i < 5; i ++ ) vowel[vw[i] - 'a'] = 1; 
    freopen ("A-large.in" , "r" , stdin);
    freopen ("out.txt" , "w" , stdout);
    cin >> T;
    while (T--) {
        int l;  
        scanf("%s%d" , a , &l);
        N = strlen (a);
        printf ("Case #%d: %lld\n" , CASE , solve (a , l) );
        CASE ++;       
    }
//system("pause");
return 0;
}


 
