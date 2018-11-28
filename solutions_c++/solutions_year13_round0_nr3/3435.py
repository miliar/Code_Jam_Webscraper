#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int gao(long long tmp)
{
    int a[100], len = 0;
    while (tmp)
    {
        a[len++] = tmp%10;
        tmp /= 10;
    }
    for (int i = 0; i < len; i++)
        if (a[i] != a[len-1-i]) return 0;
    return 1;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, n;
    cin>>T;
    for (int Case = 1; Case <= T; Case++)
    {
        long long A, B;
        cin>>A>>B;
        cout<<"Case #"<<Case<<": ";

        int cnt = 0;
        long long k = 1;
        while (k*k <= B)
        {
            long long tmp = k*k;
            k++;
            if (tmp < A || !gao(k-1)) continue;

            if (gao(tmp)) cnt++;
        }
        cout<<cnt<<endl;
    }
    return 0;
}
