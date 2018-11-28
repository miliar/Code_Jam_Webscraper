#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;

int pal(int num)
{
     int n, digit, rev = 0;
     
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
   //  cout << " The reverse of the number is: " << rev << endl;
     if (n == rev)
       return 1;
       //cout << " The number is a palindrome";
     else
       return 0;
       //cout << " The number is not a palindrome";
                  
       
}
int main()
{    
    int n, *arr, lb, ub;
    
    cin>>n;
    int m=2*n;
    arr = new int[m];
    for(int i=0;i<n;i++){
    
    cin>>lb>>ub;
    int p=2*i;
       arr[p]=lb;
       arr[p+1]=ub;
     }
     
     for(int i=0;i<n;i++)
     {
          int lb,ub,counter;
          int p=2*i;
          lb=arr[p];
          ub=arr[p+1];
          for(int j=lb;j<=ub;j++)
           {
                  if(j==1)
                   counter+=1;
                  if(pal(j)==1){
                         for(int k=1;k<=(j/2);k++)
                          if(j==(k*k) && pal(k)==1)       
                              counter+=1;
                    }
                  } 
                  cout<<"Case #"<<i+1<<": "<<counter<<"\n";
                  counter=0;
             }
             
             getch();
             return 0;
}    
