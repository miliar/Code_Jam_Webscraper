#include<stdio.h>
char a[6][6];
int x,o;
void in()
{    int i,j;
     for(i=0;i<4;i++)
              {               
                              for(j=0;j<4;j++)
                              scanf("%c",&a[i][j]);
                            //  printf("in loop");
                            //fflush(stdin);
                              scanf("\n");
              }
}


/*void print()
{    int i,j;
      for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              printf("%c",a[i][j]);
                              printf("\n");
              }
}
*/
int rowcheck()
{
         int i,j;
              for(i=0;i<4;i++)//row
              {               
                              x=0;
                              o=0;
                              for(j=0;j<4;j++)
                              {
                                              if(a[i][j]=='X'||a[i][j]=='T')
                                              x++;
                                              
                                              if(a[i][j]=='O'||a[i][j]=='T')
                                              o++;
                              }
                              if(x==4||o==4)
                              {
                                          // printf("x=%d o=%d\n",x,o);
                                           return 1;
                              }
                              
              }
              return 0;
}

int colcheck()
{
    int i1,j1;
               
               for(i1=0;i1<4;i1++)//start
               {
                                   
                x=0;
                o=0;
                for(j1=0;j1<4;j1++)
                {
                   if(a[j1][i1]=='X'||a[j1][i1]=='T')
                   x++;
                                              
                   if(a[j1][i1]=='O'||a[j1][i1]=='T')
                   o++;
                }
                if(x==4||o==4)
                {
                      //   printf("x=%d o=%d\n",x,o);     
                          return 1;    
                }
               }//end
             return 0; 
}
    
int main()
{
    int t,t1,i,i1,i2,i3,j,j1,j2,j3,f1,f2;
    FILE *f;
    f=freopen("A-large.in","r",stdin);
    freopen("oo.txt","w",stdout);
    scanf("%d\n",&t);
    t1=t;
   // printf("%d\n",t);
    for(t=1;t<=t1;t++)
    {      
            //// printf("int test case %d\n",t);
             in();
            // print();
             f1=rowcheck();
             if(f1==1)            //if start
             {// printf("in f=1");
             
               if(x==4)
               {
                      printf("Case #%d: X won\n",t);
                                      
               }
               else
               {
                      printf("Case #%d: O won\n",t);
                                     
               }
             }
             else 
             {                     //else start
               f2=colcheck();
               if(f2==1)
               {
                if(x==4)
                {
                 printf("Case #%d: X won\n",t);
                }
                else
                {
                 printf("Case #%d: O won\n",t);
                }
               }
               else
               {
                i2=0;
                x=o=0;
                while(i2<4)
                {
                  if(a[i2][i2]=='X'||a[i2][i2]=='T')
                  x++;
                                              
                  if(a[i2][i2]=='O'||a[i2][i2]=='T')
                  o++;
                  i2++;
                }
              //    printf("x=%d o=%d\n",x,o);
                if(x!=4&&o!=4)
                {x=o=0;
                 for(i2=0;i2<4;i2++)
                 {
                                    for(j2=0;j2<4;j2++)
                                    {
                                                       if(i2+j2==3)
                                                       {
                                                                    if(a[i2][j2]=='X'||a[i2][j2]=='T')
                                                                    x++;
                                                                    if(a[i2][j2]=='O'||a[i2][j2]=='T')
                                                                    o++;
                                                       }
                                    }
                 }
                }
               // printf("x=%d o=%d\n",x,o);
                if(x==4)
                {
                 printf("Case #%d: X won\n",t);
                }
                else if(o==4)
                {
                 printf("Case #%d: O won\n",t);
                }
                else
                {
                 for(i3=0;i3<4;i3++)
                 {                x=0;
                                                            for(j3=0;j3<4;j3++)
                                                            if(a[i3][j3]=='.')
                                                            {
                                                                              printf("Case #%d: Game has not completed\n",t);
                                                                              x=1;
                                                                              break;
                                                            }
                                                            if(x==1)
                                                            break;
                 }
                  if(x==0)
                  {
                   printf("Case #%d: Draw\n",t);
                  }
                }
               }
              }
              scanf("\n");
                              
}
    fclose(f);
    return 0;
}
                                              
