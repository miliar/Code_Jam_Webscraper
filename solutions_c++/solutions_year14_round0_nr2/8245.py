#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    cin>>T;
    double C,F,X;

    for(int step=1; step<=T; step++){

        cin>>C>>F>>X;


        double targ = X;

        double cur = 0;

        double rate = 2;

        double best = -1;

        double timeToX, timeToC;

        while(true){

            timeToX = targ/rate;

            if(best < 0 || cur+timeToX < best){

                best = cur+timeToX ;
            }

            if(cur > best){

                break;
            }


            timeToC = C/rate;

            cur += timeToC;

            targ = X;

            rate += F;


        }
        cout << std::fixed;
        cout<<"Case #"<<step<<": "<<setprecision(7)<<best<<endl;
    }
}

