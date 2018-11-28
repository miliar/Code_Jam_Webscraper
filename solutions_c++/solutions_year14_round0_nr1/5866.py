#include <iostream>

using namespace std;

int main()
{
   int t,f1,f2,aux;
   int c1=1;
   cin>>t;
   int m1[4][4];
   int m2[4][4];
   while(t--){
       cin>>f1;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>m1[i][j];
           }
       }
       cin>>f2;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>m2[i][j];
           }
       }
       int c=0;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               //cout<<c<<" holaaaaaaa"<<endl;
               //cout<<m1[f1-1][i]<<m2[f2-1][j]<<endl;
               if(m1[f1-1][i]==m2[f2-1][j]){
                   c++;
                   //out<<c<<" holaaaaaaa"<<endl;
                   aux=m1[f1-1][i];
               }
           }
       }
       cout<<"Case #"<<c1++<<": ";
       if(c>1){
           cout<<"Bad magician!"<<endl;
       }else if(c==1){
           cout<<aux<<endl;
       }else{
           cout<<"Volunteer cheated!"<<endl;
       }
   }
   
   return 0;
}

