#include<iostream>
#include<iomanip>
//#include <conio.h>

using namespace std;

int main()
{
    int T;
    double C, F, X;
    double S, D; //S is current speed, D is current cookie count
    double time;
    int testCasesCount = 1;
    
    cin>>T;
    while (T-- > 0)
    {
          
          cin>>C>>F>>X;
          
          S = 2.0;
          D = 0.0;
          time = 0.0;
          
          while (D != X)
          {
             if((C < X ) && ((X/S) > ((C/S) + (X/(S+F)))))
             {
                //Buy a farm
                D = 0;
                time = time + (C/S);
                S = S + F;
             } 
             else
             {
                time = time + ((X-D)/S);              //buy farm
                D = X;  
             }
          }          
          
          
          cout<<"Case #"<<testCasesCount++<<": "<<setprecision(7)<<fixed<<time;
          
          if(T!= 0)
          cout<<endl;
    }
    
    
    
    
//    getch();
    return 0;
}
