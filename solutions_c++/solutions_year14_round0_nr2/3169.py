// GCJ 2014 Qualification Round
// problem B

#include <iostream>
#include <cstdio>

using namespace std;

const char input_file[] = "B.in", output_file[] = "B.out";

int main()
{

    FILE *fin = fopen(input_file, "r");
    FILE *fout = fopen(output_file, "w");

    int test_case, test_cur;
    double time_cur, cookies_cur, farm_cur, c, f, x;

    fscanf(fin, "%d", &test_case);

    for (test_cur = 1; test_cur <= test_case; test_cur++)
    {
        fscanf(fin, "%lf%lf%lf", &c, &f, &x);

        time_cur = 0, cookies_cur = 0, farm_cur = 0;

        while (cookies_cur < x)
            if (x <= c)
            {
                time_cur += (x - cookies_cur) / (2 + f * farm_cur);
                break;
            }
            else if (cookies_cur >= c)
            {
                double buy_need_time = (x - (cookies_cur - c)) / (2 + f * (farm_cur + 1));
                double not_buy_need_time = (x - cookies_cur) / (2 + f * farm_cur);

                if (buy_need_time < not_buy_need_time)
                    cookies_cur -=c, farm_cur += 1;
                else
                    time_cur += not_buy_need_time, cookies_cur = x;
            }
            else
            {
                time_cur += (c - cookies_cur) / (2 + f * farm_cur);
                cookies_cur = c;
            }

        fprintf(fout, "Case #%d: %.7f\n", test_cur, time_cur);

    }


    fclose(fin);
    fclose(fout);

    return 0;
}



