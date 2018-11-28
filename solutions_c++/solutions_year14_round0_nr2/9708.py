#include <iomanip>
#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{
    //READ("B-small-attempt0.in");
    //WRITE("B-small-attempt0.out");
    int t;
    cin>>t;
    for(int T=0;T<t;T++)
    {
        double c,f,x,z=2;
        cin>>c>>f>>x;
        vector<double>sum;
        vector<double>sum2;
        vector<double>res;
        sum2.push_back(x/z);
        sum.push_back(c/z);
        for(int i=1;i<x;i++)
        {
            z+=f;
            sum.push_back(c/z);
            sum2.push_back(x/z);
        }
        res.push_back(sum2[0]);
        for(int k=1;k<sum.size();k++)
        {
            res.push_back(sum2[k]);
            for(int q=0;q<k;q++)
            {
                res[k]+=sum[q];
            }
        }
        sort(res.begin(),res.end());
        cout<<"Case #"<<T+1<<": "<<setprecision(9)<<res[0]<<endl;
    }
}
