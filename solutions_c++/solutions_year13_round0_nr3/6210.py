# include <iostream.h>
# include <math.h>
# include <conio.h>
# include <fstream.h>

using namespace std;
int main()
{         int a,b,c,z,x,e,p,l,t,y,i,h,no;
          float s,j;
    ifstream iff;
    ofstream off;
    iff.open("C-small-attempt0.in");
    off.open("adi2.in");
    iff>>a;
  
    for(i=0;i<a;i++)
    {
                    no=0;
           iff>>b>>c;
          
           for(z=b;z<=c;z++)
           {
                         x=z;
                         e=0;
                         while(x>0)
                         {
                                   x=x/10;
                                   e++;
                         } 
                         x=z;
                         s=0;
                         while(x>0)
                         {
                                   p=x%10;
                                   s=s+p*(pow(10,e-1));
                                   x=x/10;
                                   e--;
                         }   
                        
                         if(s==z)
                         {
                                 l=sqrt(s);
                             
                                 if(s==l*l)
                                 {
                                          
                                           t=l;
                                           y=0;
                                           while(t>0)
                                           {
                                                     t=t/10;
                                                     y++;
                                           } 
                                          
                                           t=l;
                                       
                                           j=0;
                                           while(t>0)
                                           {
                                                     h=t%10;
                                                  
                                                     j=j+h*(pow(10,y-1));
                                                     t=t/10;
                                                     y--;
                                           } 
                                           
                                           if(j==l)
                                           {no++;
                                        
                                         
                                           }
                                 } 
                         } 
                               
                         }   
                          off<<"Case #"<<i+1<<":"<<" "<<no<<endl; 
           }    
                 
    
          iff.close();
          off.close();
           getch();
           return 0;
           
} 

