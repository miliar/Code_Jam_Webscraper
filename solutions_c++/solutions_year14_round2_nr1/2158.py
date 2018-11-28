using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) //cout << #x " = " << (x) << endl

string a, aux1, b, aux2;
string crearAux(string m){
   int n = m.size();
   string s = "";
   if(n >= 0){
      s += m[0];
      for(int i = 1; i < n; ++i)
         if(m[i] != m[i-1]) s += m[i];     
   }
   return s;
}
int contarDif(){
   int acumm = 0;
   int acuma = 0; int acumb = 0;
   for(int i = 0; i < aux1.size(); ++i){
      int acum1, acum2; acum1 = acum2 = 0;
      for(int j = acuma; j < a.size(); ++j){
         acuma++;
         if(a[j] == aux1[i]) acum1++;
         else break;
      }
      for(int j = acumb; j < b.size(); ++j){
         acumb++;
         if(b[j] == aux1[i]) acum2++;
         else break;        
      }
      acumm += abs(acum1 - acum2);
   }
   return acumm;
}
int t;
int main(){
    D('a' != 'a');
   cin >> t;
   int z = 1;
   while(t--){
      int nada; cin >> nada;
      cin >> a >> b;
      aux1 = crearAux(a); aux2 = crearAux(b);
      int n1 = a.size(); int n2 = b.size();
      D(aux1); D(aux2);
      if(aux1 == aux2) cout << "Case #" << z++ << ": " << contarDif() << endl;
      else cout << "Case #" << z++ << ": " << "Fegla Won" << endl;
    //  cout << "Case #" << z++ << ": " << << endl;           
   // cout << "Case:" << z++ << endl << a << endl << b << endl << aux1 << endl << aux2 << endl;
   } 
    
   return 0;    
}
