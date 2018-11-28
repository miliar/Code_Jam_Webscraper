#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);

    int T;

    cin >> T;

    for(int testcase = 0;testcase<T;testcase++)
    {
        int musharr[10000];
        int N;
        cin >> N;
        for(int c = 0;c<N;c++)
        {
            cin >> musharr[c];
        }

        int rateforB = 0;
        //method 1
        int totalA = 0;
        for(int c = 0;c<N-1;c++)
        {
            if(musharr[c]-musharr[c+1] > 0)
            {
                totalA = totalA + musharr[c] - musharr[c+1];

                rateforB = max(rateforB,musharr[c]-musharr[c+1]);
            }
        }

        //method 2
        int totalB = 0;
        for(int c = 0;c<N-1;c++)
        {
            totalB = totalB + min(rateforB,musharr[c]);
        }

        cout << "Case #" << testcase+1 << ": " << totalA << " " << totalB << endl;
    }

    return 0;
}
