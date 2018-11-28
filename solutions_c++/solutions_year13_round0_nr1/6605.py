#include<iostream>
using namespace std;
int check(char A[4][4]);
int main()
{
char A[4][4];
int c,s=1;
cin>>c;
while(c!=0)
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cin >> A[i][j];
    }        
   int t=check(A);
   if(t==1)
    cout<<"Case #"<<s<<": "<<"X won\n";
    else if(t==2)
    cout<<"Case #"<<s<<": "<<"O won\n";
    else if(t==3)
    cout<<"Case #"<<s<<": "<<"Draw\n";
    else if(t==4)
    cout<<"Case #"<<s<<": "<<"Game has not completed\n";
c--; 
s++;
}    

return 0;
}

int check(char A[4][4])
{   
 int f1=1,count=0;
  //if X wins
    for(int i=0;i<4;i++)
    {
       f1=1,count=0;
        for(int j=0;j<4;j++)
            {
            if(A[i][j]=='X')
             {
              
             }
             else if(A[i][j]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
              else{f1=0;break;}
            }
             if(f1==1)
             {break;}
    }  
      if(f1==1)
      {return 1;}     
      f1=1; 
      for(int i=0;i<4;i++)
    {
      f1=1,count=0;
        for(int j=0;j<4;j++)
            {
            if(A[j][i]=='X')
             {
             }
             else if(A[j][i]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
              else{f1=0;break;}
            }
             if(f1==1)
             {break;}
    }       
       if(f1==1)
      {return 1;}         
  f1=1,count=0; 
 for(int i=0;i<4;i++)
    {
        if(A[i][i]=='X')
         {}
          else if(A[i][i]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
         else{f1=0;break;}
    }  
if(f1==1)
      {return 1;}  
  f1=1,count=0; 
  for(int i=0,j=3;i<4;i++,j--)
    {
        if(A[i][j]=='X')
         {}
          else if(A[i][j]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
         else{f1=0;break;}
    } 
if(f1==1)
      {return 1;} 

// if O win

f1=1,count=0;
for(int i=0;i<4;i++)
    {
       f1=1,count=0;
        for(int j=0;j<4;j++)
            {
            if(A[i][j]=='O')
             {
              
             }
             else if(A[i][j]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
              else{f1=0;break;}
            }
             if(f1==1)
             {break;}
    }  
      if(f1==1)
      {return 2;}     
      f1=1; 
      for(int i=0;i<4;i++)
       {
      f1=1,count=0;
        for(int j=0;j<4;j++)
            {
            if(A[j][i]=='O')
             {
             }
             else if(A[j][i]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
              else{f1=0;break;}
            }
             if(f1==1)
             {break;}
    }       
       if(f1==1)
      {return 2;}         
  f1=1,count=0; 
 for(int i=0;i<4;i++)
    {
        if(A[i][i]=='O')
         {}
         else if(A[i][i]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
         else{f1=0;break;}
    }  
if(f1==1)
      {return 2;}  
  f1=1,count=0; 
 for(int i=0,j=3;i<4;i++,j--)
    {
        if(A[i][j]=='O')
         {}
          else if(A[i][j]=='T')
             { 
             count++;
              if(count>1)
              {f1=0;break;}
             }
         else{f1=0;break;}
    }  
if(f1==1)
      {return 2;} 


// draw
 int c=0;
 for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            {
               if(A[i][j]=='X'||A[i][j]=='T'||A[i][j]=='O')
                {}
                else{c=1;break;}
            }
           if(c==1)
            {break;}
    }     


if(c==0)
return 3;
else
return 4;
}
