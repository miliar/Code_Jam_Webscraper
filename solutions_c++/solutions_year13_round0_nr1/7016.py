#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("alarge.txt","w",stdout);
    int t;
    cin>>t;
    int c=1;
    while(t--)
    {
              char a[4][4];
              int i,j,x,o,flagx=0,flago=0,empty=0;
              for(i=0;i<4;i++)
              {
                              x=0;
                              o=0;
                              for(j=0;j<4;j++)
                              {
                                              cin>>a[i][j];
                                              if((a[i][j]=='X')||(a[i][j]=='T'))
                                              x++;
                                              if((a[i][j]=='O')||(a[i][j]=='T'))
                                              o++;
                                              if(a[i][j]=='.')
                                              empty=1;
                              }
                              if(x==4)
                              flagx=1;
                              if(o==4)
                              flago=1;
                              
              }
              
              for(j=0;j<4;j++)
              {
                              x=0;
                              o=0;
                              for(i=0;i<4;i++)
                              {               
                                           if((a[i][j]=='X')||(a[i][j]=='T'))
                                              x++;
                                              if((a[i][j]=='O')||(a[i][j]=='T'))
                                              o++; 
                              }
                              if(x==4)
                              flagx=1;
                              if(o==4)
                              flago=1;
              }
              x=0;
                              o=0;
              for(i=0;i<4;i++)
              {
                              if((a[i][i]=='X')||(a[i][i]=='T'))
                                              x++;
                                              if((a[i][i]=='O')||(a[i][i]=='T'))
                                              o++; 
              }
              if(x==4)
                              flagx=1;
                              if(o==4)
                              flago=1;
                       x=0;
                              o=0;
               for(i=0;i<4;i++)
              {
                              if((a[i][3-i]=='X')||(a[i][3-i]=='T'))
                                              x++;
                                              if((a[i][3-i]=='O')||(a[i][3-i]=='T'))
                                              o++; 
              }
              if(x==4)
                              flagx=1;
                              if(o==4)
                              flago=1;                    
                             cout<<"Case #"<<c<<": ";
                             c++;
                             if(flagx==1)
                             cout<<"X won"<<endl;
                             else if(flago==1)
                             cout<<"O won"<<endl;
                             else if(empty==1)
                             cout<<"Game has not completed"<<endl;
                             else
                             cout<<"Draw"<<endl;
    }
    return 0;
}  
