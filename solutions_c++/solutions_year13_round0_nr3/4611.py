#include<iostream>
#include<stdio.h>
#include <math.h>

using namespace std;
bool checkPalindrome(long long int num)
{
    long long int n,digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);

     if (rev==n)
       return true;
     else
       return false;
}
int checkFandS(long long int x)
{
    if(checkPalindrome(x))
    {
        long long int y = sqrt(x);
        if(checkPalindrome(y))
            return 1;
        else
            return 0;
    }
    else
        return 0;

}

int main()
{

     freopen("C-small-attempt0.in","rt",stdin);
    freopen("op2.txt","wt",stdout);
    long long int T,l,h;

    cin>>T;
    long long int count = 0;
    long long int m = 0;
    while(m<T)
    {
        count = 0;
        cin>>l;
        cin>>h;
        for(int i=l;i<=h;i++)
        {
            if (sqrt(i)==floor(sqrt(i)))
            {
                    if(checkFandS(i))
                        count++;

            }

        }

        cout<<"Case #"<<m+1<<": "<<count<<endl;
        m++;
    }


    return 0;
}
