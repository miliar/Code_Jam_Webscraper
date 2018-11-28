#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#define INF 1000000000000LL

typedef long long int64;
typedef unsigned long long qword;
using namespace std;

/* Problem: Google Code Jam Qualification Round 2013
 *          Problem B. Lawnmower
 * URL: https://code.google.com/codejam/contest/2270488/dashboard#s=p1
 */



int main() {
   int s,t;
   int n,m;
   int i,j,x,y,h;
   int board[101][101];
   bool check[101][101];
   cin>>t;
   for(s=1; s<=t; s++) {
      cin>>n;
      cin>>m;
      for (i=0; i<n; i++) {
         for (j=0; j<m; j++) {
            cin>>board[i][j];
         }
      }
      int temp;
      bool ans = true;
      bool isOK;
      for (i=0; i<n; i++){
         for (j=0; j<m; j++) {
            //if (!check[i][j]) {
               temp = board[i][j];
               //check row
               isOK = true;
               for (x=0; x<n; x++) {
                  if (board[x][j] <= temp) {
                     //ok
                  } else {
                     isOK = false;
                  }
               }
               if (!isOK){
                  //check column
                  isOK = true;
                  for (x=0; x<m; x++) {
                     if (board[i][x] <= temp) {
                        //ok
                     } else {
                        isOK = false;
                     }
                  }
               }
               if (!isOK) {
                  ans = false;
                  break;
               }
            //}
         }
      }
      cout<<"Case #"<<s<<": ";
      if (ans) {
         cout<<"YES";
      } else {
         cout<<"NO";
      }
      cout<<endl;
   }
   return 0;
}
