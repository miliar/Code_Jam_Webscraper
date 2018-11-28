#include<fstream>
#include<math.h>

using namespace std;

int T, A, B;
ifstream f1("C-small-attempt0.in");
ofstream f2("C-small-attempt0.out");

int palindrome(int n)
{
    int nBW=0, number=n;
    while (n!=0)
    {
        nBW=nBW*10+n%10;
        n=n/10;
    }
    if (number==nBW)
        return 1;

    return 0;
}

int is_perfect_square(int n)
{
    int a=(int) sqrt(n);
    if (a*a==n)
        return 1;

    return 0;
}


int main()
{
    f1>>T;

    for (int i=1; i<=T; i++)
    {

        int k=0;
        f1>>A>>B;
        for (int j=A; j<=B; j++)
            if ( palindrome(j) && is_perfect_square(j)
                && palindrome(sqrt(j)) )
                {
                    k++;
                }

        f2<<"Case #"<<i<<": "<<k<<endl;;
    }

    f1.close();
    f2.close();

    return 0;
}

