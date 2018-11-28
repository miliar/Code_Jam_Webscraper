#include <iostream>
using namespace std;

int main()
{
    int t2;
    cin >> t2;
    for(int index = 1; index <= t2; ++index)
    {
        double c, f, x;
        cin >> c >> f >> x;

        double res = x / 2;

        double output = 2;
        double t      = 0;
        while(true)
        {
            t = t + c / output;
            output += f;

            double newres = x / output;

            if(res < newres + t)
            {
                break;
            }
            else
            {
                res = newres + t;
            }
        }

        printf("Case #%d: %.7lf\n", index, res);
    }
}
