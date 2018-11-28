//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Dylan Stenico on 12/04/14.
//  Copyright (c) 2014 Dylan Stenico. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

double calcolaFabbriche(int nFabbriche, double cost, double extra, double total);

int main(int argc, const char * argv[])
{
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Cookie Clicker Alpha/B-large.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Cookie Clicker Alpha/B-large.ou.txt");
    output.precision(15);
    int n;
    input >> n;
    cout << n << endl;
    for(int i = 0; i < n; i++)
    {
        cout << i << endl;
        double cost;
        double extra;
        double total;
        input >> cost;
        input >> extra;
        input >> total;

        double lastTime = -1;
        
        for(int i = 0; 1; i++)
        {
            double currentTime = calcolaFabbriche(i, cost, extra, total);
            if(currentTime < lastTime || lastTime == -1)
            {
                lastTime = currentTime;
            }
            else
            {
                break;
            }
        }
        output  << "Case #" << i + 1 << ": " << lastTime << endl;
    }
}

double calcolaFabbriche(int nFabbriche, double cost, double extra, double total)
{
    double time = 0;
    for(int i = 0; i < nFabbriche; i++)
    {
        time += (double)cost/((double)2.0 + (double)((double)i * (double)extra));
    }
    return time + (double)total/(double)(2.0 + (double)nFabbriche * (double)extra);
}
