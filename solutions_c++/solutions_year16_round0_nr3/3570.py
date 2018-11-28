#include<iostream>
#include<cstring>
#include<stdio.h>
#include<vector>
using namespace std;
long long int calculateBaseNvalue(long long int base, long long int num)
{
  long long int value=1;
  long long int b=base;
  for(num>>=1;num>0;num>>=1)
  {
    value+=base*(num&1);
    base*=b;
  }
  return value;
}
int main()
{
  freopen("C-small-attempt0.in","r",stdin);
  freopen("c.txt","w",stdout);
  long long int Count,i,J,j,k,cases,t,n,bound,value;
  vector<int> factors;
  
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    printf("Case #%d:\n", cases);
    cin>>n>>J;
    bound=1<<n;
    Count=0;
    for(i=((1<<(n-1))+1);i<bound;i+=2)
    {
      factors.clear();
      for(j=2;j<=10;j++)
      {
        value=calculateBaseNvalue(j,i);
        for(k=3;k<1000000 && k<value;k+=2)
          if(value % k == 0)
            break;
        if(k>=value || k>=1000000)
          break;
        factors.push_back(k);
      }
      if(factors.size()==9)
      {
        j=i;
        int str[50];
        for(k=0;j>0;k++,j>>=1)
          str[k]=(j&1);
        for(k--;k>=0;k--)
          cout<<str[k];
        for(k=0;k<9;k++)
          cout<<" "<<factors[k];
        cout<<endl;
        Count++;
        if(Count==J)
          break;
      }
    }
  }
}