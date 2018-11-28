#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

ifstream fin;
ofstream fout;
int cases;


void outAns(double ans, int num)
{
    fout<<"Case #"<<num+1<<": ";
    fout<<setprecision(8)<<setiosflags(ios::fixed)<<ans;
    fout<<endl;
}

double calculate(double c, double f, double x)
{
    double t = 0;
    double p = 2.0;
    bool buy = true;
    while (buy)
    {
        t+= c/p;
        double remaining = (x - c) / p;
        double expectation = x / (p + f);
        if (expectation < remaining)
        {
            buy = true;
            p+=f;
        } else
        {
            return t+remaining;
        }
    }
}

int main()
{
    fin.open("B-large.in",ios::in);
    fout.open("output.txt",ios::trunc);
    fin>>cases;
    double c,f,x;
    for (int caseNum=0;caseNum<cases;caseNum++)
    {
        fin>>c>>f>>x;
        if (c >= x)
        {
            outAns(x/2.0, caseNum);
        } else
        {
            double ans = calculate(c,f,x);
            outAns(ans, caseNum);
        }
    }
    fin.close();
    fout.close();
    return 0;
}
