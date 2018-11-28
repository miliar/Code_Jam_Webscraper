#include<string>
#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

string sol[4][4][4] = { 
"GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL",
"RICHARD","GABRIEL","RICHARD","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL","RICHARD","GABRIEL","RICHARD","GABRIEL","GABRIEL","GABRIEL","GABRIEL","GABRIEL",
"RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","GABRIEL","RICHARD","RICHARD","GABRIEL","GABRIEL","GABRIEL","RICHARD","RICHARD","GABRIEL","RICHARD",
"RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","RICHARD","GABRIEL","RICHARD","RICHARD","GABRIEL","GABRIEL"	
                   };
int main() {
   //freopen("input.in", "r", stdin);
   //freopen("B-large.in", "r", stdin);
   freopen("D-small-attempt2.in", "r", stdin);
   int t;
   scanf("%d\n",&t);
   //cout<<t;
   for(int i = 0; i < t; i++){
      int x,r,c;
      scanf("%d %d %d\n",&x,&r,&c);
      //cout<<x<<" "<<r<<" "<<c<<endl;
      cout<<"Case #"<<i+1<<": "<<sol[x-1][r-1][c-1]<<endl; 
   }

}
