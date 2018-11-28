#include <iostream>

#include <cstring>

using namespace std;


int main()
 {

    int t,j=1;
 
   cin>>t;

    while(t--)
  
  {

        char a[120];
 
       cin>>a;
   
     int count=0;
    
    int x=strlen(a);
 
       
        for(int i=1;i<strlen(a);i++)
 
       {
            if(a[i]=='+' && a[i-1]=='-')

            count++;
            if(a[i]=='-' && a[i-1]=='+')
   
         count++;


        }
        if(a[x-1]=='-')
    
    count++;
      
  cout<<"Case #"<<j++<<": "<<count<<endl;
   
 }
	

return 0;

}
