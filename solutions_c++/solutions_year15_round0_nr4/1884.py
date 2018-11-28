#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            int x,r,c;
            cin>>x>>r>>c;
          // cout<<x<<" "<<r<<" "<<c<<" ";
    cout<<"Case #"<<i<<": ";
            if(x>r&&x>c)
            {
                 cout<<"RICHARD\n"; 
                 continue;      
            }
            int half=x/2;
            if(2*half==x)
            {
                         if(half>r||half>c)
                         {
                                cout<<"RICHARD\n"; 
                                continue;               
                         }
            }
            else
            {
             if(r>c)   
             {
                       if((half+1)>r||half>c)
                       {
                  cout<<"RICHARD\n"; 
                                continue; 
                       }                                              
             }
             else
             {
                 if((half+1)>c||(half)>r)
                       {
                  cout<<"RICHARD\n"; 
                                continue; 
                       }  
             }
            }
            if(((r*c)/((float)x)-(r*c)/x)!=0)
            {
                 cout<<"RICHARD\n"; 
                                continue;                    
            }
          if(r==2||c==2)
            {
                          if(x==4)
                          {
                                   cout<<"RICHARD\n"; 
                                continue; 
                          }
            } 
            if(r==1||c==1)
            {
                          if(x>2)
                          {
                              cout<<"RICHARD\n"; 
                                continue;     
                          }
            }
            cout<<"GABRIEL\n";
    }
}
