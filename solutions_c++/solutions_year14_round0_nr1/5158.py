#include<iostream>
using  namespace std;
int main(){
int tcase;
cin>>tcase;
for(int k=0;k<tcase;k++){
int a[4][4];
int b[4][4];
int c[4];
int ans1;
cin>>ans1;
for(int i=0;i<4;i++)
   for(int j=0;j<4;j++)
       cin>>a[i][j];/*
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++)
              cout<<a[i][j]<<" ";
              cout<<endl;
              }*/
              /*
              for(i=0;i<4;i++)
                 b[i]=a[ans1][i];
                 */
       int ans2;
              cin>>ans2;
        for(int i=0;i<4;i++)
         for(int j=0;j<4;j++)
       cin>>b[i][j];
       /*
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++)
              cout<<b[i][j]<<" ";
              cout<<endl;
              }*/
/*
               for(i=0;i<4;i++)
                 c[i]=a[ans2][i];*/
                 int l=0;
                 int num;

                 for(int i=0;i<4;i++)
                 {
                 for(int j=0;j<4;j++){

                 if(a[ans1-1][i]==b[ans2-1][j]){
                   l++;
                   num=a[ans1-1][i];
                   break;
                   }
                   }
                   if(l==2)
                   break;
                   }

                   cout<<"case #"<<k+1<<":"<<" ";
                     if(l>1)
                     cout<<"Bad magician!"<<endl;


                     else if(l)
                     cout<<num<<endl;

                   else
                   cout<<"Volunteer cheated!"<<endl;
                   }




}
