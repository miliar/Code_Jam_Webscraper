#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
double cal(vector<double> data)
{
    double C=data[0];
    double F=data[1];
    double X=data[2];
    double n=(F*X-2.0*C)/(F*C)-1.0;
    double time=0.0;
    double i=0;
    while(i<=n)
    {
        time+=C/(2.0+i*F);
       //cout<<time<<endl;
        i=i+1;
    }
    time+=X/(2.0+i*F);
    return time;
}
int main()
{
    int num;
    cin>>num;
    vector<vector<double>> data;

    for(int k=0;k<num;k++)
    {
        vector<double> temp;
        for(int m=0;m<3;m++)
        {
            double input;
            cin>>input;
            temp.push_back(input);
        }
        data.push_back(temp);
    }
    for(int l=0;l<num;l++)
    {
        double t=cal(data[l]);
        cout.setf(ios::fixed);
        cout<<"Case #"<<l+1<<": "<<setprecision(7)<<t<<endl;
    }
    return 0;
}
