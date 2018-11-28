#include <iostream>
#include <cmath>
using namespace std;

bool palindromes(int n)
{
    int k=n;
    int rev=0;
    while (k>0)
    {
        rev=rev*10+k%10;
        k/=10;
    }
    if (rev==n)
        return true;
    else
        return false;
}

bool square(int n)
{
    int k=sqrt(n);
    if (k*k==n)
        return true;
    else
        return false;
}

int main()
{
    int t,a,b,cont;
    cin>>t;
    for (int i=0; i<t; i++)
    {
        cin>>a>>b;
        cont=0;
        for (int j=a; j<=b; j++)
        {
            if ((palindromes(j))&&(square(j))&&(palindromes(sqrt(j))))
                cont++;

        }
        cout << "Case #" << i+1<<": "<<cont<<endl;

    }

    return 0;
}
