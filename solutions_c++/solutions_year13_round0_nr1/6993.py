#include<iostream>
using namespace std;
main()
{
      int i,j;
      long int t1;
char t[4][4];
int c2,test;
cin>>test;
t1=1;

while(t1<=test)
{
       
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>t[i][j];

}

}
c2=0;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
if(t[i][j]=='X' || t[i][j]=='T' || t[i][j]=='O')
c2++;
}
 cout<<"Case #"<<t1<<": ";       
   int row, col, r, c, d,ct,dt,rt, ro, co, dO,d1,dO1,dt1;
 dO1=0;dt1=0;d1=0;
        for (row=0; row<4; row++)
        {
                r=0;
                c=0;
                d=0;
                ct=0;dt=0;rt=0;
               
                ro=0;
                co=0;
                dO=0;
                for (col=0; col<4; col++)
                {
                    if((row+col)==3)
                     {
                     if(t[row][col]=='X')
                     d1++;
                     if(t[row][col]=='O')
                       dO1++;
                       if(t[row][col]=='T')
                       dt1++;
                     }
                                    if(t[row][col]=='X')
                                r++;
                     if(t[row][col]=='T')
                        rt++;
                       if(t[row][col]=='O')
                                ro++;
                      if(t[col][row]=='X')
                                c++;
                        if(t[col][row]=='O')
                                co++;
                      if(t[col][row]=='T')
                         ct++;
                       if(t[col][col]=='X')
                                d++;
                      if(t[col][col]=='O')
                                dO++;
                      if(t[col][col]=='T')
                     dt++;   
                     
                     
                }
            
                //cout<<r<< c<<d <<ro<<co<<dO<<rt<<dt<<ct<<dO1<<dt1<<"\n";
                if((r==3&&rt==1)||r==4)
                {
                cout<<"X won"; 
                break;
                }
        if((c==3&&ct==1)|c==4)
                {
                cout<<"X won"; 
                break;
                }
            if((d==3&&dt==1)||d==4)
                {
                cout<<"X won"; 
                break;
                }
      if((ro==3&&rt==1)||ro==4||(co==3&&ct==1)||co==4|(dO==3&&dt==1)|| dO==4)
                {
                cout<<"O won"; 
                break;
                }
                
  
        
         if((d1==3&&dt1==1)|| d1==4)
                {
                cout<<"X won"; 
                break;
                }
                
        
 if((dO1==3&&dt1==1)|| dO1==4)
                {
                cout<<"O won"; 
                break;
                }
else if(c2==16&& row==3)
      cout<<"Draw";               
     else if(c2!=16 && row==3)
     cout<<"Game has not completed"; 
                }
                cout<<"\n";
                         t1++;
                }
 
}
