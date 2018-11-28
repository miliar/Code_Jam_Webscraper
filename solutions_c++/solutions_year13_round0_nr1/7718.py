#include <stdio.h>
char board[4][4];
void printstatus(int i,int s,bool nb)
 {
  printf("Case #%d: ",i);
  switch(s)
   {
    case 0: if(!nb)
             printf("Draw\n");
            else
             printf("Game has not completed\n");
             break;
    case 1: printf("X won\n");
            break;         
    case 2: printf("O won\n");
            break;         
           
   }    
 }
int main()
{
   
 int t;
 scanf("%d",&t);
 for(int i = 1 ; i<= t;i++)
  {
   char sp;
   
   int rx[4]= {0,0,0,0};
   int ro[4] = {0,0,0,0};
   int cx[4] = {0,0,0,0};
   int co[4] = {0,0,0,0};
   char ch;
   bool nb= false;
   int status = 0;
   for(int j= 0;j<4;j++)
    {
     scanf("%c",&sp); 
     for(int k =0;k<4;k++)     
        {
         scanf("%c",&ch);
         switch(ch)
         {
           case 'X': board[j][k] = 'X';
                 cx[k]++;
                 rx[j]++;
                 break;
           case 'T': board[j][k] = 'T';
                 cx[k]++;
                 rx[j]++;
                 co[k]++;
                 ro[j]++;
                 break;
           case 'O':  board[j][k] = 'O';
                 co[k]++;
                 ro[j]++;
                 break;
           case '.':  board[j][k] = '.';
                 nb = true;
                 break;
           }         
           }
          if(rx[j]==4)
           {status = 1;}
          else if(ro[j]==4)
           {status = 2;} 
         }
         if(status == 0)
          {
           for(int k =0;k<4;k++)
            {
             if(cx[k]==4)
              {
               status = 1;break;
              }
             if(co[k]==4)
              {
               status = 2;break;           
              }       
            }                   
           if(status == 0)
            { int nxd[2] = {0,0},nod[2] = {0,0};
             for(int k =0;k<4;k++)
              {
               switch(board[k][k])
                {
                 case 'X' : nxd[0]++;break;
                 case 'O' : nod[0]++;break;   
                 case 'T' : nxd[0]++;nod[0]++;break;               
                }
                switch(board[k][3-k])
                {
                 case 'X' : nxd[1]++;break;
                 case 'O' : nod[1]++;break;
                 case 'T' : nod[1]++;nxd[1]++;break;                  
                }       
              }         
             if(nxd[0] == 4 || nxd[1] == 4)
              status = 1;
             else if(nod[0] == 4 || nod[1] == 4)
              status = 2;
                  
            }      
           
          }
         printstatus(i,status,nb);
         if(i!=t)
          scanf("%c",&sp);
      
    }
    
    
}
                  
                   
   
