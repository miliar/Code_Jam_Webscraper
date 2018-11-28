#include<cstdio>
#include<iostream>
using namespace std;
bool check(char a);
int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
              long long x=0,count=0,ans=0,temp=0,con=0,left=0;
              long long n;
              string s;
              cin>>s>>n;
              long long k=s.length();
              for(int i=0;i<k;i++)
              {
                      if(check(s[i]))count++;
                      else count =0;
                      if(count>=n)left=i-n+2;
                      /*if(count>=n)
                      {
                                  a[x][0]=1;
                                  a[x][1]=i-n+2;
                                  a[x][2]=k-i;
                                  temp=x;
                                  x++;
                                  for(int j=0;j<temp;j++)
                                  {
                                          a[x][0]=-a[j][0];
                                          a[x][1]=a[j][1];
                                          a[x][2]=a[temp][2];
                                          x++;
                                  }cout<<"aman\n"<<count;
                                  
                      }*/
                      ans=ans+left;
              }
              printf("Case #%d: %lld\n",z,ans);
    }
}
bool check(char a)
{
     if(a!='a'&&a!='e'&&a!='i'&&a!='o'&&a!='u')
     return true;
     else return false;
}
     
    
