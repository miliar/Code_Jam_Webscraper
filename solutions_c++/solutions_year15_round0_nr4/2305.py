#include <iostream>

int main(){
  int cases;
  std::cin >> cases;
  for(int _c = 0; _c < cases; _c++){
    int x, r, c;
    std::cin >> x >> r >> c;

    
    bool gana_richard = false;
 int en_diagonal = (x+1)/2;
 
    if(r < c && c < x) gana_richard = true; // hago un palito
    
    else if(r*c < x) gana_richard = true; //no entra la figura

    else if((r*c) % x != 0) gana_richard = true; //no van a entrar

    else if(en_diagonal > r || en_diagonal > c) gana_richard = true; // puedo poner las cosas en diagonal
    


    else if(x == 1){
      gana_richard = false;
    } else if(x == 2){
      gana_richard = false;
    } else if(x == 3){
      gana_richard = false;
    } else if(x == 4){
      if(c <= 2 || r <= 2) gana_richard =  true; //se puede elgir tal que pierda
      else gana_richard = false;
    }

    std::cout << "Case #" << _c+1 << ": " << (gana_richard? "RICHARD" : "GABRIEL") << std::endl;
  }
}


