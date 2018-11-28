#include<iostream>
#include<cstdio>

using namespace std;

void findDigits(int n, int array[10])
{
    do
    {
        int digit = n % 10;
        array[digit] = 1;
        n /= 10;
    }
    while (n > 0);
}

int checkDigits(int numb, int arr[], int i)
{

    findDigits(numb, arr);
    int count = 0;
    for(int i = 0; i < 10; i++)
    {
        if(arr[i] == 1)
            count++;
    }
    if(count == 10)
    {
        cout<<"Case #"<<(i+1)<<": "<<numb<<"\n";
        return 1;
    }
    return 0;

}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T;
    cin>>T;

    for (int i = 0; i < T ; i++)
    {
        int array[10] = {0};
        int number;
        cin>>number;
        int new_number = number;
        checkDigits(new_number, array, -1);
        int loop = 1;
        while(loop)
        {
            new_number += number;

            if(new_number == number)
            {
                cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<"\n";
                break;
            }
            if(checkDigits(new_number, array, i))
                break;
        }
    }
}
