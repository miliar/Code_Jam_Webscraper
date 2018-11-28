#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

double calc(int n,double f,double c)
{

    double ans=0;

    for(double i=2;i<n;i+=f)
    {
        ans+=c/i;
    }
    return ans;
}

int main()
{
    fstream file;
    ofstream output;
    file.open("B-large.in");
    output.open("answer.txt");

    int n=0;

    file>>n;

    for(int i=1;i<=n;i++)
    {
        double c,f,x;
        file>>c;
        file>>f;
        file>>x;

        vector<double> ans;
        int pos=0;
        double rate=2;

        ans.push_back(x/rate);
        pos++;

        while(1)
        {
            rate+=f;

            double cal=calc(rate,f,c);

            ans.push_back((x/rate) + cal);

            if(ans[pos]>ans[pos-1])
            {
               // cout<<"Case #"<<i<<": "<<ans[pos-1]<<endl;
                output<<setprecision(7)<<fixed<<"Case #"<<i<<": "<<ans[pos-1]<<endl;
                break;
            }
            pos++;
        }

    }

}
