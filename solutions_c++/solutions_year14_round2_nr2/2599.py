#include<iostream>
using namespace std;

int main()
{
    long long A,B,K;
    int T;

    long long count;

    cin >> T;

    for(int i=0; i<T; ++i)
    {
        cin >> A >> B >> K;
        count = 0;

        for(long long j=0; j<A; ++j)
        {
            for(long long k=0; k<B; ++k)
            {
                if((j&k) < K)
                    ++count;
            }
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
