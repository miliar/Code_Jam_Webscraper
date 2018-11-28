#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main()
{ string a="a.in" ;string b="b.txt" ;
ifstream File(a.c_str());
ofstream Fil(b.c_str());
int n; File>>n;
for(int t=1;t<=n;t++) {
    int add=0,abb =0 ;
    int  b ; File>>b ;
int s ; File>>s ;     int po= pow(10,b); int u=s/po ;  int cl =u ; s=s-po*u;
 for (int q=1;q<=b;q++){
        int po= pow(10,b-q);
        int r=s/po ;s=s-r*po ;
        if(r>0){
    if (q<=cl) cl=cl+r ;
 else {
    abb=q-cl ;
    add=add+abb ;
    cl=cl+r+abb;
 }
 }}
Fil<<"Case #"<<t<<":"<<add<<endl ;
  }
return 0;
}