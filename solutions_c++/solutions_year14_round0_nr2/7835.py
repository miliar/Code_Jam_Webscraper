#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

class CookiesProduction{
private:
    double production;
    double time;
    double c, f, x;
    double cookies;

public:
    CookiesProduction(double c, double f, double x)
    {
        this->c = c;
        this->f = f;
        this->x = x;
        this->production = 2;
        this->time = 0;
        this->cookies = 0;
        simulate();
    }

    double getResult()
    {
        return this->time;
    }

private:
    void simulate()
    {
        time = min(timeToWait(0, production), timeToBuy(0, production));
    }

    double timeToWait(double time, double production)
    {
        return time+x/production;
    }

    double timeToBuy(double time, double p)
    {
        if(timeToWait(time, p) <= timeToWait(time+c/p, p+f)){
            //cout << "WAIT " << time << endl;
            return timeToWait(time, p);
        }else{
            //cout << "BUY " << time << endl;
            return timeToBuy(time+c/p, p+f);
        }
    }

    double min(double x, double y)
    {
        return (x<y) ? x : y;
    }

};

int main()
{
    int T;
    cin >> T;

    double res[T], c, f, x;
    CookiesProduction *cookie;

    for(int i = 0; i < T; i++)
    {
        cin >> c >> f >> x;
        cookie = new CookiesProduction(c, f, x);
        res[i] = cookie->getResult();
        //cout << endl;
    }

    for(int i = 0; i < T; i++)
        printf("Case #%d: %f\n", i+1, res[i]);

    return 0;
}

