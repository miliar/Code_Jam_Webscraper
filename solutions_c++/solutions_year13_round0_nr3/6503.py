#include <iostream>

using namespace std;

int lessthan(int n)
{
    if (n<1) return 0;
    else if (n<4) return 1;
    else if (n<9) return 2;
    else if (n<121) return 3;
    else if (n<484) return 4;
    else return 5;
}

void the_case()
{
    int a, b;
    cin >> a >> b;
    cout << lessthan(b)-lessthan(a-1) << endl;
}

int main()
{
    int N, n;
    cin >> N;
    n = N;
    while(n--)
    {
        cout << "Case #" << N-n << ": ";
        the_case();
    }
}
