#include<iostream>
#include<vector>
using namespace std; 
 
 
  
int main()
{
    freopen("B-large.in","r",stdin);
   freopen("mins.txt","w",stdout);
    int TT;
    cin>>TT;
   double currentRate  ;
  double currentCookies  ;
  
    for(int T=1;T<=TT;T++)
    {
      
       
       currentRate = 2;
       currentCookies = 0;
         double C,F,X;
     cin>>C>>F>>X;
      
   // cout<<"X"<<C<<" "<<F<<" "<<X<<endl;
               
  double totalTime = 0;
      while(currentCookies<X)
       {
           double timeToBuyF = (C - currentCookies)/currentRate;
           double timeToTargetAfterBuyF = (X)/(currentRate + F);
           double timeToTarget = (X - currentCookies)/currentRate;
           // cout<<"time "<<timeToBuyF<<" "<<timeToTargetAfterBuyF<<" "<<timeToTarget<<endl;
        //    system("pause");
      //    cout<<currentRate<<endl;
           if(timeToBuyF + timeToTargetAfterBuyF>timeToTarget)
           {
                       //  cout<<"Dont"<<endl;
                 
                       totalTime += timeToTarget;
                       currentCookies = X;
           }else
           {
              //  cout<<"buy"<<endl;
                totalTime += timeToBuyF;
                currentRate += F;
                currentCookies = 0; 
           }
       } 
       //out<<"Case #"<<T<<": "; 
    //   cout<<totalTime<<endl;  
     printf ("Case #%d: %.7f \n",T, totalTime);
    
    }
} 
