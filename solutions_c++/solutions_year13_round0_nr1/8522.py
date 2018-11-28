#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
 int Tic(int i,char T[10][5][5])
                      {

                               int c1,c2,k,j,l,m;
                               c1=0;
                               c2=0;
                               for(j=1;j<4;j++)
                               {                                      
                                      if(T[i][j][j-1]==T[i][j+1][j]&&T[i][j][j-1]!='.')
                                      {
                                                                     c1++;
                                      }
                                      if(T[i][j][4-j]==T[i][j+1][3-j]&&T[i][j][4-j]!='.')
                                      {
                                                                     c2++;
                                      }
                               }
                               if((c1==3)||((c1==2)&&(T[i][1][0]=='T'||T[i][4][3]=='T')))
                               {
                                                                                       
                                                                                       
                                       printf("Case #%d: %c won",i+1,T[i][2][1]);                                                                                                        
                                       return 0 ;
                               } 
                                if((c2==3)||((c2==2)&&(T[i][1][3]=='T'||T[i][4][0]=='T')))
                               {
                                                                                         
                                       printf("Case #%d: %c won",i+1,T[i][2][2]);                                                                                                           
                                       return 0;
                                        ;
                               }                                    
                               for(j=1,l=1;j<5,l<5;j++,l++)
                               {
                                               c1=0;
                                               c2=0;
                                               for(k=0,m=0;k<3,m<3;k++,m++)
                                               {
                                                               if(T[i][j][k]==T[i][j][k+1]&&T[i][j][k]!='.')
                                                               {
                                                                     c1++;
                                                               }
                                                               if(T[i][m+1][l-1]==T[i][m+2][l-1]&&T[i][m+1][l-1]!='.')
                                                               {
                                                                     c2++;
                                                               }
                                               }
                                               if((c1==3)||((c1==2)&&((T[i][j][0])=='T'||T[i][j][3]=='T')))
                                               {
                                                       printf("Case #%d: %c won",i+1,T[i][j][1]);                                                            
                                                        return 0;
                                               }
                                               if((c2==3)||((c2==2)&&((T[i][1][l-1])=='T'||T[i][4][l-1]=='T')))
                                               {
                                                                                                              
                                                        printf("Case #%d: %c won",i+1,T[i][2][l-1]);                                                                                     
                                                        return 0;
                                               } 
                               }  
                               for(k=1;k<5;k++)
                               {
                                               for(j=0;j<4;j++)
                                               {
                                                               if(T[i][k][j]=='.')
                                                               {
                                                                                 printf("Case #%d: Game has not completed",i+1);                    
                                                                               return 0;
                                                               }
                                               }
                               }
                               printf("Case #%d: Draw",i+1);
                               return 0;
                      }
main()
{
      int n,z,j;
      char Q[10][5][5];
      int S;
      scanf ("%d",&n);
      for(z=0;z<n;z++)
      {
                      for(j=0;j<5;j++)
                      {
                                      gets(Q[z][j]);
                      }
      }
      
                     
                      for(z=0;z<n;z++)
                      {
                                      S=Tic(z,Q) ;                              
                                      printf("\n");
                      }
                      getch();
}
                                      
                                                                
                                                                  
                      
               
