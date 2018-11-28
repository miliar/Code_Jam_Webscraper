#include <iostream>
#include <string>
#include <cmath>

using namespace std;

main()
{
    unsigned long long t;
    cin >> t;
    for (unsigned long long i =1ULL; i < t+1; i++)
    {   
        unsigned long long r,tp;
        cin >> r >> tp;

        unsigned long long c = 0ULL;
        unsigned long long n = sqrt(tp);

        unsigned long long min = 0ULL;
        unsigned long long max = n;

        bool found = false;

        while (!found)

        {

            unsigned long long mid = (min + max ) /2;
            if (min == mid)
                found = true;
            else
            {
                if ((1 + 2 * r + 2 * (mid -1)) < tp/mid)
                {
                    min = mid;
                }
                else 
                {
                    if ((1 + 2 * r + 2 * (mid -1)) > tp/mid)
                    {
                        max = mid;
                    }
                    else
                    {
                        min = mid;
                        found = true;
                    }
                }
            }

        }





        cout << "Case #" << i << ": ";

        cout << min;

        cout << endl;
    }
}
