#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<string>
using namespace std;

bool con(char c)
{
 if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
           return 0;
 return 1;
}

int main()
{
int t;
scanf("%d",&t);
int ca=0;
while(t--)
          {int answer=0;
          
          char s[101];
          getchar();
          scanf("%s",&s);
          int d;
          scanf("%d",&d);
          
          int l=strlen(s);
          int a[l][l];
          
          for(int i=0;i<l;i++)
          for(int j=0;j<l;j++)
                  {
                   a[i][j]=0;
                  }
          
          for(int i=0;i<l;i++)
                  {
                   if(con(s[i]))
                               {int j;
                                for(j=i+1;j<i+d && j<l;j++)
                                        {
                                         if(!con(s[j]))
                                                      break;
                                        }
                               if(j==(i+d))
                                          {
                                           answer++;
                                           a[i][j-1]=1;
                                           for(int k=0;k<=i;k++)
                                                   {
                                                    for(int p=j-1;p<l;p++) 
                                                    if(a[k][p]==0)
                                                                    {
                                                                     a[k][p]=1;
                                                                     answer++;
                                                                    }
                                                   
                                                   }
                                          
                                          
                                          }
                               }
                  }
                  
         /* for(int i=0;i<l;i++)
          {for(int j=0;j<l;j++)
                  cout<<a[i][j];
                  cout<<"\n";
                  }*/
                  ca++;
          printf("Case #%d: %d\n",ca,answer);
         
          }
}
