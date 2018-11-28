#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("asmall.txt","w",stdout);
    int t;
    cin>>t;
    int z=1;
    while(t--)
    {
              int x,i,a,n,s[105]={0},b;
              cin>>a>>n;
              for(i=0;i<n;i++)
              {
                              cin>>x;
                              s[x]++;
              }
              if(a==1)
              {
                      printf("Case #%d: %d\n",z,n);
                      z++;
                      continue;
              }
              int count=0,count2[12]={0};
              int flag=-1,j=0;
              for(i=0;i<=100;i++)
              {
                                 while(s[i]>0)
                                 {
                                              if(a>i)
                                              {
                                                     a=a+i;
                                                     count++;
                                                     s[i]--;
                                              }
                                              else
                                              {
                                                  
                                                  b=a;
                                                  while(b<=i)
                                                  {
                                                             b=b+b-1;
                                                             count2[j]++;
                                                  }
                                                  a=b;
                                                  if(count2[j]>n-count)
                                                  {
                                                                    flag=j;
                                                                    break;
                                                  }
                                                  j++;
                                              }
                                 }
                                 if(flag>=0)
                                 break;
              }
              int max=0;
              
              
                  for(i=0;i<j;i++)
                  {
                                   max=max+count2[i];
                  }
                 // cout<<max;
                  max=max+n-count;
                  printf("Case #%d: %d\n",z,max);
                  z++;
                 // cout<<max<<endl;
              
    }
    return 0;
}
                                                  
                                                  
                                                  
