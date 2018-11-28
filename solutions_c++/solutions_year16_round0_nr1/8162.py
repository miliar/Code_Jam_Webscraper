#include <iostream>
#include <vector>
using namespace std;
int arr[10];
bool AreAllDigitsSeen()
{
    int i;
    for ( i=0; i < 10; i++)
    {
        if (arr[i] == 0)
        {
            return false;
        }
    }
    return true;
}

void Markthedigit(int n)
{
    while( n > 0)
    {
        int val = n%10;
        arr[val] = 1;
        n = n/10;

    }

}

int main()
{
 int t;
 cin>>t;
 int value = t;
 while(value--)
 {
     int val;
     int n;
     cin>>n;
     if (n == 0)
     {
         cout<<"Case #"<<t - value<<": "<<"INSOMNIA"<<endl;
     }
     else
     {

        int i;
        for( i =0; i<10; i++)
        {

            arr[i] = 0;
        }
        for ( i = 1; AreAllDigitsSeen() == false; i++)
        {
            val = i *n;
            Markthedigit(i * n);
        }
        cout<<"Case #"<<t - value<<": "<<val<<endl;
     }
  }
}
