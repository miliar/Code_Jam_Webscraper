#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<cstdio>
#include<cstring>
using namespace std;

int findpos(char a[10000],int n)
{
    int i;
    for(i=n-1;i>=0;i--)
      if(a[i]=='-')
     return i;
    return -1;
}
void swap(char a[],int j)
{
    int i;
    for(i=0;i<=j;i++)
    {
        if(a[i]=='+')
        a[i]='-';
        else
        a[i]='+';
    }
}
int main()
{
  int i,n,t,k,sum;
  long long count;
  char a[100005];
  cin>>t;
  for(k=1;k<=t;k++)
  {
      cin>>a;
      count=0;
      n=strlen(a);
      while(findpos(a,n)!=-1)
      {
          count++;
          i=findpos(a,n);
          swap(a,i);
      }
      cout<<"Case #"<<k<<": "<<count<<endl;
  }
  
} 