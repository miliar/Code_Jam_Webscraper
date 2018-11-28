#include<iostream>
#include<stdio.h>
#include<algorithm>
#define SIZE 26
using namespace std;
struct node{
  int index,amount;
};
bool myCompare(node a, node b)
{
  if(a.amount > b.amount)
    return true;
  return false;
}
node all[SIZE+3];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.txt","w",stdout);
  int cases,t,i,j,n,sum;
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    cin>>n;
    sum=0;
    for(i=0;i<n;i++)
    {
      cin>>all[i].amount;
      all[i].index=i;
      sum+=all[i].amount;
    }
    printf("Case #%d:", cases);
    while(true)
    {
      if(sum==0)
        break;
      sort(all,all+n,myCompare);
      for(i=0;i<n;i++)
        if(all[i].amount==0)
          break;
      n=i;
      if(sum>1)
      {
        if(all[0].amount>1)
        {
          if((double)(all[0].amount-2)/(double)(sum-2) > 0.5 || (n>1 && (double)all[1].amount/(double)(sum-2) > 0.5))
          {
            all[0].amount--;
            all[1].amount--;
            sum-=2;
            cout<<" "<<(char)('A'+all[0].index)<<(char)('A'+all[1].index);
          }
          else
          {
            all[0].amount--;
            sum--;
            cout<<" "<<(char)('A'+all[0].index);
          }
        }
        else
        {
          for(i=0;i<n;i++)
            if(all[i].amount == 0)
              break;
          if(i%2 == 1)
          {
            cout<<" "<<(char)('A'+all[0].index);
            for(j=1;j<i;j+=2)
              cout<<" "<<(char)('A'+all[j].index)<<(char)('A'+all[j+1].index);
            sum=0;
          }
          else
          {
            for(j=0;j<i;j+=2)
              cout<<" "<<(char)('A'+all[j].index)<<(char)('A'+all[j+1].index);
            sum=0;
          }
        }
      }
    }
    cout<<endl;
  }
  return 0;
}