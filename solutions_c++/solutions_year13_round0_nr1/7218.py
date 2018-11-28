#include<stdio.h>
#include<iostream>
#include<fstream>

using namespace std;

main()
{
      char a[5],b[5],c[5],d[5],cr;
      int t,i,j,k,check1=0,check2=0,dot=0;
      ifstream ifile("E:/tic.txt");
      ofstream ofile("E:/tac.txt");
      ifile>>t;
      for (i=1;i<=t;i++)
      {
          check1=0;
          check2=0;
          dot=0;
          ifile>>a;
          ifile>>b;
          ifile>>c;
          ifile>>d;
          for (j=0;j<=3;j++)
          {
              if ((a[j]=='T') || (a[j]=='X'))
              {
                         check1=1;
              }
              else if (a[j]=='.')
              {
                   dot=1;
                   check1=0;
                   break;
              }    
              else 
              {
                   check1=0;
                   break;
              }
          }
          
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((a[j]=='T') || (a[j]=='O'))
              {
                         check2=1;
              }
              else if (a[j]=='.')
              {
                   dot=1;
                   check2=0;
                   break;
              }    
              else 
              {
                   check2=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((b[j]=='T') || (b[j]=='X'))
              { 
                         check1=1;
              }
              else if (b[j]=='.')
              {
                   dot=1;
                   check1=0;
                   break;
              }    
              else 
              {
                   check1=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((b[j]=='T') || (b[j]=='O'))
              {
                         check2=1;
              }
              else if (b[j]=='.')
              {
                   dot=1;
                   check2=0;
                   break;
              }    
              else 
              {
                   check2=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((c[j]=='T') || (c[j]=='X'))
              {
                         check1=1;
              }
              else if (c[j]=='.')
              {
                   dot=1;
                   check1=0;
                   break;
              }    
              else 
              {
                   check1=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((c[j]=='T') || (c[j]=='O'))
              {
                         check2=1;
              }
              else if (c[j]=='.')
              {
                   dot=1;
                   check2=0;
                   break;
              }    
              else 
              {
                   check2=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((d[j]=='T') || (d[j]=='X'))
              {
                         check1=1;
              }
              else if (d[j]=='.')
              {
                   dot=1;
                   check1=0;
                   break;
              }    
              else 
              {
                   check1=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
          for (j=0;j<=3;j++)
          {
              if ((d[j]=='T') || (d[j]=='O'))
              {
                         check2=1;
              }
              else if (d[j]=='.')
              {
                   dot=1;
                   check2=0;
                   break;
              }    
              else 
              {
                   check2=0;
                   break;
              }
          }
          }
          if ((check1==0) && (check2==0))
          {
                       for (j=0;j<=3;j++)
                       {
                           if (((a[j]=='X') || (a[j]=='T')) && ((b[j]=='X') || (b[j]=='T')) && ((c[j]=='X') || (c[j]=='T')) && ((d[j]=='X') || (d[j]=='T')))
                           {
                                             check1=1;
                                             break;
                           }
                       }
          }
          if ((check1==0) && (check2==0))
          {
                       for (j=0;j<=3;j++)
                       {
                           if (((a[j]=='O') || (a[j]=='T')) && ((b[j]=='O') || (b[j]=='T')) && ((c[j]=='O') || (c[j]=='T')) && ((d[j]=='O') || (d[j]=='T')))
                           {
                                             check2=1;
                                             break;
                           }
                       }
          }
          if ((check1==0) && (check2==0))
          {
                       if (((a[0]=='X') || (a[0]=='T')) && ((b[1]=='X') || (b[1]=='T')) && ((c[2]=='X') || (c[2]=='T')) && ((d[3]=='X') || (d[3]=='T')))
                       check1=1;
          }
          if ((check1==0) && (check2==0))
          {
                        if (((a[0]=='O') || (a[0]=='T')) && ((b[1]=='O') || (b[1]=='T')) && ((c[2]=='O') || (c[2]=='T')) && ((d[3]=='O') || (d[3]=='T')))
                       check2=1;
          }
          if ((check1==0) && (check2==0))
          {
                       if (((a[3]=='X') || (a[3]=='T')) && ((b[2]=='X') || (b[2]=='T')) && ((c[1]=='X') || (c[1]=='T')) && ((d[0]=='X') || (d[0]=='T')))
                       check1=1;
          }
          if ((check1==0) && (check2==0))
          {
                        if (((a[3]=='O') || (a[3]=='T')) && ((b[2]=='O') || (b[2]=='T')) && ((c[1]=='O') || (c[1]=='T')) && ((d[0]=='O') || (d[0]=='T')))
                       check2=1;
          }
          if ((check1==1) || (check2==1))
          {
                         if (check1==1)
                         {
                                      ofile<<"Case #"<<i<<": X won"<<endl;
                         }
                         else
                         {
                                       ofile<<"Case #"<<i<<": O won"<<endl;
                         }
          }
          else 
          {    int sa;
               for(sa=0;sa<4;++sa)
               {
                                  if(a[sa]=='.') {dot=1; break;}
                                  }
                                  for(sa=0;sa<4;++sa)
               {
                                        if(b[sa]=='.') {dot=1; break;}
                                  }
                                  for(sa=0;sa<4;++sa)
               {
                                  if(c[sa]=='.') {dot=1; break;}
                                  }
                                  for(sa=0;sa<4;++sa)
               {
                                  if(d[sa]=='.') {dot=1; break;}
                                  }
               
               if (dot==1)
          {
                                       ofile<<"Case #"<<i<<": Game has not completed"<<endl;
          }
          else 
          {
               ofile<<"Case #"<<i<<": Draw"<<endl;
          }
          }
      }
}   
          
                             
