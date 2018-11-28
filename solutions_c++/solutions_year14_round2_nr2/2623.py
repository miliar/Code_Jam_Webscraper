#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <hash_map>
using namespace std;
int T, A, B, K;
int main()
{
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        long count = 0;
        cin >> A >> B >> K;
        for (int j = 0; j < A; ++j)
        {
            for (int k = 0; k < B; ++k)
            {
                int temp = j&k;
                if (temp < K)
                {
                    count++;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }

    return 0;
}