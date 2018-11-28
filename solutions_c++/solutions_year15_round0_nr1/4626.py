#include <iostream> 
#include <vector>

template <typename T>
void print (std::vector<T> a){
  for (int i = 0; i<a.size(); i++){
    std::cout << (int) a[i] << " ";
  }
  std::cout << std::endl;
}


int main(){
  int casos = 0;
  std::cin >> casos;
  for(int i = 0; i<casos; i++){
    int s_max = 0;
    std::cin >> s_max;


    int agregados = 0;
    int suma_anteriores  = 0;

    for(int j = 0; j<= s_max; j++){
      char k; std::cin >> k;
      int a = ((int) k)-48;
      if (j > suma_anteriores  + agregados){
        agregados += j - (suma_anteriores+agregados);
        //std::cout << "(j=" << j << ";agr="<<j-suma_anteriores<< ") ";
      }
      suma_anteriores+= a;
    }
  std::cout << "Case #" << i+1 << ": "<< agregados << std::endl;

  }
  
}
