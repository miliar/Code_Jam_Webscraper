#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main()
{
    cout.setf(cout.showpoint);
    cout.precision(7);
    cout.setf(ios::fixed);
    int caseNum;
    double time=0;
    double speed=2;
    double buy,acc,win;
    vector<double> result;
    cin>>caseNum;
    for(int i=0;i<caseNum;i++)
    {
        speed = 2;
        cin>> buy >> acc >> win;
        if(buy >= win)
            result.push_back(win/speed);
        else
        {
            time = buy/speed;
            while(win/speed > buy/speed+win/(speed+acc))
            {
                speed = speed + acc;
                time = time + buy/speed;
            }
            time = time+(win-buy)/speed;
            result.push_back(time);
        }
    }
    for(int i=0;i<caseNum;i++)
        cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
    return 0;
}
