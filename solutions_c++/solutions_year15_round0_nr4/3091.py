#include <iostream>
using namespace std;

int main (){
   string g = "GABRIEL";
   string richard = "RICHARD";
   int T;
   cin>>T;
   for (int caseN=1;caseN<=T;caseN++){
      int x,rnum,c;
      string winner;
      cin>>x>>rnum>>c;
      switch(x){
      case 1:
         winner = g;
         break;
      case 2:
         if (rnum*c % 2 == 0){
            winner = g;
         }
         else{
            winner = richard;
         }
         break;
      case 3:
         if (rnum*c % 3 == 0 && c!= 1 && rnum != 1){
            winner = g;
         }
         else{
            winner = richard;
         }
         break;
      case 4:
         if ((c == 4 || rnum == 4) && c>=3 && rnum>=3 ){
            winner = g;
         }
         else {
            winner = richard;
         }
         break;
      }
      
      
      cout<<"Case #"<<caseN<<": "<<winner<<endl;

   }
   
}
