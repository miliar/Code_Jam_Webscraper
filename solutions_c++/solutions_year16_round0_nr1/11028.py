
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isComplete(int a[])
{
    for(int i=0;i<10;i++)
    {
       if(a[i]==0)
       {
           return false;
       }
    }
    return true;
}

int Bleatrix(long int number)
{
    int arr[10];
    for(int i=0;i<10;i++)
    {
        arr[i]=0;
    }

    int j=1;
    long int num=number,fin;
    while(!isComplete(arr))
    {
        num=number*j;
        fin=num;
        do
        {
            arr[num%10]++;
            num=num/10;
        }while(num!=0);
        j++;
    }
    return fin ;
}

int main() {
    int Test;
    long int Number ;
    cin >> Test ;
    for(int i=1;i<=Test;i++)
    {
        cin >> Number ;
        if(Number==0)
        {
           cout << "Case #"<<i<<": INSOMNIA" << endl ;
        }
        else
        {
           cout<<"Case #"<<i<<": "<<Bleatrix(Number)<<endl;
        }

    }

	return 0;
}
