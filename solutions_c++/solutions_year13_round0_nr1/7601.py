#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
   ifstream in ("emad.in");
   ofstream out("output.txt");
   int c=1; 
   int cm=1,cc=0;
   char n[4][4];
   int f=3;
   long int count;
   cout<<"enter no. of sen."<<endl;
  // cin>>m;
   
   string x;
   getline(in,x);
   
   count = atoi(x.c_str());
   for(long int i=0;i<count;i++)
  { cc=0;
        f=3;
         for(int j=0;j<4;j++)
          for(int k=0;k<4;k++)
          in>>n[j][k];
          for(int j=0;j<4;j++)
          for(int k=0;k<4;k++)
          if(n[j][k]=='.')
          cc++;
      // for(int j=0;j<4;j++)
          for(int k=0;k<4;k++)
          {
             
            if ((n[k][0]=='X'||n[k][0]=='T') &&( n[k][1]=='X'||n[k][1]=='T' )&& (n[k][2]=='X'||n[k][2]=='T' )&&( n[k][3]=='X'||n[k][3]=='T'))
            {
           f=0;
           //cout<<"1";
           break;
           
        }
            if ((n[0][k]=='X'||n[0][k]=='T')&&(n[1][k]=='X'||n[1][k]=='T')&&(n[2][k]=='X'||n[2][k]=='T')&&(n[3][k]=='X'||n[3][k]=='T'))
           {
          f=0;
          // cout<<"2";
             break;
           
        }
           
         
          if((n[0][0]=='X'||n[0][0]=='T')&&(n[1][1]=='X'||n[1][1]=='T')&&(n[2][2]=='X'||n[2][2]=='T')&&(n[3][3]=='X'||n[3][3]=='T'))
           {
          f=0;
          // cout<<"3";
             break;
           
        }
           if((n[0][3]=='X'||n[0][3]=='T')&&(n[1][2]=='X'||n[1][2]=='T')&&(n[2][1]=='X'||n[2][1]=='T')&&(n[3][0]=='X'||n[3][0]=='T'))
           {
           f=0;
           //cout<<"4";
             break;
          
        } 
           if ((n[k][0]=='O'||n[k][0]=='T')&&(n[k][1]=='O'||n[k][1]=='T')&&(n[k][2]=='O'||n[k][2]=='T')&&(n[k][3]=='O'||n[k][3]=='T'))
           {
           f=1;
           
        }
            if ((n[0][k]=='O'||n[0][k]=='T')&&(n[1][k]=='O'||n[1][k]=='T')&&(n[2][k]=='O'||n[2][k]=='T')&&(n[3][k]=='O'||n[3][k]=='T'))
            {
           f=1;
        
        } 
           if((n[0][0]=='O'||n[0][0]=='T')&&(n[1][1]=='O'||n[1][1]=='T')&&(n[2][2]=='O'||n[2][2]=='T')&&(n[3][3]=='O'||n[3][3]=='T'))
            {
           f=1;
          
        }
           if((n[0][3]=='O'||n[0][3]=='T')&&(n[1][2]=='O'||n[1][2]=='T')&&(n[2][1]=='O'||n[2][1]=='T')&&(n[3][0]=='O'||n[3][0]=='T'))
            {
           f=1;
           
        } 
           if(f!=0||f!=1)
           {
              if (n[k][0]=='.'&&n[k][1]=='.'&&n[k][2]=='.'&&n[k][3]=='.')
              {
           f=2;  
          
           }
           if (n[0][k]=='.'&&n[1][k]=='.'&&n[2][k]=='.'&&n[3][k]=='.')
            {
           f=2;  
           
           }  
           
           
                
                }    
          
       
            
    }
    
   
     
 if(f==0){
            out<<"Case #"<<cm<<": X won"<<endl;
            goto mmm;
            }
            else
            if(f==1){      
            out<<"Case #"<<cm<<": O won"<<endl;
            goto mmm;
            }
             else  
             if(f==2||cc>0)   {
            out<<"Case #"<<cm<<": Game has not completed"<<endl;
            goto mmm;
            }
            else{
            out<<"Case #"<<cm<<": Draw"<<endl;}
            mmm :
            cm++;
          
           }
           
    
  //cin>>x;
   return 0; 
 }
