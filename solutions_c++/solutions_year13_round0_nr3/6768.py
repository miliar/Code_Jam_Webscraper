#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;

bool isPalindrome(long long x, char input[])
{
    int head, tail;
    long long  temp = 1;

    memset(input, '\0', sizeof(input));
    for(int i=0; i<7; i++)
        temp *= 10;

    int a = x/temp;
    int b = x%temp;

    if(0 != a)
        itoa(a, input, 10);
    itoa(b, input+strlen(input), 10);
    head = 0;
    tail = strlen(input)-1;

    while(head<=tail)
    {
        if(input[head] != input[tail])
            return false;
        head++;
        tail--;
    }
    return true;
}

bool isSquare(long long x)
{
    char input[15];
    long long root = (long long)sqrt(double(x));
    if(x==root*root && isPalindrome(root, input))
        return true;
    else
        return false;
}

int main()
{
    int T, NO=0, num;
    long long A, B;
    char input[15];
    ifstream in("C-small-attempt1.in");
    ofstream out("C-small-attempt1_out.in");

    in>>T;
    while(T--)
    {
        NO++;
        num = 0;
        in>>A>>B;
        for(long long i=A; i<=B; i++)
        {
            if(isPalindrome(i, input) && isSquare(i))
                num++;
        }

        out<<"Case #"<<NO<<": "<<num<<endl;
    }
    in.close();
    out.close();
    return 0;
}
