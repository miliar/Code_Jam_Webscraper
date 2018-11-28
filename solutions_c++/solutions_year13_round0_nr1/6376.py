#include<iostream>
using namespace std;

char arr[4][4];
int flagx,flago;

void chk_o()
{
     //columns
     for(int j=0;j<4;j++)
     {
             int cnto=0,cntt=0;
             for(int i=0;i<4;i++)
             {
                     if(arr[i][j]=='T')
                                       cntt++;
                     if(arr[i][j]=='O')
                                       cnto++;
             }
             
             if(cnto==4 || (cnto==3 && cntt==1))
             {
                        flago=1;
                        return;
             }
     }
     
     //rows
     for(int i=0;i<4;i++)
     {
             int cnto=0,cntt=0;
             for(int j=0;j<4;j++)
             {
                     if(arr[i][j]=='T')
                                       cntt++;
                     if(arr[i][j]=='O')
                                       cnto++;
             }
             
             if(cnto==4 || (cnto==3 && cntt==1))
             {
                        flago=1;
                        return;
             }
     }
     
     //diagonals
     int cnto=0,cntt=0;
     for(int i=0;i<4;i++)
     {
              if(arr[i][i]=='T')
                         cntt++;
              if(arr[i][i]=='O')
                         cnto++;
     }
     
     if(cnto==4 || (cnto==3 && cntt==1))
     {
                 flago=1;
                 return;
     }
     
     cnto=0,cntt=0;
     for(int i=0;i<4;i++)
     {
              if(arr[i][3-i]=='T')
                         cntt++;
              if(arr[i][3-i]=='O')
                         cnto++;
     }
     
     if(cnto==4 || (cnto==3 && cntt==1))
     {
                 flago=1;
                 return;
     }
}

void chk_x()
{
     //columns
     for(int j=0;j<4;j++)
     {
             int cntx=0,cntt=0;
             for(int i=0;i<4;i++)
             {
                     if(arr[i][j]=='T')
                                       cntt++;
                     if(arr[i][j]=='X')
                                       cntx++;
             }
             
             if(cntx==4 || (cntx==3 && cntt==1))
             {
                        flagx=1;
                        return;
             }
     }
    
     //rows
     for(int i=0;i<4;i++)
     {
             int cntx=0,cntt=0;
             for(int j=0;j<4;j++)
             {
                     if(arr[i][j]=='T')
                                       cntt++;
                     if(arr[i][j]=='X')
                                       cntx++;
             }
             
             if(cntx==4 || (cntx==3 && cntt==1))
             {
                        flagx=1;
                        return;
             }
     }
     
     //diagonals
     int cntx=0,cntt=0;
     for(int i=0;i<4;i++)
     {
              if(arr[i][i]=='T')
                         cntt++;
              if(arr[i][i]=='X')
                         cntx++;
     }
     
     if(cntx==4 || (cntx==3 && cntt==1))
     {
                 flagx=1;
                 return;
     }
     
     cntx=0,cntt=0;
     for(int i=0;i<4;i++)
     {
              if(arr[i][3-i]=='T')
                         cntt++;
              if(arr[i][3-i]=='X')
                         cntx++;
     }
     
     if(cntx==4 || (cntx==3 && cntt==1))
     {
                 flagx=1;
                 return;
     }
}
      
int main()
{
    
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    
    
    int t,x=1;
    scanf("%d\n",&t);
    
    while(t--)
    {
              flagx=0,flago=0;
              int empty=0;
              
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%c",&arr[i][j]);
                              if(arr[i][j]=='.')
                                                empty=1;
                      }
                      scanf("\n");
              }
             
              chk_x();
              
              if(flagx==1)
              {
                          printf("Case #%d: X won\n",x++);   
                          continue;
              }
              if(flagx==0)
                          chk_o();
              
              if(flago==1)
              {
                          printf("Case #%d: O won\n",x++);
                          continue;
              }
                          
              if(flagx==0 && flago==0)
              {
                          if(empty==0)
                          {
                                      printf("Case #%d: Draw\n",x++);
                          }
                          else if(empty==1)
                          {
                               printf("Case #%d: Game has not completed\n",x++);
                          }
              }
    }
}
