#include <cstdio>
#include <algorithm>
using namespace std;


int n,t,p[100],a[100],b[100],test;

void solve() {
     test++;
     printf("Case #%d: ",test);
     
     scanf("%d",&n);
     
     int x;
          
     for (int i = 0; i < 4; i++) {
          for (int j = 0; j < 4; j++) {
               scanf("%d",&x);
               if (i + 1 == n) a[j] = x;}}


     scanf("%d",&n);
     
     for (int i = 0; i < 4; i++) {
          for (int j = 0; j < 4; j++) {
               scanf("%d",&x);
               if (i + 1 == n) b[j] = x;}}

     int sol = 0,sol1;
     
     for (int i = 0; i < 4; i++) 
          for (int j = 0; j < 4; j++) 
               if (a[i] == b[j]) {sol++; sol1 = a[i];}
     
     if (sol > 1) 
          printf("Bad magician!\n");
     else if (sol == 0) 
          printf("Volunteer cheated!\n");
     else 
          printf("%d\n",sol1);}

int main() {
     scanf("%d",&t);
     while (t--) solve();
     
     return 0;}
