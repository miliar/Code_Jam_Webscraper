/*
   Problem:
   Author: Akai
   Date: 2012//
   Meaning£º
   Algorithm£º
*/
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

long long a[10000001] ;
int b[20] ;
int T , tot = 0 ; ;

bool check(long long x){
     int k = 0 ;
     while (x > 0){
           b[++k] = x % 10 ;
           x /= 10 ;
     }
     for (int i = 1 ; i <= (k >> 1) ; i++)
      if (b[i] != b[k-i+1]) return 0;
      return 1 ;
      }

int get(long long x){
    if (x == 0) return 0 ;
    if (x > a[tot]) return tot ;
    for (int i = 1 ; i <= tot ; i++) if (a[i] > x) return i- 1;
    return tot ;
}


int main(){
//	freopen("C-small-attempt0.in", "r", stdin);
 //	freopen("C-small-attempt.out", "w", stdout);
	freopen("C-large-1.in", "r", stdin);
 //	freopen("C-large-2.out", "w", stdout);
    for (int i = 1 ; i <= 10000000 ; i++)
        if (check(i))
           if (check((long long)i * (long long)i)){
                            a[++tot] = (long long)i * (long long)i ;
   //                         if (i <= 1000ll) cout << i << " " ;
    }
   // cout << tot << endl ;  
   // scanf("%d" , &T);
    cin >> T ;
    for (int cases = 1 ; cases <= T ; cases++){
          printf("Case #%d: " , cases);
          long long x , y;
         // scanf("%d%d" , &x , &y);
          cin >> x >> y ;
      //    printf("%d %d\n" , get(y) , get(x)) ;
          printf("%d\n" , get(y) - get(x - 1) ) ;
    
    
    }
         
	return 0;
}
