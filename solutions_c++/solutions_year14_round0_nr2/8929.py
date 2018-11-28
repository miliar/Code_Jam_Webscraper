#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <iterator>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ifstream file("test.inp", ifstream::in);
    if (!file) {
            string error_message = "No valid input file was given, please check the given filename.";
            cout << error_message;
        }
        string line;
        //getline(file, line);
        int count;
        double c, f, x;
        cout.precision(15);
        file >> count;
        //cout << count << endl;

        double rTime1, rTime2;
        double score, timeSpent;
        bool finished;
        double rate;

        for(int i=1; i<=count; i++)
        {
            file >> c >> f >> x;
            //cout << "c: " << c << ", f: " << f << ", x: " << x << endl;

            score = 0.0d;
            timeSpent = 0.0d;
            finished = false;
            rate = 2.0d;

            rTime1 = x/rate;
            rTime2 = (x+(c/rate))/(rate+f);
            double d1 = c/rate + x;
            //cout << d1 << ", " << (rate+f) << endl;

            //cout << "x: " << x << ", rate: " << rate << ", time1: " << rTime1 << ", time2: " << rTime2 << endl;

            if(rTime1<rTime2)
            {
                timeSpent += (x-score)/rate;
                finished = true;
            }

            while (!finished)
            {
                rTime1 = (x-score)/rate;
                rTime2 = (c-score)/rate+x/(rate+f);
                if(rTime1<rTime2)
                {
                    timeSpent += (x-score)/rate;
                    finished = true;
                }
                else
                {
                    timeSpent += (c-score)/rate;
                    score = 0;
                    rate+=f;
                }
            }
            cout << "Case #" << i << ": " << timeSpent << endl;
        	
        }
	return 0;
}
