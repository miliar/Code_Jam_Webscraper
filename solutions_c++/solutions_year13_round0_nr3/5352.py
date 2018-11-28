#include <iostream>
#include <math.h>
#include <sstream>

using namespace std;

bool p(int x){
    
    int a,b;
    stringstream s1;
    s1 << x;
    string n1;
    n1 = s1.str();
    a = 0;
    b = n1.size() -1;
    while(a <= b){
        if(n1[a] != n1[b])
        return false;
        a++;
        b--;        
    }
//cout << n1 << "palindromo\n";
   
    int l;
    
     l = sqrt(x);
     
     stringstream s2;
    s2 << l;
    string n2;
    n2 = s2.str();
    a = 0;
    b = n2.size() -1;
    while(a <= b){
        if(n2[a] != n2[b])
        return false;
        a++;
        b--;        
    }
       //  cout << n2 << "palindromo\n\n\n";
    return true;
}

int main()
{
   int qtd,a,b,n,z,total;
   double raiz;
   cin >> qtd;
   
   for(z = 0; z < qtd; z++){
         cin >> a >> b;
         total = 0;
       for(int x = a; x <=b; x++){
           raiz = sqrt(x);
raiz = floor(raiz);
//	cout << x << " -> " << raiz*raiz<< endl;
           if(double(raiz*raiz) == x)
              if(p(x))
               total++;
       }
       cout << "Case #" << z+1 << ": " << total;
       if(z != qtd-1)
            cout << endl;
   }
     
   return 0;
}
