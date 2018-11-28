#include<iostream>
#include <string>
#include <sstream>
#include <math.h>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std;

int main()
{
    READ("C-small-attempt0.in");
    WRITE("C-small-attempt0.out");
    
    int t;
    cin>>t;
    for(int i = 0; i<t; i++)
    {
      int A,B;
       int count = 0;
      cin>>A;
      cin>>B;
      int n1 = A;
      while(n1<=B)
      {
      
      bool isPal = false, isSquare = false, RootPal = false;
      string s="",s2="",s3="",s4="";
      stringstream ss;
      ss<<n1;
      ss>>s;
      for(int i = s.size()-1; i>=0; i--)
      {
        s2 = s2+ s[i];
      }
      
       if(s==s2)
      {
      isPal = true;
      
      double d_sqrt = sqrt(n1);
      int i_sqrt = d_sqrt;
      if ( d_sqrt == i_sqrt)
      {
      isSquare = true;
      
      stringstream ss2;
      ss2<<i_sqrt;
      ss2>>s3;
      
       for(int i = s3.size()-1; i>=0; i--)
      {
        s4 = s4+ s3[i];
      }
      if(s4==s3)
      RootPal = true;
       
      }
      
      }
    
    if(RootPal ==true && isSquare == true && isPal == true)
    count++;
    
            n1++;
}
cout<<"Case #"<<i+1<<": "<<count<<endl;

    }
 
 
 return 0;   
}
