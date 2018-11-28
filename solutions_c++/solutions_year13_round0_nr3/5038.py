#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
bool palindrom(int x)
{
    char arr[4];
    int i=0;
    while(x!=0)
    {
        arr[i]=x%10;
        x=x/10;
        i++;
    }
    i--;
    for(int j=0;j<=i/2;j++)
    {
        if(arr[j]!=arr[i-j])
        {
            return false;
        }
    }
    return true;
//    String number=itoa(x);
 //   cout<< number;
}
int main()
{
    ofstream write;
    write.open ("file.out");

    ifstream read("C-small-attempt0.in");
    int t;
    read>> t;
    for(int j=0;j<t;j++)
    {
        int a;
        int b;
        read >> a;
        read >>b;
        int counter=0;
        for(int i=sqrt(a);i<=sqrt(b);i++)
        {
            if(i*i>=a&&palindrom(i)==true&&palindrom(i*i)==true)
            {
                counter++;
            }
        }
        write<<"Case #"<<j+1<<": "<<counter<<endl;
    }
    write.close();
    return 0;
}
