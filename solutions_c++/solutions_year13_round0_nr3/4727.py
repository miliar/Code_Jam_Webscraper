#include<iostream>
#include<stdio.h>
#include<math.h>
#include<conio.h>
using namespace std;

main()
{
      int t,i,count,cnt,r,ans[10020];
      long min, max, j;
      long fstsq, diff,newnum,a,root;
      cin>>t;
      for(i=0;i<t;i++)
      {
              count=0;
              cnt=0;
              diff=1;
              scanf("%ld%ld",&min,&max);
              for(j=min;j<=max;j=j+diff)
              {
                                   root=sqrt(j);
                                   if(root*root == j)
                                   {
                                              //  cout<<j<<" "<<diff<<"\n";
                                                if(cnt<2)
                                                {
                                                         if(cnt==0)
                                                         {
                                                                   fstsq=j;
                                                                   cnt++;
                                                                   }
                                                         else
                                                         {
                                                             diff=j-fstsq+2;
                                                             cnt++;
                                                             }
                                                }
                                                else
                                                    diff+=2;
                                                a=j;
                                                newnum=0;
                                                while(a!=0)
                                                {
                                                      r=a%10;
                                                      a=a/10;
                                                      newnum=(newnum*10)+r;     
                                                           }
                                                if(newnum==j)
                                                {
                                                             a=root;
                                                             newnum=0;
                                                             while(a!=0)
                                                             {
                                                                        r=a%10;
                                                                        a=a/10;
                                                                        newnum=(newnum*10)+r;     
                                                                        }
                                                             if(newnum==root)
                                                             count++;
                                                           
                                                }
                                                              
                                   }
                                   
              }
           //   cout<<"Case #"<<i+1<<": "<<count<<"\n";
           ans[i]=count;
      }
      for(i=0;i<t;i++)
      {
                      cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
                      }
getch();
}
