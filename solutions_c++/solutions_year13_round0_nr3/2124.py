#include <cstdio>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;

const int pw = 15;

int d_num[pw];
int d_sq[pw];

int main()
{
    int case_namber;
    cin >> case_namber;

    for(int current = 1; current <= case_namber; ++current)
    {
        long long int up_bound;
        long long int down_bound;

        cin >> down_bound;
        cin >> up_bound;

        int counter = 0;

        for(int i = down_bound; i <= up_bound; ++i)
        {
            long long int number = i;
            bool p_num = true;

            for(int j = 0; j < pw; ++j)
            {
                d_num[j] = number % 10;
                number /= 10;
            }

            //number
            int last = pw - 1;
            while(d_num[last] == 0) { --last; }
            if(last > 0)
            {
                for(int k = 0; k < (last+1)/2; ++k)
                {
                    if(d_num[k] != d_num[last-k])
                    {
                        p_num = false;
                        break;
                    }
                }
            }

            if(!p_num) continue;

            double d_sqrt = sqrt(double(i));
            long long int i_sqrt = floor(d_sqrt);
            if(i_sqrt*i_sqrt != i)
            {
                ++i_sqrt;
                if(i_sqrt*i_sqrt != i) continue;
            }

            bool p_sqrt = true;

            for(int j = 0; j < pw; ++j)
            {
                d_sq[j] = i_sqrt % 10;
                i_sqrt /= 10;
            }

            last = pw - 1;
            while(d_sq[last] == 0) { --last; }
            if(last > 0)
            {
                for(int k = 0; k < (last+1)/2; ++k)
                {
                    if(d_sq[k] != d_sq[last-k])
                    {
                        p_sqrt = false;
                        break;
                    }
                }
            }

            if(p_sqrt) ++counter;
        }

        cout << "Case #" << current << ": ";
        cout << counter;
        cout << endl;
    }
    return 0;
}
