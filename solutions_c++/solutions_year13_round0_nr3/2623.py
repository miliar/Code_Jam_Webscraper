#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
bool is_palindrome(long long int A)
{
  long long int rev=0, temp=A;
  while(temp)
  {
    int r=temp%10;
    temp=temp/10;
    rev=rev*10+r;
  }
  return (rev==A);
}
int main()
{
  int T;
  scanf("%d",&T);
  for(int Ti=1;Ti<=T;Ti++)
  {
    int N,M;
    scanf("%d %d",&N,&M);
    long long int itr=(long long int)sqrt(N);
    long long int end=(long long int)sqrt(M);
    //cout<<itr<<" "<<end<<endl;
    long long int ans=0;
    for(long long int i=itr;i<=end;i++ )
    {
      if((i*i>=N) && (i*i<=M) && is_palindrome(i) && is_palindrome(i*i))
      {  ans++;
        //printf("ANS->%lld\n",i);
      }
      
    }
    printf("Case #%d: %lld\n", Ti,ans);
  }
  return 0;
}
