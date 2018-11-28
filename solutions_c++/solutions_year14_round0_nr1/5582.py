#include <iostream>

using namespace std;

int main()
{
   int n;
   int a1[4][4],a2[4];
   int row;
   int i,j;
   cin>>n;
   int temp=1;
   while(n>0){
       cin>>row;
       row--;
       for(i=0;i<4;i++){
           for(j=0;j<4;j++){
               cin>>a1[i][j];
           }
       }
       
       for(i=0;i<4;i++)
        a2[i] = a1[row][i];
       
       cin>>row;
       row--;
       for(i=0;i<4;i++){
           for(j=0;j<4;j++){
               cin>>a1[i][j];
           }
       }
       int count=0;
       int pos;
       for(i=0;i<4;i++){
           for(j=0;j<4;j++){
               if(a1[row][i] == a2[j]){
                   count++;
                   pos = j;
               }
           }
       }
       
       if(count==0){
            cout<<"Case #"<<temp<<": Volunteer cheated!"<<endl;
       }else if(count==1){
           cout<<"Case #"<<temp<<": "<<a2[pos]<<endl;
       }else{
          
           cout<<"Case #"<<temp<<": Bad magician!"<<endl;
       }
       temp++;
       n--;
   }
   
   
   return 0;
}
