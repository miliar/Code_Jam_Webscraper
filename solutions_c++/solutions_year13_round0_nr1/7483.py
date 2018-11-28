#include<stdio.h>
int main()
{
    int t,save,i,j,cx=0,cy=0,val;
    char s[6][6],ch;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    save=t;
    ch=getchar();
    while(save--)
    {
              val=0;
              for(i=0;i<4;i++)
              {
                             scanf("%s",s[i]);
              }
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              if(s[i][j]!='.')
                                              {
                                                              val++;
                                              }
                              }
              }
              for(i=0;i<4;i++)
              {
                              cx=0;
                              cy=0;
                              for(j=0;j<4;j++)
                              {
                                              if(s[i][j]=='X')
                                              {
                                                              cx++;
                                              }
                                              else if(s[i][j]=='O')
                                              {
                                                   cy++;
                                              }
                                              else if(s[i][j]=='T')
                                              {
                                                   cx++;
                                                   cy++;
                                              }
                              }
                              if(cx==4||cy==4)
                              {
                                              break;
                              }
              }
              if(cx==4)
              {
                       printf("Case #%d: X won\n",t-save);
                       continue;
              }
              else if(cy==4)
              {
                   printf("Case #%d: O won\n",t-save);
                   continue;
              }
              else
              {
                  for(i=0;i<4;i++)
                  {
                                  cx=0;
                                  cy=0;
                                  for(j=0;j<4;j++)
                                  {
                                                  if(s[j][i]=='X')
                                                  {
                                                                  cx++;
                                                  }
                                                  else if(s[j][i]=='O')
                                                  {
                                                       cy++;
                                                  }
                                                  else if(s[j][i]=='T')
                                                  {
                                                       cy++;
                                                       cx++;
                                                  }
                                  }
                                  if(cx==4||cy==4)
                                  {
                                                  break;
                                  }
                  }
                  if(cx==4)
                  {
                           printf("Case #%d: X won\n",t-save);
                           continue;
                  }
                  else if(cy==4)
                  {
                       printf("Case #%d: O won\n",t-save);
                       continue;
                  }
              }
              cx=0;
              cy=0;
              for(i=0;i<4;i++)
              {
                              if(s[i][i]=='X')
                              {
                                              cx++;
                              }
                              else if(s[i][i]=='O')
                              {
                                   cy++;
                              }
                              else if(s[i][i]=='T')
                              {
                                   cx++;
                                   cy++;
                              }
              }
              if(cx==4)
              {
                       printf("Case #%d: X won\n",t-save);
                       continue;
              }
              else if(cy==4)
              {
                   printf("Case #%d: O won\n",t-save);
                   continue;
              }
              cx=0;
              cy=0;
              for(i=0;i<4;i++)
              {
                              if(s[i][3-i]=='X')
                              {
                                                cx++;
                              }
                              else if(s[i][3-i]=='O')
                              {
                                   cy++;
                              }
                              else if(s[i][3-i]=='T')
                              {
                                   cx++;
                                   cy++;
                              }
              }
              if(cx==4)
              {
                       printf("Case #%d: X won\n",t-save);
                       continue;
              }
              else if(cy==4)
              {
                   printf("Case #%d: O won\n",t-save);
                   continue;
              }
              if(val==16)
              {
                         printf("Case #%d: Draw\n",t-save);
              }
              else
              {
                  printf("Case #%d: Game has not completed\n",t-save);
              }
    }
    return 0;
}
              
              
