#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

static long long a1[100];
int j = 0;

bool palin(long long n) 
{
     stringstream ss;
     ss.clear();
     ss << n;
     string s = ss.str(),s1;
     s1 = s;
     reverse(s.begin(),s.end());
     return s == s1;
}
     
void pre()
{
     int t;
     long long i,p;
     t = 10000000;
     for ( i = 1; i <= t; i++ ) {
         p = i*i;
         if ( palin(i) && palin(p) ) {
              //cout << i << " " << p << endl;
              a1[j++] = p;
         }
     }
     return;
}                               

int main()
{
    int t,c,i,k;
    long long a,b;
    
    pre();
    
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    
    for ( i = 1; i <= t; i++ ) {
          scanf("%lld%lld", &a, &b);
          c = 0;
          for ( k = 0; k < j; k++ ) {
              if ( a1[k] >= a && a1[k] <= b ) {
                 c++;
              }
          }
          printf("Case #%d: %d\n", i, c);
    }
    
    return 0;
}
