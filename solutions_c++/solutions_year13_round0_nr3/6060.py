#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

bool isPalindrome(long long x)
{
    long long y=0, tmp=x;
    while (tmp!=0)
    {
        y*=10;
        y+=tmp%10;
        tmp/=10;
    }
    return x==y;
}

bool isSquare(long long x)
{
    long long tmp=x, s = sqrt(tmp);
    if (s*s!=x)
        return false;
    return isPalindrome(s);

}

int main()
{
    ios_base::sync_with_stdio(0);

    int testy;
    long long a, b, ile;

    cin>>testy;
    for (int numcase=1; numcase<=testy; numcase++)
    {
        cin>>a>>b;
        ile=0;
        for (long long n=a; n<=b; n++)
            if (isPalindrome(n) && isSquare(n))
                ile++;

        cout<<"Case #"<<numcase<<": "<<ile<<endl;
    }
    return 0;
}
