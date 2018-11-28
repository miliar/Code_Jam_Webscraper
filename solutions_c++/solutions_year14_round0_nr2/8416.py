#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <fstream>
#include <ctime>
#define pb push_back
typedef long long int i64;
typedef unsigned long long u64;
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
int T;
vector<long double> answers;
void read()
{
    long double C, F, X;
    long double currentCookiesPerSec = 2;
    long double timePast = 0;
    fin >> C >> F >> X;
    while(1)
    {
        long double timeWhenWaiting = X / currentCookiesPerSec;
        long double timeToBuyFarm = C / (currentCookiesPerSec);
        if(timeWhenWaiting < timeToBuyFarm + X / (currentCookiesPerSec + F))
        {
            timePast += timeWhenWaiting;
            //fout<<"TimeToWait: "<<timeWhenWaiting<<endl;
            break;
        }
        else
        {
            //fout<<"toBuyFarm: "<<timeToBuyFarm<<endl;
            timePast += timeToBuyFarm;
            currentCookiesPerSec += F;
        }
    }
    answers.pb(timePast);
}
int main()
{
    ios::sync_with_stdio(false);
    fin >> T;
    for(int i = 0; i < T; ++i)
    {
        read();
    }
    for(int i = 0; i < T; ++i)
    {
        fout<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<<answers[i]<<"\n";
    }
    return 0;
}
