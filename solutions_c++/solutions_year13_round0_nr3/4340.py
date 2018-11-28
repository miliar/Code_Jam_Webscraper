#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <fstream>

#define S scanf
#define P printf 
using namespace std;
int main()
{
    long long int a[40]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000000};
    long long int b, c;
    int y,i,p,t,n;
    
    ifstream ifile("C:/New folder/ip.txt");
    ofstream ofile("C:/New folder/out.txt");
    
    ifile >>n;
    y=n;
   // P("%lld\n",a[5]);
   while(n>0){
    ifile >> b >> c;
    
    for(i=0;i<39;i++){
                      if(a[i+1]*a[i+1]>=b && a[i]*a[i]<b)//remember b=1
                      t=i+1;
                      else if(a[i]*a[i]==b)
                      t=i;
                      
                      if(a[i+1]*a[i+1]>=c && a[i]*a[i]<c)
                      p=i+1;
                      else if(a[i]*a[i]==c)
                      p=i+1;
                    //  else if(a[i]==c)
                    //  p=i+1;
                      
                      }
                     // for(i=t+1;i<=p;i++){
                                           ofile<<"Case #"<<y-n+1<<": "<<p-t<<endl;
                       //                    }
              n--;
              }        
    getch();
    return 0;
    
}
