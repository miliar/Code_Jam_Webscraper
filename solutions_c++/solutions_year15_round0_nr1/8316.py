#include <algorithm>
#include <iostream>

using namespace std;

#define CERR(x) { std::cerr << #x << " = " << (x) << "\n";  }

void solve(const size_t t)
{
	size_t smax = 0, result = 0;

	cin >> smax;
    //CERR(smax);
	char c;
    size_t sum = 0;
    size_t n = 0;

	for (size_t s = 0; s <= smax; ++s)
	{
        cin >> c;
        n = c - '0';
        //CERR(n);
        const size_t needed = s; // needed people
        //CERR(needed);

        if (needed > sum)
        {
            // invite people
            size_t diff = needed - sum;
            //CERR(diff);
            result += diff;
            sum += diff;
        }

        sum += n;
        //CERR(sum);
	}

    cout << "Case #" << t << ": " << result << "\n";
}

int main()
{
	size_t T = 0;
    cin >> T;
    //CERR(T);

    for (size_t t = 0; t < T; ++t)
    {
        solve(t + 1);
    }

    return 0;
}
