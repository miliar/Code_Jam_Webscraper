#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    cout << "Cookies......" << endl;

    FILE* fpIn = fopen("./B-large.in", "r");
    FILE* fpOut = fopen("./B-large.out", "w");

    int nTestCases = 0;
    fscanf(fpIn,"%d", &nTestCases);


    for(int nTestCaseNo = 1;nTestCaseNo <= nTestCases; ++ nTestCaseNo)
    {
        double c = 0.0, f = 0.0, x = 0.0;
        double cookieCount = 2.0;
        fscanf(fpIn,"%lf %lf %lf",&c,&f,&x);
        cout << c << "\t" << f<< "\t" << x <<endl;


        ///while loop
        double time =0.0;
        double bestValue = ((x/cookieCount)+time);
        double nextBestValue = ((c/(cookieCount+f))+((x/(cookieCount+f))+time));
        double previousBestValue = bestValue;
        while(nextBestValue <  bestValue)

        {
            previousBestValue = bestValue;
            time += c/cookieCount;
            cookieCount +=f;
            bestValue = ((x/cookieCount)+time);
            nextBestValue = ((c/(cookieCount+f))+((x/(cookieCount+f))+time));
        ///
        }
        fprintf(fpOut,"Case #%d: %lf\n",nTestCaseNo,previousBestValue);
    }




    fclose(fpIn);
    fclose(fpOut);

    return 0;
}

