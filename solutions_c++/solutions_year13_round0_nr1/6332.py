#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>

#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define T_Max  10000
void toggle(int&x);

int main ()
{
 int i,j,T,ccase;
 char box[16];
 int boxint[16];
    
      
                 freopen("A-large.in","rt",stdin);    
                 freopen("A-large.out","wt",stdout);    
      
                 
				 cin>>T;    
    
    
    

    
                  rep(i,T)    
                                                    
                  {    
    
    ccase=3;
	                      rep(j,16)   
						    {cin>>box[j];
						    if(box[j]=='O')boxint[j]=2;
						    else if(box[j]=='X')boxint[j]=3;
						    else if(box[j]=='T')boxint[j]=1;
						    else if(box[j]=='.'){boxint[j]=10;ccase=4; }
						    }
							
							for(int m=0;m<=12;m+=4)
							{
							if( (boxint[m+0]+boxint[m+1]+boxint[m+2]+boxint[m+3])==10  && (boxint[m+0]*boxint[m+1]*boxint[m+2]*boxint[m+3])==27)    
    				    	{ccase=1;exit;
    				    	}
    				    					
							if( (boxint[m+0]+boxint[m+1]+boxint[m+2]+boxint[m+3])==12 && (boxint[m+0]*boxint[m+1]*boxint[m+2]*boxint[m+3])==81)    
    						{
    						ccase=1;exit;}
    						  						
    						  						
							if( (boxint[m+0]+boxint[m+1]+boxint[m+2]+boxint[m+3])==7 && (boxint[m+0]*boxint[m+1]*boxint[m+2]*boxint[m+3])==8)    
    				    	{
    				    	ccase=2;exit;}
    				    
							if( (boxint[m+0]+boxint[m+1]+boxint[m+2]+boxint[m+3])==8 && (boxint[m+0]*boxint[m+1]*boxint[m+2]*boxint[m+3])==16)    
    						{
    						ccase=2;exit;}
    						
    						
							}
    
							for(int m=0;m<=3;m+=1)
							{
							if( (boxint[m+0]+boxint[m+4]+boxint[m+8]+boxint[m+12])==10 && (boxint[m+0]*boxint[m+4]*boxint[m+8]*boxint[m+12])==27)    
    				    	{
    				    	ccase=1;exit;}
    				    					
							if( (boxint[m+0]+boxint[m+4]+boxint[m+8]+boxint[m+12])==12 && (boxint[m+0]*boxint[m+4]*boxint[m+8]*boxint[m+12])==81)    
    						{
    						ccase=1;exit;}
    						  						
    						  						
							if( (boxint[m+0]+boxint[m+4]+boxint[m+8]+boxint[m+12])==7 && (boxint[m+0]*boxint[m+4]*boxint[m+8]*boxint[m+12])==8)    
    				    	{
    				    	ccase=2;exit;}
    				    					
							if( (boxint[m+0]+boxint[m+4]+boxint[m+8]+boxint[m+12])==8 && (boxint[m+0]*boxint[m+4]*boxint[m+8]*boxint[m+12])==16)    
    						{
    						ccase=2;exit;}
    						
    						
							}
    
    
    
	
							{
							if( (boxint[0]+boxint[5]+boxint[10]+boxint[15])==10 && (boxint[0]*boxint[5]*boxint[10]*boxint[15])==27)    
    				    	ccase=1;
    				    					
							if( (boxint[0]+boxint[5]+boxint[10]+boxint[15])==12 && (boxint[0]*boxint[5]*boxint[10]*boxint[15])==81 )    
    						ccase=1;
    						  						
    						  						
							if( (boxint[0]+boxint[5]+boxint[10]+boxint[15])==7 && (boxint[0]*boxint[5]*boxint[10]*boxint[15])==8)    
    				    	ccase=2;
    				    					
							if( (boxint[0]+boxint[5]+boxint[10]+boxint[15])==8 && (boxint[0]*boxint[5]*boxint[10]*boxint[15])==16)    
    						ccase=2;
    						
    						
							}
    
    
							{
							if( (boxint[3]+boxint[6]+boxint[9]+boxint[12])==10 && (boxint[3]*boxint[6]*boxint[9]*boxint[12])==27)    
    				    	ccase=1;
    				    					
							if( (boxint[3]+boxint[6]+boxint[9]+boxint[12])==12 && (boxint[3]*boxint[6]*boxint[9]*boxint[12])==81)    
    						ccase=1;
    						  						
    						  						
							if( (boxint[3]+boxint[6]+boxint[9]+boxint[12])==7 && (boxint[3]*boxint[6]*boxint[9]*boxint[12])==8)    
    				    	ccase=2;
    				    					
							if( (boxint[3]+boxint[6]+boxint[9]+boxint[12])==8 && (boxint[3]*boxint[6]*boxint[9]*boxint[12])==16)    
    						ccase=2;
    						
    						
							}
    
    
    
    if(ccase==1){cout<<"Case #"<<i+1<<": X won";}
	else if(ccase==2){cout<<"Case #"<<i+1<<": O won";}
	else if(ccase==4){cout<<"Case #"<<i+1<<": Game has not completed";}
	else {cout<<"Case #"<<i+1<<": Draw";}
	 cout<<endl;
	 
				  }
    
       
  return 0;    
}    
    
    
void toggle(int &x)    
{    
                 if(x==0)
					 x=1;    
                 else 
				       x=0;    
}     

 
