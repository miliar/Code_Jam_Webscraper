#include <fstream>
#include<iostream>
using namespace std;
int main () {
  char a[100][100];
  int n,index,i,j,xf=0,yf=0,dotf=0,x=0,y=0,dot=0;
  fstream fin,fout;
  fout.open("fout.txt",ios::out);
  fin.open ("A-large.in",ios::in);
   fin>>n;
   for(index=0;index<n;index++)
   {      
           x=y=dot=xf=yf=dotf=0;
         
	 for(i=0;i<4;i++)
          {
            for(j=0;j<4;j++)
             {
		fin>>a[i][j];
               
             }
          }
           for(i=0;i<4;i++)
          { x=y=dot=0;
            for(j=0;j<4;j++)
             {   
		if(a[i][j]=='X')
                {x++;}
	        else
	        if(a[i][j]=='O')
		y++;
		else
	        if(a[i][j]=='.')
		dot++;
                 
             }
                    if(x+y+dot==4)
                   {
	              if(x==4)
                      {xf=1;break;}  
                      if(y==4)
		      {yf=1;break;} 
		      if(dot>0)
		      dotf=1;
                   }
                   if(x+y+dot==3)
		   {  
                      if(x==3)
                      {xf=1;break;}  
                      if(y==3)
		      {yf=1;break;} 
		      if(dot>0)
		      dotf=1;
			
		   }
           }
            
                if(xf!=1||yf!=1)
		{   
                   
                    for(j=0;j<4;j++)
                     { x=y=dot=0;
                       for(i=0;i<4;i++)
                         {
				if(a[i][j]=='X')
                                 x++;
	                         else
	                         if(a[i][j]=='O')
  				 y++;
				 else
	        		 if(a[i][j]=='.')
				 dot++;
                		   
		         }
                                 if(x+y+dot==4)
                	           {
	        		      if(x==4)
                		      {xf=1;break;}  
                		      if(y==4)
				      {yf=1;break;} 
				      if(dot>0)
				      dotf=1;
                		   }
				      if(x+y+dot==3)
		                      {
                                        if(x==3)
                                        {xf=1;break;}  
                                        if(y==3)
		                        {yf=1;break;} 
		                        if(dot>0)
		                        dotf=1;
		                       }
		     }
                     
                }
                if(xf!=1||yf!=1)
                {x=y=dot=0;
                  for(i=0;i<4;i++)
                     {
		               if(a[i][i]=='X')
                                 x++;
	                         else
	                         if(a[i][i]=='O')
  				 y++;
				 else
	        		 if(a[i][i]=='.')
				 dot++;
                     }      
                            if(x+y+dot==4)
                	           {
	        		      if(x==4)
                		      {xf=1;}  
                		      if(y==4)
				      {yf=1;} 
				      if(dot>0)
				      dotf=1;
                		   }
				      if(x+y+dot==3)
		                      {
                                        if(x==3)
                                        {xf=1;}  
                                        if(y==3)
		                        {yf=1;} 
		                        if(dot>0)
		                        dotf=1;
		                       }
		}
                if(xf!=1||yf!=1)
                {     j=3;x=y=dot=0;
                      for(i=3;i>=0;i--)
		       {
			       if(a[i][j-i]=='X')
                                 x++;
	                         else
	                         if(a[i][j-i]=='O')
  				 y++;
				 else
	        		 if(a[i][j-i]=='.')
				 dot++; 
			}
                              if(x+y+dot==4)
                	           {
	        		      if(x==4)
                		      {xf=1;}  
                		      if(y==4)
				      {yf=1;} 
				      if(dot>0)
				      dotf=1;
                		   }
				      if(x+y+dot==3)
		                      {
                                        if(x==3)
                                        {xf=1;}  
                                        if(y==3)
		                        {yf=1;} 
		                        if(dot>0)
		                        dotf=1;
		                       }
                }
          if(yf==1)
           {fout<<"Case #"<<index+1<<": O won\n";}
          else
          if(xf==1)
          {fout<<"Case #"<<index+1<<": X won\n";}
          else
          if(dotf==1)
          {fout<<"Case #"<<index+1<<": Game has not completed\n";}
          else
		fout<<"Case #"<<index+1<<": Draw\n";
           
          

   }
  fin.close();
  fout.close();
  return 0;
}
