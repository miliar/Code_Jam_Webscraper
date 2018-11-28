#include <iostream>
#include <algorithm>
#include <string>
#include <list>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std;

int determine(double cost, double rate, double extra, double win);
double timeSum(double cost, double rate, double extra, double win, int k);

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");

    int numCases = 0;
    fin >> numCases;
    double cost = 0;
    double extra = 0;
    double win = 0;
    double time = 0;
    double rate = 2;
    double extraTime = 0;
    int k = 0;
    bool eat = true;
    for(int i = 0; i < numCases; i++)
    {
        fin >> cost;
        fin >> extra;
        fin >> win;
        while(eat)
        {
            if(win / rate > (cost / rate) + (win / (rate + extra))) // if stopping now is definitely bad
            {
                time = time + cost/rate;
                rate = rate + extra;
            }
            else
            {
                k = determine(cost, rate, extra, win);
                extraTime = timeSum(cost, rate, extra, win, k);
                {
                    fout << "Case #" << i + 1 << ": " << setprecision(12) << time + extraTime << endl;
                    eat = false;
                }
            }
        }
        rate = 2;
        eat = true;
        time = 0;
    }
    return 0;
}

int determine(double cost, double rate, double extra, double win)
{
    double sum = cost / rate;
    int k = 0;
    while(k < 100)
    {
        if(win/rate < sum)
        {
            return k;
        }
        k++;
        sum = sum + cost/(rate + k*extra);
    }
    return k;
}

double timeSum(double cost, double rate, double extra, double win, int k)
{
    double time = win/(rate);
    double temp = 0;
    for(int i = 0; i <= k; i++)
    {
        temp = temp + cost/(rate + i*extra);
        if(temp + win/(rate + (i+1)*extra) < time)
        {
            time = temp + win/(rate + (i+1)*extra);
        }
    }
    return time;

}
