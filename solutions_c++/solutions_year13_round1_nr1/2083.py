#include <iostream>

using namespace std;
int ra, total, aux;

int calcular(int rp, int tp, int c){
 int cont = 1;
 ra = rp;
 aux = ra+1;
 ra = ((ra + 1)*(ra + 1)) - ((ra)*(ra));
 tp = tp- ra;
//cout << "el tp es : " << tp << " el ra es: " << ra << " el aux" << aux <<  endl;
 while( tp >= 0){
       ra = ((aux + 2)*(aux + 2)) - ((aux+1)*(aux+1));
       tp = tp - ra; 
       aux = aux + 2;
  //cout << "el tp es : " << tp << " el ra es: " << ra << endl; 
      cont ++;    
    }

 cont --;
 cout << "Case #" << c <<": "<< cont <<endl;
 return 0;
    
}


int main(){
    int cases;
    cin >> cases;
    for(int i=1; i<=cases; i++){
     int r, t;
     cin >> r >> t;
     calcular(r,t,i);     
    }
    
    
    return 0;
}
