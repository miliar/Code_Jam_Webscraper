#include<iostream>
#include<cmath>
using namespace std;


int palindrome(int num)
{
    int  n;
    int digit;
    double rev = 0;
    double root;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);

     if (n == rev)
      { rev=0;
       root=sqrt((double)n);

       if(((double)root-(int)root)!=0)
        return 0;


       num=(int)root;
       n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);

     if (n == rev)
      return 1;

      else return 0;

      }

      else
        return 0;
}




int main()
{
     int t;
     cin>>t;
     for(int data=1;data<=t;data++)
     {


    int a,b;
    int c=0;
    int flag=0;
    cin>>a;
    cin>>b;
    for(int i=a;i<=b;i++)
    {
        flag=palindrome(i);

        if(flag==1)
            c+=1;;

    }

    cout<<"Case #"<<data<<":"<<" "<<c<<endl;
}

}





