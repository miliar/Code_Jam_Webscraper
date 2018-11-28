#include <iostream>

using namespace std;

int main()
{
   int t,f1,f2,num;
   int c1=1;
   cin>>t;
   int N[4][4];
   int M[4][4];
   while(t--){
       cin>>f1;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>N[i][j];
           }
       }
       cin>>f2;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>M[i][j];
           }
       }
       int cont=0;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               if(N[f1-1][i]==M[f2-1][j]){
                   cont++;
                   num=N[f1-1][i];
               }
           }
       }
       cout<<"Case #"<<c1<<": ";
       if(cont>1){
           cout<<"Bad magician!"<<endl;
       }else{
           if(cont==1){
               cout<<num<<endl;
           }else{
               cout<<"Volunteer cheated!"<<endl;
           }
       }
       c1++;
   }
   
   return 0;
}

