#include <iostream>
#include <math.h>
using namespace std;

long long int pow10(int n)
{
    long long int result=1;

    for(int i=0; i<n; i++)
    {
        result = result*10;
    }

    return result;
}

bool palindrome(long long int x)
{
    if(x < 10) return true;

    long long int powup = pow10((int)log10(x) + 1);
    long long int powdown = 10;

    //cout <<powdown << "&" << powup <<endl;

    do
    {
        //cout << x << ": " <<  x%powdown - x%(powdown/10)<< ", " << (x%powup - x%(powup/10))/(powup/10) << endl;

        if(x%powdown - x%(powdown/10) == (x%powup - x%(powup/10))/(powup/10))
        {

            powdown *= 10;
            powup /= 10;
            continue;
        }
        else return false;
    }
    while(powdown < powup);

    return true;
}

int countfs(long long int a, long long int b)
{
    int cnt = 0;

    for(long long int i = (int)sqrt(a-1) + 1; i <= (int)sqrt(b-1) + 1; i++)
    {
        if(i*i > b) break;
        //cout << i << " ";
        if(palindrome(i) && palindrome(i*i)) cnt++;
    }

    return cnt;
}

int main()
{
    int T;
    cin >> T;

    long long int A, B;

    for(int i=0; i<T; i++)
    {
        cin >> A >> B;

        cout << "Case #" << i+1 << ": " << countfs(A, B) << endl;

    }

}
