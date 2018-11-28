#include <iostream>
#include <iomanip>
using namespace std;


int main()
{
    int ip_1;
     double c,f,x,prev=0,present=0,n=0,y=0,z=0,ans=0.0;
    
    cin>>ip_1;
    for(int i=0;i<ip_1;i++)
    {
        cin>>c>>f>>x;
       if(x<c)
        {
           ans=x/2.0;
           
           printf("Case #%d: %.7lf \n",i+1,ans);
            continue;
        }
        else{
            prev=0;
            present=0;y=0;z=0;n=0;
            
            while(true)
            {
            prev=c/(n*f+2)+prev;
            //cout<<"prev"<<prev<<endl;
            y=(x/((n+1)*f+2));
            present=c/((n+1)*f+2)+prev;
            z=(x/((n+2)*f+2));
             //cout<<"present"<<present<<endl;
             //cout<<"present+z"<<present+z<<endl;
             //cout<<"prev+y"<<prev+y<<endl;
            if((x/2)<prev+y)
            {
               printf("Case #%d: %.7lf \n",i+1,x/2);break; 
            }
            else if(prev+y<present+z)
            {
                
               // std::cout<<"Case #"<<i+1<<": "<<prev+y<<endl;
               printf("Case #%d: %.7lf \n",i+1,prev+y);
               break;
            }
                
            else
            {
                n++;
                
            }
            
            }
            
            
        }
        
    
        
        
        
    }
    
    
   
   return 0;
}

