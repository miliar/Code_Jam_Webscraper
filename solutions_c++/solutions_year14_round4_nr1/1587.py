#include <iostream>
#include <set>

int main( )
{
   int t;
   std::cin >> t;
   
   for (int ti = 0; ti < t; ++ti) {
      int n, c;
      std::cin >> n >> c;
      
      std::multiset<int> discos;
      
      for (int i = 0; i < n; ++i) {
         int temp;
         std::cin >> temp;
      
         discos.insert(temp);
//std::cerr << "disco " << temp << '\n';
      }
      
      int cuenta = 0;
//std::cerr << "a la cuenta\n";
      while (!discos.empty( )) {
         int mayor = *std::prev(discos.end( ));
         int diferencia = c - mayor;
//std::cerr << "mayor: " << mayor << ", diferencia = " << diferencia << '\n';
         discos.erase(std::prev(discos.end( )));
         cuenta += 1;
         
         auto candidato = discos.lower_bound(diferencia);
         
         if (candidato == discos.end( ) && !discos.empty( )) {
            --candidato;
         }
         
         if (candidato != discos.end( )) {
            while (*candidato > diferencia) {
               if (candidato == discos.begin( )) {
                  goto siguiente;     
               }
               
               --candidato;
            }
            
//std::cerr << "encontrado pareja de " << *candidato << '\n';
            discos.erase(candidato);
         }
         
      siguiente:
         continue;
      }
//std::cerr << "fin a la cuenta\n";
      std::cout << "Case #" << ti + 1 << ": " << cuenta << '\n';
   }
}
