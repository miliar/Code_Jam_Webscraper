#include <iostream>
#include <math.h>

int ispali(unsigned long long n);
int issquare(unsigned long long n);

int main()
{
    unsigned long long tot = 0;
    unsigned long long counter = 0;
    unsigned long long counter2 = 0;
    unsigned long long A = 0;
    unsigned long long B = 0;
    unsigned long long i = 0;
  //  std::cout << ispali(1765571);
    std::cin >> tot;

    while(counter < tot)
    {
        counter2 = 0;
        std::cin >> A;
        std::cin >> B;
        i = A;
        while(i <= B)
        {
            if(ispali(i) == 1 && issquare(i) == 1 && ispali(sqrt(i)) == 1)
                counter2++;
            i++;
        }
        std::cout << "Case #" << counter + 1 << ": " << counter2 << "\n";
        counter++;
    }
    return 0;
}

int ispali(unsigned long long n)
{
    if(n==1)
        return 1;
    int i = 0;
    int length = 0;
    int temp = n;
    int array[14];

    for(i=0;i<14;i++)
        array[i] = 0;

    i = 0;
    while(pow(10,i)<=n)
        i++;
    length = i;
    i = 0;

    for(i=0;i<length;i++)
    {
        temp = n%10;
        n = (n-temp)/10;
        array[i] = temp;
    }

    for(i=0;i<length/2;i++)
    {
        if(array[i] == array[length-i-1])
            i++;
        else
            return 0;
    }
    return 1;
}

int issquare(unsigned long long n)
{
    unsigned long long i;
    i = sqrt(n);
    if(i*i == n)
        return 1;
    else
        return 0;
}
