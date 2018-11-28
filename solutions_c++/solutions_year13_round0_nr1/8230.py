#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int check_t1(int i, int j, int k, int case1);
int check_t2(int i, int j, int k, int case1);
int check_oo(int i, int j, int k, int case1);
int check_xx(int i, int j, int k, int case1);
int check_diagonal(int i, int j, int k, int case1);
int check_opp(int i, int j, int k, int case1);
int check1(int i, int j, int k, int case1);
int check2(int i, int j, int k, int case1);
int check3(int i, int j, int k, int case1);
int calculation(int number, int i, int j, int k, int case1);
char a[50][4];
int index;
int input1()
{
    int i,j;
    	FILE *fp1;
    

    if((fp1=freopen("A-small-attempt0.in", "r" ,stdin))==NULL) {
      printf("Cannot open file.\n");
      exit(1);
    }
    scanf("%d",&index);
    index=index*4;
    for(i=0;i<index;i++)
    {
           scanf("%s",&a[i]);
    }
     fclose(fp1);
    return 0;
}
int cal()
{//start cal()
   int i,j,k,case1,m,z=1;
    i=0;
    while(i<index)
    {//while
        case1 = i/4;
        k=i/4;
        j=0;
        for(m=1;m<=8;m++)
        {
          z=calculation(m,i,j,k,case1);
          if(z==0)
          {
                i=i+4;
                break;
          }
        }
        if(z!=0)
        {
              z=check3(i,j,k,case1);
              if(z==0)
              {
              i=i+4;
              }
        }
    }//while
   return 0;
}
int calculation(int number, int i, int j,int k, int case1)
{//start
    int z;
      switch(number)
        {
             case 1 :
             {
              z=check_diagonal(i,j,k,case1);//st diagonal
              if(z==0)
              {
                      return 0;
              }
              else
              return 1;
             }
              case 2:
              {
                    z=check1(i,j,k,case1);//o on y axis
                    if(z==0)
                    {
                      return 0;
                    } 
                    else
                    return 1;
              }
              case 3:
              {
                     z=check2(i,j,k,case1);//x on y axis
                     if(z==0)
                     {
                      return 0;
                     }
                     else 
                     return 1;
              }
              case 4:
              {
                    z=check_xx(i,j,k,case1);//x on x axis
                    if(z==0)
                    {
                        return 0;
                    }
                    else
                    return 1;
              }
              case 5:
              {
                    z=check_oo(i,j,k,case1);//o on x axis
                    if(z==0)
                    {
                        return 0;
                    }       
                    else
                    return 1;
              }
              case 6:
              {
                    z=check_t1(i,j,k,case1);
                    if(z==0)
                    {
                        return 0;
                    }       
                    else
                    return 1;
              }
              case 7:
              {
                    z=check_t2(i,j,k,case1);
                    if(z==0)
                    {
                        return 0;
                    }       
                    else 
                    return 1;
              }
              case 8:
              {
                   z=check_opp(i,j,k,case1);
                   if(z==0)
                   {
                           return 0;
                   }
                   else 
                   return 1;
              }
        }
}//end
int check_t1(int i, int j, int k, int case1)
{//start
    int p=i,f;
    while(a[p][j]!='T' && k==case1)
    {//start while
          p=p+1;
          k=p/4;
    }//end while
    if(a[p][j]=='T')
    {//start outer if
       j=j+1;
       if(a[p][j]!='.')
       {//start inner if
           if(a[p][j]=='X')
           {//start innermost if
                j=j+1;
                while(a[p][j]=='X'&&j<4)
                {//start while
                    j=j+1;
                }//end while
                if(j==4)
                {//start if
                        printf("Case #%d: X won\n",case1+1);
                        return 0;
                }//end if
                else
                {//start else
                    return 1;
                }//end else
           }//end innermost if
           else
           {//start innermost else
               j=j+1;
                while(a[p][j]=='O'&&j<4)
                {//start while
                    j=j+1;
                }//end while
                if(j==4)
                {//start if
                        printf("Case #%d: O won\n",case1+1);
                        return 0;
                }//end if
                else
                {//start else
                    return 1;
                }//end else
           } //end innermost else
       }//end inner if 
       else
       {//start inner else
           return 1;
       }//end inner else
    }//end outer if
    else
    {
        return 1;
    }
}//end
int check_t2(int i, int j, int k, int case1)
{
               j=0;
               while(a[i][j]!='T' && j<4)
               {
                   j=j+1;
               }
               if(j<4)
               {
                  i=i+1;
                  if(a[i][j]!='.')
                  {
                  if(a[i][j]=='X')
                  {
                                  while(a[i][j]=='X'&&k==case1)
                                  {
                                         i=i+1;
                                         k=i/4;
                                  }
                                  if(k!=case1)
                                  {
                                         printf("Case #%d: X won\n",case1+1);
                                         return 0;
                                  }
                                  else
                                  {
                                         return 1;
                                  }
                  }
                  else
                  {
                                  while(a[i][j]=='O'&&k==case1)
                                  {
                                         i=i+1;
                                         k=i/4;
                                  }
                                  if(k!=case1)
                                  {
                                         printf("Case #%d: O won\n",case1+1);
                                         return 0;
                                  }
                                  else
                                  {
                                         return 1;
                                  }
                  }
                  }
                  else
                  {
                      return 1;
                  }
               }
               else
               {
                   return 1;
               }
               
}               
    
