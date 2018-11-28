#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    double time=0;
    double cpt;
    double cost;
    double goal;
    double bonus;
    int tests;
    cin >> tests;


    for(int i=0; i<tests; i++)
    {
        bool test=true;
        cpt=2.0000000;
        time =0.0000000;
        cin >> cost;
        cin >> bonus;
        cin >> goal;
        double to_goal=goal/cpt;
        while(test)
        { //cout << to_goal << "\t" << time <<
            if(to_goal<=((cost/cpt)+goal/(cpt+bonus)))
            {
                test=false;
                time+=to_goal;
            }
            else
            {
                time+=cost/cpt;
                cpt+=bonus;
                to_goal=goal/cpt;
            }
        }
        printf("Case #%d: %.7f\n", i+1, time);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
