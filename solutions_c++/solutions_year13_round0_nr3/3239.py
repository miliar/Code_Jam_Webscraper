#include <cstdio>
using namespace std;

unsigned long long int fns[1000000],sqr,k,m,n,i,a,b;
char str[300];
int t,cas=1,p;
unsigned long int j=0,totGen=0,numOfNos;

bool isPalindrome(unsigned long long sqr)
{
    
    k=0;
    while(sqr)
    {
      str[k++]=sqr%10;
      sqr/=10;
    }
    
    
    for(m=0,n=k-1;m<k/2;m++,n--)
      if(str[m]!=str[n])
        break;
    if(m>=n)
      return true;
    else 
      return false;
      
}
void gen()
{
  for(i=1;i<50000000;i++)
  {
    
    
    if(isPalindrome(i)&&isPalindrome(i*i))
      fns[totGen++]=i*i;
  }
      
    
}
  
int main()
{
  gen();
  
  scanf("%d",&t);
  p=t;
  while(p--)
  {
    
    if(cas<=t&&cas>1)
      printf("\n");
    
    scanf("%lld %lld",&a,&b);
    j=0;
    while(a>fns[j])j++;
    numOfNos=0;
    for(;fns[j]<=b;j++)
      numOfNos++;
	printf("Case #%d: %lld",cas++,numOfNos);    
  }
    
  return 0;
}	