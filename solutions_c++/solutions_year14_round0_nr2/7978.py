#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    int T=0,casen =1;
    cin >> T;

    double C,F,X;
    while(T--)
    {
        cout << "Case #" << (casen++) << ": ";
        cin >> C >> F >> X;
        double mingoal = X/2.0;
        double speed   = 2.0 +F;
        double totalfarmcost = C/2.0;
        double newmin = totalfarmcost + X/speed;
        
        while(newmin < mingoal)
        {
            mingoal = newmin;
            totalfarmcost += C/speed;
            speed += F;

            newmin = totalfarmcost + X/speed;


        }
        cout << std::fixed <<  std::setprecision(7) <<  mingoal << endl;
    }
}
