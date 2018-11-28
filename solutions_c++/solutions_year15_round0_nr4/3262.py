#include<string>
#include<iostream>
#include<stdio.h>

using namespace std;

string map[4][4][4] = { 
"GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL",
"RICHARD","GABRIEL","RICHARD","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","RICHARD","GABRIEL","RICHARD","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL",
"RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","GABRIEL","RICHARD","RICHARD","GABRIEL","GABRIEL","GABRIEL","RICHARD","RICHARD","GABRIEL","RICHARD",
"RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","GABRIEL","RICHARD","RICHARD","GABRIEL","GABRIEL"	
                   };
int main() {
   freopen("D-small-attempt0.in", "r", stdin);
   int t;
   scanf("%d\n",&t);
   for(int i = 0; i < t; i++){
      int X,R,C;
      scanf("%d %d %d\n",&X,&R,&C);
      cout<<"Case #"<<i+1<<": "<<map[X-1][R-1][C-1]<<endl; 
   }

}
