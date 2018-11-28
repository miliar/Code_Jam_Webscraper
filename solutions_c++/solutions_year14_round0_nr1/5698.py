#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
    
    freopen ("googlecodejamfirstoutput.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++){
               int arr[4][4],arr1[4][4],i,j,k,l,m,an1,an2;
               cin>>an1;
               for(i=0;i<4;i++)
               for(j=0;j<4;j++)
               cin>>arr[i][j];
               cin>>an2;
               for(i=0;i<4;i++)
               for(j=0;j<4;j++)
               cin>>arr1[i][j];
               int count =0;
               an1--;
               an2--;
               for(i=0;i<4;i++)
               for(j=0;j<4;j++){
               //cout<<"compare"<<arr[an1][i]<<"--"<<arr1[an2][j]<<endl;
               if(arr[an1][i]==arr1[an2][j])
               {count++;
               m=arr[an1][i];
               }}
               cout<<"Case #"<<z<<": ";
               if(count>1)
               cout<<"Bad magician!"<<endl;
               if(count==1)
               cout<<m<<endl;
               if(count==0)
               cout<<"Volunteer cheated!"<<endl;
               }
               cin.get();
               cin.get();
    }
