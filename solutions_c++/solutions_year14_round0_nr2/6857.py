#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>

void
get_cols(char *buf, double *vals)
{
    char *ptr = buf;
    char *p2;
    int c = 0;
    while ((p2 = strchr(ptr, ' ')) != NULL)
    {
        *p2 = '\0';
        double val = atof(ptr);
        vals[c] = val;
        c++;
        ptr = p2+1;
    }

    double val = atof(ptr);
    vals[c] = val;
}

double 
interpolate_linear(double x, double x1, double y1, double x2, double y2)
{
	if (x1 != x2)
	{
	    double lambda = (x2 - x) / (x2 - x1);
	    double y = y1 * lambda + y2 * (1.0-lambda); 
	    return y;
	}
	else
	{
		return y1;
	}
}

double
calc(double C, double F, double X, int num_farms)
{
    double prod_rate = 2.0; // per second
    double ttl_secs = 0.0;

    for (int farm = 0; farm < num_farms; farm++)
    {
        double secs = C / prod_rate;
        double cookies_made = prod_rate * secs;

        if (cookies_made > X)
        {
            // interpolate
            double x1 = 0;
            double x2 = cookies_made;
            double x = X;

            double y1 = ttl_secs;
            double y2 = ttl_secs + secs;

            double y = interpolate_linear(x, x1, y1, x2, y2);

            return y;
        }
        else if (cookies_made == X)
            return ttl_secs + secs;

        ttl_secs += secs;
        prod_rate += F;
    }

    return ttl_secs + (X / prod_rate);
}

double
calc_min(double C, double F, double X)
{
    double minval = calc(C, F, X, 0);
    int i = 1;
    for ( ; true; i++)
    {
        double v = calc(C, F, X, i);
        if (v >= minval)
            return minval;
        minval = v;
    }
}

int
main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <input.txt>\n", argv[0]);
        return 0;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f)
    {
        printf("Couldn't open file\n");
        return 0;
    }

    char buf[10001];
    fgets(buf, 10001, f);
    int num_tests = atoi(buf);

    //printf("Got %d tests\n", num_tests);

    for (int test_num = 0; test_num < num_tests; test_num++)
    {
        fgets(buf, 10001, f);
        double vals[6];
        get_cols(buf, vals);

        double C = vals[0];
        double F = vals[1];
        double X = vals[2];

        double v = calc_min(C, F, X);
        printf("Case #%d: %0.7f\n", test_num+1, v);
        
    }

    fclose(f);

    return 0;
}
