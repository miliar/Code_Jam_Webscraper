#include <iostream>
#include<fstream>

using namespace std;

int main(int argc, char *argv[])
{
     int  n,i,j,x,o,t;
 int space=0;
 int xr;
 int oro;
 int trow;
 char arr[4][4];
    ifstream infile; ofstream outfile; outfile.open("output.txt");
    infile.open("A-large.in");
    
           infile>>n;             
 int z=1;
 
 while(z<=n)
 {
for(i=0;i<4;i++)
{
                for(j=0;j<4;j++)
                {
                                infile>>arr[i][j];
                                }
                                }
                                for(i=0;i<4;i++)
                                { x=o=t=xr=oro=trow=0;
                                                for(j=0;j<4;j++)
                                                {
                                                                if(arr[i][j]=='X')
                                                                x++;
                                                                if(arr[i][j]=='O')
                                                                o++;
                                                                if(arr[i][j]=='T')
                                                                t++;
                                                                if(arr[i][j]=='.')
                                                                space++;
                                                                if(arr[j][i]=='X')
                                                                xr++;
                                                                if(arr[j][i]=='O')
                                                                oro++;
                                                                if(arr[j][i]=='T')
                                                                trow++;
                                                                }
                 if((x+t==4) || (xr+trow==4))
    {
              outfile<<"Case "<<"#"<<z<<": "<<"X won\n";
              goto next;
              }         
              if((o+t==4)||(oro+trow==4))
              {outfile<<"Case "<<"#"<<z<<": "<<"O won\n";
              goto next;
                        }     
                        }
                        
                        
                        xr=trow=oro=0; j=3;x=o=t=0;
                        
                        //DIAGONAL CHECK
                        for(i=0;i<4;i++)
                        {
                        if(arr[i][i]=='X')
                                                                xr++;
                                                                if(arr[i][i]=='O')
                                                                oro++;
                                                                if(arr[i][i]=='T')
                                                                trow++;
              
                                                         if(arr[i][j]=='X')
                                                         x++;
                                                         if(arr[i][j]=='O')
                                                         o++;
                                                         if(arr[i][j]=='T')
                                                         t++;
                                                        
                                                         j--;
                                                         
                                                         }
              
                                                         if(x+t==4)
                                                       {
              outfile<<"Case "<<"#"<<z<<": "<<"X won\n";
              goto next;
              }         
              if(xr+trow==4)
               {
              outfile<<"Case "<<"#"<<z<<": "<<"X won\n";
              goto next;
              }         
              
              if(o+t==4)
              {
              outfile<<"Case "<<"#"<<z<<": "<<"O won\n";
              goto next;
              } 
              if(oro+trow==4)         
                 {
              outfile<<"Case "<<"#"<<z<<": "<<"O won\n";
              goto next;
              } 
              
           if(space>0)
              {
                         outfile<<"Case #"<<z<<": Game has not completed\n";
                         goto next;
                         }
                         else
                         { outfile<<"Case #"<<z<<": Draw\n";   goto next;}
                            
                                                      
    
  next:
       z++; 
       space=0; 
    
    
    
}  

    
    infile.close();
    outfile.close();
    
    
    
    return 1;
    
  
}
