#include<iostream>
using namespace std;

long long int t,n,f,j,m;

int main()
{
    cin >> t;

    for (long long int i = 1; i <= t; ++i)
    {
        f = 0;
        j = 0;

        cin >> n;

        if(n==0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        while (f<((1<<10)-1))
        {
            j++;

            m = j*n;

            while (m>0)
            {
                f |= 1<<(m%10);
                m /= 10;
            }
        }

        cout << "Case #" << i << ": " << j*n << endl;
    }
}
