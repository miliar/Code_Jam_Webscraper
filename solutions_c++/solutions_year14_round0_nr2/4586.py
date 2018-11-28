#include <iostream>
#include <iomanip>
using namespace std;

int main()
{

    int T;
    cin >> T;
    double C, F, X;
    for(int icase=0; icase<T; ++icase)
    {
        cin >> C >> F >> X;
        
        double passedTime = 0.0;
        double cookiesLeft = X;
        double currentRate = 2.0;

        bool isFinished = false;
    
        while(!isFinished)
        {
            double costToBuyInSeconds = C/(currentRate+F);
            double timeToBuy = C/currentRate;
            double currentTimeToFinish = cookiesLeft/currentRate;


//            cout << "cookiesLeft: " << cookiesLeft << endl;
//            cout << "current rate: " << currentRate << endl;
//            cout << "Time passed: " << passedTime << endl;
//            cout << "currentTimeToFinish: " << currentTimeToFinish << endl;
            double timeToFinishIfBuy = timeToBuy + cookiesLeft/(currentRate+F);
//            cout << "timeToFinishIfBuy: " << timeToFinishIfBuy << endl;
//            cout << "timeToBuy: " << timeToBuy << endl;

            if (currentTimeToFinish <= costToBuyInSeconds || currentTimeToFinish <= timeToFinishIfBuy || currentTimeToFinish <= timeToBuy) //dont buy
            {
//                cout << "don't buy" << endl;
                passedTime += currentTimeToFinish;
                isFinished = true;
                break;
            }
            if (currentTimeToFinish > timeToFinishIfBuy) // buy it
            {
//                cout << "buy" << endl;
                passedTime += timeToBuy ;
                cookiesLeft += timeToBuy*currentRate;

                cookiesLeft -= C;
                currentRate += F;
            }
        }
        
        cout << "Case #" << icase+1 << ": " << fixed << setprecision(7) << passedTime << endl;
        

    }
    return 0;
}
