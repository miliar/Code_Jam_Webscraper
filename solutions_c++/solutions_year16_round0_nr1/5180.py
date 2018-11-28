#include <iostream>

using namespace std;

long long solved(long long n)
{
    int check [10];
    int count = 0;
    for (int i = 0; i < 10; ++i) {
        check[i] = 0;
    }

    for (long long d = 1; d < 10000; ++d) {
        long long tmp = n*d;
        while (tmp > 0) {
            if (check[tmp%10] == 0) {
                ++count;
                check[tmp%10] = 1;
            }

            tmp /= 10;
        }

        if (count == 10) {
            return n*d;
        }
    }

    return -1;
}

int main()
{
    int t;
    long long n;
    cin>>t;

    for (int i = 1; i <= t; ++i) {
        cin>>n;
        cout<<"Case #"<<i<<": ";
        long long res = solved(n);
        if (res == -1) {
            cout<<"INSOMNIA"<<endl;
        } else {
            cout<<res<<endl;
        }
    }
    return 0;
}
