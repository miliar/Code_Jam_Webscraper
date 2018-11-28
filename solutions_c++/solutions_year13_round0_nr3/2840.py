#include<cstdlib>
#include <cmath>
#include <iostream>
using namespace std;
 bool check(int l)
 {
      int ind=0;
      int arr[50];
      while(l>0)
      {
           arr[ind++]=l%10;
           l/=10;     
      }
      for(int i=0; i< ind/2; i++)
     {
             if(arr[i]!=arr[ind-1-i])
                return false;
     }
     return true;
 }
 
int main()
{
    int T;
    cin>>T;
    for(int k=0; k< T; k++)
    {
         int A, B;
         cin>> A;
         cin >> B;
         int cnt=0;
         for(int i=A; i<= B; i++)
         {
                 if(check(i))
                 {
                        double d=sqrt(i);
                        int m=d;
                        if(d>m)
                            continue;     
                        if(check((int)d))
                            cnt++;     
                 }
         }
         char sol[40]={0};
         sprintf(sol,"Case #%d: %d", k+1, cnt);
         cout<<sol<<endl;
    }
    
}
