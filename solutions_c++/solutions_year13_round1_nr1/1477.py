#include <iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    int i=1;
    long long r,t;
    while(i<=T)
    {
        cin >> r >>t;
        long long sum = 0;
        long long count = 0;
        while(sum <= t)
        {
            sum= sum + 2*r+1;
            r+=2;
            count++;
        }

        cout << "Case #" <<i<<": "<<(--count)<<endl;
        i++;
    }
    return 0;
}

