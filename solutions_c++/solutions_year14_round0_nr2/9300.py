#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    FILE* reader = fopen("input.txt", "r");
    FILE* printer = fopen("output.txt", "w");
    int T;
    fscanf(reader, "%d", &T);

    for(int i=1; i<=T; i++)
    {
        double C, F, X;
        fscanf(reader, "%lf %lf %lf", &C, &F, &X);
        //printf("%lf %lf %lf\n", C, F, X);
        double time = 0;
        double rate = 2;
        double to_finish;
        double to_farm;
        double to_farm_and_finish;

        while(true)
        {
            to_finish = X / rate;
            to_farm = C / rate;
            to_farm_and_finish = to_farm + X / (rate + F);

            if(to_farm_and_finish < to_finish)
            {
                time += to_farm;
                rate += F;
            } else
            {
                time += to_finish;
                fprintf(printer, "Case #%d: %.7lf\n", i, time);
                break;
            }
        }

    }
    return 0;
}
