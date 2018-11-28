#include <iostream>
#include<fstream>
using namespace std;
int main()
{
     int  n,i,j,x,o,t;
 int mark=0;
 int rr;
 int ww;
 int wan;
 char arr[4][4];
    ifstream infile; ofstream outfile; outfile.open("output.txt");
    infile.open("input.in");
    
           infile>>n;             
 int wq=1;
 
 while(wq<=n)
 {
for(i=0;i<4;i++)
{
                for(j=0;j<4;j++)
                {
                                infile>>arr[i][j];
                }
}
                for(i=0;i<4;i++)
                { 
							x=o=t=rr=ww=wan=0;
                              for(j=0;j<4;j++)
                             {
                                     if(arr[i][j]=='X')
											x++;
                                     if(arr[i][j]=='O')
                                            o++;
                                     if(arr[i][j]=='T')
                                            t++;
                                     if(arr[i][j]=='.')
                                            mark++;
                                     if(arr[j][i]=='X')
                                            rr++;
                                     if(arr[j][i]=='O')
                                            ww++;
                                     if(arr[j][i]=='T')
                                            wan++;
                             }
                 if((x+t==4) || (rr+wan==4))
			  {
              outfile<<"Case "<<"#"<<wq<<": "<<"X won\n";
              goto next;
              }         
              if((o+t==4)||(ww+wan==4))
              {outfile<<"Case "<<"#"<<wq<<": "<<"O won\n";
              goto next;
                        }     
                        }
                        
                        
                        rr=wan=ww=0; j=3;x=o=t=0;
                        
                        //DIAGONAL CHECK
                        for(i=0;i<4;i++)
                        {
                                                         if(arr[i][i]=='X')
                                                         rr++;
                                                         if(arr[i][i]=='O')
                                                         ww++;
                                                         if(arr[i][i]=='T')
                                                         wan++;
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
              outfile<<"Case "<<"#"<<wq<<": "<<"X won\n";
              goto next;
              }         
              if(rr+wan==4)
               {
              outfile<<"Case "<<"#"<<wq<<": "<<"X won\n";
              goto next;
              }         
              
              if(o+t==4)
              {
              outfile<<"Case "<<"#"<<wq<<": "<<"O won\n";
              goto next;
              } 
              if(ww+wan==4)         
                 {
              outfile<<"Case "<<"#"<<wq<<": "<<"O won\n";
              goto next;
              } 
              
           if(mark>0)
              {
                         outfile<<"Case #"<<wq<<": Game has not completed\n";
                         goto next;
                         }
                         else
                         { outfile<<"Case #"<<wq<<": Draw\n";   goto next;}
                            
                                                      
    
  next:
       wq++; 
       mark=0; 
    
    
    
}  

    
    infile.close();
    outfile.close();
    
    
    
    return 1;
    
  
}
