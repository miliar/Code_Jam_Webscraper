#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

double cost[100005];
double costS[100005];

double C,F,X;

double getAns(int k)
{
    double ans = X+k*C+F*costS[k-1];
    ans /= 2.0 + F*k;
    return ans;
}

int main()
{
    int t,tt,i;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>C>>F>>X;
        cost[0] = C/2.0;
        costS[0] = cost[0];
        for(i=1; i<=100000; ++i)
        {
            cost[i] = cost[i-1] + (C/(2.0 + i*F));
            costS[i] = costS[i-1] + cost[i];
        }

        double ans = X/2.0;
        double newAns;

        for(i=1; i<=100000; ++i)
        {
            newAns = getAns(i);
            if(newAns > ans)
                break;
            ans = newAns;
        }
        fout << "Case #" << t << ": ";
        fout.precision(10);
        fout << ans << endl;
    }
    return 0;
}

