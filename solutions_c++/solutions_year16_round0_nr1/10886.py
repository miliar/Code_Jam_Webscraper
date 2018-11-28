#include <iostream>
#include <vector>
using namespace std;

vector<int> lista;
int size;

void list(int res){
  int b=1;
  int a=size;
  int i=0;
  if(a>0){
    while(i<a){
      if(res==lista[i])
	b=0,i++;
      else
	i++;
    }
    if(b>0){
      lista.push_back(res);
      size++;
    }
  }else{
    lista.push_back(res);
    size++;
  }
}


void dividir(int val){
  while (val>0){
    intresto=val%10;
    val=val/10;
    list(resto);
  }
}




void comprobar(int valor){
  size=0;
  int i=1;
  int valor2=valor;
  int tam=lista.size();
  while(tam<10){
    valor=valor2*i;
    if(valor!=0){
      dividir(valor);
      i++;
      tam=lista.size();
    }
    else{
      tam=10;
    }
  }
  if(valor!=0)
    cout << valor << endl;
  else
    cout << "INSOMNIA" << endl;
}

void casos(int a){
  int leer;
  for(int i=0;i<a;i++){
    lista.clear();
    cin >> leer;
    cout << "Case #" << (i+1) << ": ";
    comprobar(leer);
  }
}

int main() {
  int a;
  cin >> a;
  casos(a);
  return 0;
}
