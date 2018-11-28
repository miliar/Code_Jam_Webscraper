#include <iostream>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    cout.setf(ios::fixed);
    cout.precision(7);
    long double c,f,x,income,time,result;
    int t;
    cin>>t;
    //price of farm, profit, goal
    for(int j=1; j<=t; j++)
    {
        cin>>c>>f>>x;
        result=x/2;
        income=2;
        time=0;
        while(1)
        {
            time+=c/income;
            income+=f;
            if(result>time+(x/income))
                result=time+(x/income);
            else
                break;
        }
        cout<<"Case #"<<j<<": "<<result<<"\n";
    }


    return 0;

}
