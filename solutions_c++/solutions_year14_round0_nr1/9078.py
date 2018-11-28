#include <iostream>

using namespace std;

int valores[4]; //lista de posibles

bool find(int a){
           for (int i=0;i<4;i++){
               if(valores[i]==a)
               return true;
           }
           return false;
       }

int main()
{
   int ciclo;
   int vc=0; //contador de posibles
   int selected;
   int dump;  //entrada de matriz
   int status=0; //tipo de respuesta
   cin>>ciclo;
   for(int i=0;i<ciclo;i++){
       //start values
       vc=0;
       status=0;
       selected=0;
       int select;
       //get selected row
       cin>>select;
       // cout<<select;
       
       for (int a=1;a<=4;a++){
           for (int b=0;b<4;b++){
               cin>>dump;
               if(a==select){
                 valores[vc]=dump;  
                 vc++;
               }
           }
       }
       //reset start values
       vc=0;
    
       //segundo set
       //get selected row
       cin>>select;
       // cout<<select;
       
       for (int a=1;a<=4;a++){
           for (int b=0;b<4;b++){
               cin>>dump;
               
               if(a==select && find(dump) ){
                 status++;
                 selected=dump;
               }
           }
           
       }
       
      switch(status){
          case 1:
            cout<<"Case #"<<i+1<<": "<<selected<<endl;
            break;
          case 0:
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
            break;
          default:
            cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
      }
       
   }
   
   return 0;
}

 
