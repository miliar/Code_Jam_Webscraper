#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

class Prod_Cookies{
private:
    double Prod;
    double time;
    double c, f, x;
  

public:
    Prod_Cookies(double c, double f, double x)
    {
        this->c = c;
        this->f = f;
        this->x = x;
        this->Prod = 2;
        this->time = 0;
       
        simulate();
    }

    double getResult()
    {
        return this->time;
    }

private:
    void simulate()
    {
        time = min(timeToWait(0, Prod), timeToBuy(0, Prod));
    }

    double timeToWait(double time, double Prod)
    {
        return time+x/Prod;
    }

    double timeToBuy(double time, double p)
    {
        if(timeToWait(time, p) <= timeToWait(time+c/p, p+f)){
            
            return timeToWait(time, p);
        }else{
            
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
    Prod_Cookies *cookie;

    for(int i = 0; i < T; i++)
    {
        cin >> c >> f >> x;
        cookie = new Prod_Cookies(c, f, x);
        res[i] = cookie->getResult();
       
    }

    for(int i = 0; i < T; i++)
	 printf("Case #%d: %f\n", i+1, res[i]); 
        

    return 0;
}

