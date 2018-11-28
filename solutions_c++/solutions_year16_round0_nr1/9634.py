#include <iostream>

using namespace std;
bool number[10];


int main(){
  int t,n,actual,i,cont,cas = 0;
  cin >> t;
  
  while(t--){
   
    
    for(int j = 0 ; j < 10; ++j){
      number[j] = false;
    }

    
    cin >> n;
    cas++;
    
    if(n == 0){
      cout << "Case #" << cas << ": " << "INSOMNIA"<< endl;
      continue;
    }
    
    i = 1;
    cont = 0;
    while(cont < 10){
      actual = i * n;
      int temp1 = actual;
      while(temp1 > 0){
	if(!number[temp1%10]){
	  //cout << temp1%10 << endl;
	  number[temp1%10] = true;
	  cont++;
	  if(cont == 10) break;
	}
	 temp1 /= 10;
      }
     i++;
    }
     cout << "Case #" << cas << ": " << actual << endl;
  }
 
}
  

