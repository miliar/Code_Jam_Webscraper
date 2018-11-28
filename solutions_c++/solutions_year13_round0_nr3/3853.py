#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool is_palindrome(int N)
{
    int aux=N;
    int rev=0;
    while (aux>0)
    {
        rev=10*rev+aux%10;
        aux/=10;
    }
    return rev==N;
}

int alg(int A, int B)
{
    int ammount=0;
    int a=ceil(sqrt(A)), b=floor(sqrt(B));
    for (int i=a; i<=b; ++i)
        if (is_palindrome(i*i)&&is_palindrome(i))
            ++ammount;
    return ammount;
}

int main()
{
    int T;
    long long A, B;
    ifstream in("C-small-attempt0.in");
    ofstream out("C-small-attempt0.out");
    in >> T;
    for (int i=1; i<=T; i++)
    {
        in >> A >> B;
        out << "Case #" << i << ": " << alg(A, B) << endl;
    }
    return 0;
}
