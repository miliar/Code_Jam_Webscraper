#include<iostream>

using namespace std;

int main()
{
    int nTests = 0;
    double C, F, X;
    cin>>nTests;

    for (int i = 1; i <= nTests; i++)
    {
        cin>>C;
        cin>>F;
        cin>>X;

        double currentTime = 0;
        double currentRate = 2;
        double ttf = X/currentRate;
        double ttfBuy = C/currentRate + X/(currentRate+F);

        while (ttfBuy < ttf)
        {
            //Keep buying
            currentTime = currentTime + C/currentRate;
            currentRate = currentRate + F;
            ttf = X/currentRate;
            ttfBuy = C/currentRate + X/(currentRate+F);
        }

        double finishTime = currentTime + X/currentRate;

        cout.precision(10);
        cout<<"Case #"<<i<<": "<<finishTime<<endl;
    }
    return 0;
}
