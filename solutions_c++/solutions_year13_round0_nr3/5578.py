#include<iostream>
#include<cmath>
#define ULL long long
#define isSQR(x) (sqrt(x)*sqrt(x))
using namespace std;
ULL countFairNumbers(ULL,ULL);
bool checkPalindrome(ULL);
int main()
{
int T;
cin>>T;
int a,b;
    for(int i=0 ; i<T ;i++)
    {
      cin>>a>>b;
      cout<<"Case #"<<(i+1)<<": "<<countFairNumbers(a,b)<<endl;
    }
return 0;
}

ULL countFairNumbers(ULL a,ULL b)
{
    ULL i=a;
    ULL count=0;
    for(;i<=b;i++)
    {
       if(isSQR(i)==i)
       {
         if(checkPalindrome(sqrt(i)))
          {
            if(checkPalindrome(i))
             {
                 count++;
             }
          }
       }
    }
return count;
}

bool checkPalindrome(ULL num)
{
ULL ret=0,tmp=num;
  while(num!=0)
  {
    ret=ret*10+(num%10);
    num=num/10;
  }

  if(tmp==ret)
    return true;
return false;
}
