#include <iostream.h>
#include<fstream.h>
#include<conio.h>
using namespace std;

int main()
{
     int  n,i,j,x,o,t;
     int s=0,k,r,z,y;
     char a[4][4];
     ifstream iff;
     ofstream off;
     iff.open("A-large.in");
     off.open("soln5.in");
    
             iff>>n;             
             z=1;
 
      while(z<=n)
      {
       for(i=0;i<4;i++)
       {
                for(j=0;j<4;j++)
                {
                                iff>>a[i][j];
                }
       }
                for(i=0;i<4;i++)
                { 
						x=o=t=k=r=y=0;
                        for(j=0;j<4;j++)
                        {         
                               if(a[i][j]=='T')
                                   t++;
                               if(a[i][j]=='.')
                                   s++;
                               if(a[i][j]=='X')
                                   x++;
                               if(a[i][j]=='O')
                                   o++;
                               if(a[j][i]=='X')
                                   k++;
                               if(a[j][i]=='O')
                                   r++;
                               if(a[j][i]=='T')
                                   y++;
                             }
              if((x+t==4)||(k+y==4))
			  {
                off<<"Case "<<"#"<<z<<": "<<"X won\n";
                goto next;
              }         
              if((o+t==4)||(r+y==4))
              {
                off<<"Case "<<"#"<<z<<": "<<"O won\n";
                goto next;
               }    
               }
                   k=y=r=0;
                   j=3;
                   x=o=t=0;
                  
               for(i=0;i<4;i++)
               {
                  if(a[i][i]=='X')
                   k++;
                  if(a[i][i]=='O')
                   r++;
                  if(a[i][i]=='T')
                   y++;

                  if(a[i][j]=='X')
                    x++;
                  if(a[i][j]=='O')
                    o++;
                  if(a[i][j]=='T')
                    t++;
                    j--;                     
                }                                                             
                       if(x+t==4)
                       {
                            off<<"Case "<<"#"<<z<<": "<<"X won\n";
                            goto next;
                        }         
                       if(k+y==4)
                        {
                          off<<"Case "<<"#"<<z<<": "<<"X won\n";
                          goto next;
                         }         
              
                       if(o+t==4)
                        {
                         off<<"Case "<<"#"<<z<<": "<<"O won\n";
                         goto next;
                        } 
                       if(r+y==4)         
                        {
                          off<<"Case "<<"#"<<z<<": "<<"O won\n";
                          goto next;
                        } 
              
                       if(s>0)
                       {
                         off<<"Case #"<<z<<": Game has not completed\n";
                         goto next;
                        }
                         else
                         {
                              off<<"Case #"<<z<<": Draw\n";   
                              goto next;
                        }
         
  next:
       z++; 
       s=0; 
   
}  
    iff.close();
    off.close();
  
    getch();
    return 0;

}
