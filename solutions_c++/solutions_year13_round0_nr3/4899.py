#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;
bool ispalindrome (int num)
{
    if (num/10==0)
        return true;
     int n, digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if (n == rev)
       return true;
     else
      return false ;


}
main()
{

    int T,A,B;
    cin>>T;
    int cnt;
    for(int v=1;v<=T;v++)
    {
        cin>>A>>B;
        cnt=0;
        for(int i=A;i<=B;i++)
        {
            if(ispalindrome(i))
            if(((int)sqrt(i))*((int)sqrt(i))==i)
            if (ispalindrome((int)sqrt (i)))
                cnt++;
        }
        printf("Case #%d: %d\n",v,cnt);
    }


    return 0;
}
