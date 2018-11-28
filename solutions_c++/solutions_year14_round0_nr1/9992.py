#include <iostream>
#include<algorithm>

using namespace std;

int main()
{
   int test;
   cin>>test;
   int q=1;
   while(test--){
       int a,b;
       int mat[4][4];
       cin>>a;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>mat[i][j];
           }
       }
       cin>>b;
       int  mat2[4][4];
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               cin>>mat2[i][j];
           }
       }
       
       int ref[8];
       for(int i=0;i<4;i++){
           ref[i]=mat[a-1][i];
       }
       
       for(int i=0;i<4;i++){
           ref[i+4]=mat2[b-1][i];
       }
       
       sort(ref,ref+8);
       
       int counter=0;
       int value;
       for(int i=0;i<7;i++){
           if(ref[i]==ref[i+1]){
               counter++;
               value=ref[i];
           }
           
       }
       cout<<"Case #"<<q<<": ";
       
       
       
       if(counter==1){
           cout<<value;
       }
       
       if(counter==0){
           cout<<"Volunteer cheated!";
       }
       
       if(counter>1){
           cout<<"Bad magician!";
       }
        cout<<endl;
        q++;
    }
    
}
