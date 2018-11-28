#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <math.h> 
#include <assert.h>
#include <utility>


using namespace std;

#define ll long long
#define ui unsigned int
#define debug(a) cout << #a << ": " << a << endl;
#define debugVector(a) cout << #a << ": "; for(ui i; i < a.size(); i++) {cout << a[i] << " ";} cout << endl;
#define pb(a) push_back(a)
#define case(i) fOut << "Case #" << (i) << ": "; cout << "Case #" << (i) << endl;

bool myfunction (int i,int j) { return (j<i); }

int solve(int test, int d, int* plates) {
    sort(plates, plates + d, myfunction);
	//shyness, 
    int timeToFinish = plates[0];
	//while (!)
    for (int i = 2; i < timeToFinish; i++) {
        //to finish in i timesteps
        for (int splits = 1; splits < (i-1); splits++) {
            int timeLeft = i - splits;
            int splitsLeft = splits;
        //either split 1 time finish in i-1
        //split 2 finish i-2
            //possible?
            for (int k = 0; k < d; k++) {
                if (plates[k] <= timeLeft) {
                    return i;
                }

                if (splitsLeft <= 0) break;
                 //if (i==3) cout << "timeLeft " << timeLeft << endl;

                //else use splits
                int splitFound = 0;
                for (int di = 2; (di-1) <= splitsLeft; di++) {
                    float r = (float) plates[k] / (float) di;
                    //if (i==3 && test == 99) cout << "r " << r << endl;
                    if (r <= (float) timeLeft + 0.000001) {
                        splitsLeft -= (di-1);
                        if (k == (d-1)) return i;
                        splitFound++;
                        break;
                    }
                }
                if (splitFound == 0) {
                    break;
                }

            }


        }
    }

	return timeToFinish;
}


int main()
{
    ui tests; cin >> tests;
    int d;
    int* plates = (int*) malloc(3000 * sizeof(int));
    for (ui t = 0; t < tests; t++) {
    	cin >> d;
    	for (int i = 0; i < d; i++) {
    		cin >> plates[i];
    	}

    	cout << "Case #" << (t+1) << ": " << solve(t, d, plates) << endl;


    }

    
 

}
