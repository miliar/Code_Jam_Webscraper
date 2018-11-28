
#include<iostream>
#include<math.h>
using namespace std;
bool palindrome(int n)
{  int digit,rev=0;
int num=n;
     while(num!=0)
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }
          if (n == rev)
       return true;
     else
       return false;
}
bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    //int root(round(sqrt(n)));
    //return n == root * root;
    double m= sqrt(n);
    if(m==int(m)) return true;
    else return false;
}
 bool fair_and_square(int x)
{
    if(is_perfect_square(x) && palindrome(x))
    {
    int square_root=sqrt(x);
    if(palindrome(square_root))
    return true;
    else
    return false;
    }
    return false;
}
int main()
{   int test_cases;
int counter=0;
     cin>>test_cases;
     int num1[100],num2[100];
     for(int l=0;l<test_cases;l++)

     cin >> num1[l]>>num2[l];
     for(int j=0;j<test_cases;j++)
     {
         counter=0;

     for(int i=num1[j];i<=num2[j];i++)
     {
         if(fair_and_square(i))
         counter++;

     }
cout<<"Case #"<<j+1<<": "<<counter<<endl;
     }


    return 0;
}
