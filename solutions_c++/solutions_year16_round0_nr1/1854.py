#include <iostream>
#include <cstring>
#include <cassert>

using namespace std;

bool have[10];
int cont = 0;

void mark(int n){
  while(n){
    int aux = n % 10;
    n /= 10;
    
    if(!have[aux]){
      have[aux] = true;
      ++cont;
    }
  }
}

int search(int n){
  int aux = 0,it = 0;
  cont = 0;
  memset(have,false,sizeof have);
  
  while(cont < 10){
    aux += n;
    mark(aux);
    ++it;
  }
  
  assert(it <= 100);
  
  return aux;
}

int main(){
  int T,N;
  
  /*for(int tc = 1;tc <= 1000000;++tc){
    search(tc);
  }*/
  
  cin >> T;
  
  for(int tc = 1;tc <= T;++tc){
    cin >> N;
    cout << "Case #" << tc << ": ";
    
    if(N == 0) cout << "INSOMNIA\n";
    else cout << search(N) << "\n";
  }
  
  return 0;
}
