
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void flipz(bool panz[], int j);
int flipNext(bool panz[], int j, int size);


int main(){
  int test, size;
  cin >> test;
  char cake;
  for(int i = 1; i <= test; i++){ 
    int count = 0;
    string pans;
    cin >> pans;
    size = pans.length();
    bool panz[size];
    for(int j = 0; j < size; j++){
      cake = pans[j];
      if(cake == '+')
        panz[j] = true;
      else
        panz[j] = false;
    }
    for(int j = 0; j < size; ){
      j = flipNext(panz, j, size);
      if(j >= -1)
        count++;
      else
        break;
    }
     cout << "Case #" << i << ": " << count << endl;
  }
}


void flipz(bool panz[], int j){
  for(int i = 0; i <= j; i++){
    if(panz[i])
      panz[i] = false;
    else
      panz[i] = true;
  }
}

int flipNext(bool panz[], int j, int size){
  for(int i = 0; i < size; i++){
    if(!panz[i])
      break;
    if(i == size - 1 && panz[i])
      return -2;
  }
  int i = j;
  while(i < size && (panz[i] == panz[j]))
    i++;
  if(i > size){
    if(!panz[0]){
      flipz(panz, i - 1);
      return -1;
    }
    else
      return -2;
  }
  else
    flipz(panz, i - 1);
  for(int n = 0; n < size; n++){
    if(!panz[n])
      return i;      
  }
}


/*
    for(int j = 0; j < size; j++){
      if(panz[j])
        cout << "+";
      else
        cout << "-";
     }
*/
