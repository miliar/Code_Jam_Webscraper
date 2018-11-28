#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *in = fopen("input.txt", "rt");
    FILE *out = fopen("output.txt", "wt");
    
    int T = 0;
    double C = 0, F = 0, X = 0;
    double curRate = 2;
    double newRate = 0;
    double newDeficit = 0;
    double timeToNextFarm = 0;
    double curEndTime = 0;
    double newEndTime = 0;
    double acc = 0;
    double timeTaken = 0;

    bool b1 = false;

    fscanf(in, "%d", &T);
    for (int i =0; i < T; i++)
    {
        C = 0, F = 0, X = 0;
        curRate = 2;
        newRate = 0;
        newDeficit = 0;
        timeToNextFarm = 0;
        curEndTime = 0;
        newEndTime = 0;
        acc = 0;
        timeTaken = 0;
        b1 = false;

        fscanf(in, "%lf %lf %lf", &C, &F, &X);
    
        if (!(X > C))
        {
            // No farm needed
            fprintf(out, "Case #%d: %lf\n", i+1, X/curRate);
        }
        else
        {
            timeToNextFarm = C/curRate;
            curEndTime = X/curRate;
            if (!(timeToNextFarm < curEndTime))
            {
                timeTaken = curEndTime;
                b1 = true;
            }
            else
            {
                do
                {
                    timeTaken += timeToNextFarm;
                    newRate = curRate + F;
                    timeToNextFarm = C/newRate;
                    newEndTime = timeTaken + X/newRate;

                    if (newEndTime < curEndTime)
                    {
                        curRate = newRate;
                        curEndTime = newEndTime;
                        timeToNextFarm = C/newRate;
                    }
                    else
                    {
                        b1 = true;
                    }
                } while (!b1);
            }
            fprintf(out, "Case #%d: %lf\n", i+1, curEndTime);
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}