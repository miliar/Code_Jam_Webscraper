#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <fstream>

using namespace std;

double findAnswer(double cost, double increase, double final)
{
       double curCook = 0, curRate = 2, answer = 0, temp1, temp2;
       bool condition = true;
       while (condition)
       {
             temp1 = (final/curRate);
             //temp1/=curRate;
             temp2 = (cost/curRate);
             //temp2/=curRate;
             temp2 += (final/(curRate + increase));
             if (temp1 < temp2)
             {
                       answer += temp1;
                       condition = false;          
             }
             else
             {
                       temp2 = (cost - curCook);
                       temp2/=curRate;
                       answer += temp2;
                       curRate+=increase;
             }         
       }
       return answer;
}

int main()
{
    int cases;
    double cost, rateIncrease, final, answer;
    ifstream fin ("secondBig.in");
    ofstream fout ("output2Big.txt");
    fin>>cases;
    for (int i=0; i<cases; i++)
    {
        fin>>cost>>rateIncrease>>final;
        answer = findAnswer(cost, rateIncrease, final);
        fout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<answer<<endl;
    }
    return 0;
}
