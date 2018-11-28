#include<iostream>
#include<vector>
#include <iomanip>
using namespace std;
int main()
{
    cout.setf(ios::showpoint);
    cout.precision(7);
    cout.setf(ios::fixed);
    vector<double> res;
    int T;
    vector<vector<double> > vec;
    cin >> T;
    for(int i=0;i!=T;i++)
    {
        vector<double> num;
        double sum(0.0);
        double sp=2.0;
        double countnum(0);
        for(int j=0;j!=3;j++)
        {
            double temp;
            cin>>temp;
            num.push_back(temp);
        }
        vec.push_back(num);
        num.clear();
        while(vec[i][2]/sp>(vec[i][0]/sp+vec[i][2]/(sp+vec[i][1])))
        {
            sum+=vec[i][0]/sp;
            sp=sp+vec[i][1];
            countnum++;
        }
        res.push_back(sum+vec[i][2]/(sp));
    }
    for(int i=0;i!=T;i++)
    cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
}
