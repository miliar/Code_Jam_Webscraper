#include <iostream>

using namespace std;
#define OK 0x03FF

#ifdef SMALL
#define MY_INT unsigned int
#else
#define MY_INT unsigned long long
#endif

void check(int n)
{
    if( n == 0 )
    {
        cout << "INSOMNIA\n";
        return;
    }

    int numbers = 0;
    MY_INT N = n;
    bool is_insomnia = false;
    while( !is_insomnia && numbers != OK )
    {
        MY_INT K = N;
        while( K > 0 && numbers != OK )
        {
            int q = K % 10;
            numbers |= 1 << q;
            K /= 10;
        }
        if( numbers == OK )
        {
            cout << N << std::endl;
            return;
        }
        N += n;
        if( N <= n ) is_insomnia = true;
    }
    cout << "INSOMNIA\n";
}

int main()
{
    int t,n;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        cin >> n;
        check(n);
    }
}