int check_xx(int i, int j, int k, int case1)
{
        while(a[i][j]!='X' && k==case1)
        {
            i=i+1;
            k=i/4;
        }
        if(a[i][j]=='T' || a[i][j]=='X')
        {
            j=j+1;
            while((a[i][j]=='X' || a[i][j]=='T') && j<4)
            {
                 j=j+1;
            }
            if(j==4)
            {
               printf("Case #%d: X won\n",case1+1);
               return 0;
            }
            else
            {
                return 1;
            }
        }
        else
        {
            return 1;
        }
}
int check_oo(int i, int j, int k, int case1)
{
        while(a[i][j]!='O' && k==case1)
        {
            i=i+1;
            k=i/4;
        }
        if(a[i][j]=='T' || a[i][j]=='O')
        {
            j=j+1;
            while((a[i][j]=='O' || a[i][j]=='T') && j<4)
            {
                 j=j+1;
            }
            if(j==4)
            {
               printf("Case #%d: O won\n",case1+1);
               return 0;
            }
            else
            {
                return 1;
            }
        }
        else
        {
            return 1;
        }
}
int check3(int i, int j, int k, int case1)
{
    while(k==case1)
    {
        j=0;
        while(a[i][j]!='.'&& j<4)
        {
            j=j+1;
        }
        if(j==4)
        {
            i=i+1;
            k=i/4;
        }
        else
        {
            printf("Case #%d: Game has not completed\n",case1+1);
            return 0;
        }
    }
    if(k>case1)
    {
        printf("Case #%d: Draw\n",case1+1);
        return 0;
    }
}
int check_opp(int i, int j, int k, int case1)
{
     j=3;
     if(a[i][j]=='T' || a[i][j]=='X')
     {//start if
           i=i+1;
           j=j-1;
           while((a[i][j]=='X' || a[i][j]=='T') && k==case1 )
           {//start while
                 i=i+1;
                 j=j-1;
                 k=i/4;
           }//end while
           if(k == (case1+1))
           {//start inner if
                 printf("Case #%d: X won\n",case1+1);
                 return 0;
           }//end inner iF
           else
           {
                 return 1;
           }
     }//end if
     else if(a[i][j]=='T' || a[i][j]=='O')
     {//start if
           i=i+1;
           j=j-1;
           while((a[i][j]=='O' || a[i][j]=='T') && k==case1 )
           {//start while
                  i=i+1;
                  j=j-1;
                  k=i/4;
           }//end while
           if(k == (case1+1))
           {//start inner if
                  printf("Case #%d: O won\n",case1+1);
                  return 0;
           }//end inner if
           else
           {
                  return 1;
           }
     }//end else if
     else
     {
         return 1;
     }         
}
int check_diagonal(int i, int j, int k, int case1)
{
    if(a[i][0]=='T' || a[i][0]=='X')
    {//start if
           j=j+1;
           i=i+1;
           while((a[i][j]=='X' || a[i][j]=='T') && k==case1 )
           {//start while
                i=i+1;
                j=j+1;
                k=i/4;
           }//end while
           if(k == (case1+1))
           {//start inner if
                printf("Case #%d: X won\n",case1+1);
                return 0;
           }//end inner if
           else
           {
               return 1;
           }
      }//end if
      else if(a[i][0]=='T' || a[i][0]=='O')
      {//start if
            i=i+1;
            j=j+1;
            while((a[i][j]=='O' || a[i][j]=='T') && k==case1 )
            {//start while
                  i=i+1; 
                  j=j+1;
                  k=i/4;
            }//end while
            if(k == (case1+1))
            {//start inner if
                  printf("Case #%d: O won\n",case1+1);
                  return 0;
            }//end inner if
            else
            {
                return 1;
            }
       }//end if 
       else
       {
           return 1;
       }    
}
       
                      


    
int check1(int i,int j,int k,int case1)//check O on y axis
{
               j=0;
               while(a[i][j]!='O' && j<4)
               {
                   j=j+1;
               }
               if(j<4)
               {
                  i=i+1;
                  while((a[i][j]=='O' || a[i][j]=='T') && k==case1)
                  {
                       i=i+1;
                       k=i/4;
                  }
                  if(k==(case1 +1))
                  {
                       printf("Case #%d: O won\n",case1+1);
                       return 0;
                  }
                  else
                  {
                      return 1;
                  }
              }
              else
              {
                  return 1;
              }
}
int check2(int i, int j, int k, int case1)//check X on y axis
{
               j=0;
               while(a[i][j]!='X' && j<4)
               {
                   j=j+1;
               }
               if(j<4)
               {
                 i=i+1;
                 while((a[i][j]=='X' || a[i][j]=='T') && k==case1)
                 {
                       i=i+1;
                       k=i/4;
                 }
                 if(k==(case1 +1))
                 {
                       printf("Case #%d: X won\n",case1+1);
                       return 0;
                 }
                 else
                 {
                  return 1;
                 }
              }
              else
              {
                  return 1;
              }
} 

int main()
{
    input1();
     FILE *fp;


    if((fp=freopen("OUT1", "w" ,stdout))==NULL) {
      printf("Cannot open file.\n");
      exit(1);
    }
     cal();
     fclose(fp);
    getch();
    return 0;
}
