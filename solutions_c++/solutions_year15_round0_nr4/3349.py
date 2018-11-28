#include <iostream>
using namespace std ;

int main()
{

	int t , x, r, c ;
	cin>>t; 
	for(int i = 0 ; i < t ; i++)
	{
      cin>>x>>r>>c ;
      if(x==1) {
      	 cout<<"Case #"<<i+1<<": GABRIEL"<<endl;      
      }
      else 
      	if(x==2) {
         if((r%2==0)||(c%2==0)) 
         	cout<<"Case #"<<i+1<<": GABRIEL"<<endl; 
         else
            cout<<"Case #"<<i+1<<": RICHARD"<<endl; 
        }
        else
        	if(x==3) {
        		if((r==3)||(c==3)) {
        	      if(r==1||c==1)
                      cout<<"Case #"<<i+1<<": RICHARD"<<endl;  
                else    
                     cout<<"Case #"<<i+1<<": GABRIEL"<<endl; 
        	  }
            else
        	      cout<<"Case #"<<i+1<<": RICHARD"<<endl;  		
        	  
          }
        	else
        		if(x==4) {
        			if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
	                 cout<<"Case #"<<i+1<<": GABRIEL"<<endl; 
	                else 
        	         cout<<"Case #"<<i+1<<": RICHARD"<<endl;  	
        		}

	}
return 0 ;
}