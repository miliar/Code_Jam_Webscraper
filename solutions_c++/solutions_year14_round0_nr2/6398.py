#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    FILE *ifp, *ofp;
    char outputFilename[] = "abcde.txt";
    ofp = fopen(outputFilename, "w");
    int test;
    cin>>test;
    int cnt=1;
    double c, f, X;
    while (test--){
        cin>>c>>f>>X;
       // double tot=0;
        //int prev=0;
        double k=2;
        double time = 0.0;
        //long long total = 0;
        while(1) {
               double t = X/k;

               if ( t <=  (c / k + (X) / ( f + k)) ){
                    time += t;
                    break;
                }

                //total = 0;
                time += c / k;
                k += f;
        }
        fprintf(ofp, "Case #%d: ",cnt++);
        fprintf(ofp, "%.7f\n",time);
        //printf("%.7f\n",time);
        //cout << std::setprecision(7) << time << "\n";

    }

    return 0;
}
