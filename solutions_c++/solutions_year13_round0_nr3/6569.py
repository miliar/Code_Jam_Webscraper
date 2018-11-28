#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

static int a1[100];
int j = 0;

bool palin(int n) 
{
     stringstream ss;
     ss << n;
     string s = ss.str(),s1;
     s1 = s;
     reverse(s.begin(),s.end());
     return s == s1;
}
     
void pre()
{
     int i,t;
     t = (int)(sqrt(1000));
     for ( i = 1; i <= t; i++ ) {
         if ( palin(i) && palin(i*i) ) {
              a1[j++] = i*i;
         }
     }
     return;
}                               

int main()
{
    int t,c;
    int a,b,i,k;
    freopen ("inp.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    pre();
    
    scanf("%d", &t);
    
    for ( i = 1; i <= t; i++ ) {
          scanf("%d%d", &a, &b);
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

                    
          
          
                    
