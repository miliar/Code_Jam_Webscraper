#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
      int n, ***arr,*r,*c;
      int flag=1;
      
      cin>>n;
      arr= new int** [n];
      r =new int[n];
      c= new int[n];
      //input
      for(int i=0;i<n;i++){
      
      cin>>r[i]>>c[i];
      arr[i]= new int* [r[i]];
       for(int j=0;j<r[i];j++)
        arr[i][j]= new int[c[i]];
      for(int j=0; j<r[i];j++)
        for(int k=0;k<c[i];k++)
           cin>>arr[i][j][k];
           
      }
      
      //output
      
      for(int i=0;i<n;i++)
            {
                 int max[r[i]];         
        for(int j=0;j<r[i];j++){
                max[j]= arr[i][j][0];
         for(int k=0;k<c[i];k++)
                      {
                           if(arr[i][j][k]>max[j])
                             max[j]=arr[i][j][k];          
                      }     
                 }
                 
              if(c[i]==1 || r[i]==1)
              flag=1;
              else{  
                 for(int j=0;j<r[i]&&flag==1;j++)
                   for(int k=0;k<c[i];k++)
                      if(arr[i][j][k]<max[j])
                       {
                                
                                for(int l=0;l<r[i];l++)
                                 if(arr[i][j][k]<arr[i][l][k]) 
                                 {
                                 flag=0;break;
                                 } 
                                                 
                       }
                       }
                       
                      if(flag==1)
                      cout<<"Case #"<<i+1<<": "<<"YES \n";
                      else
                      cout<<"Case #"<<i+1<<": "<<"NO \n";
                      
                      flag=1;
                 }
       getch();
       return 0;
    }
