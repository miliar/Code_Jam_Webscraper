#include<iostream>
#include <iomanip>
using namespace std;
double g[100000];//g[i]表示买i个农场的用时
double h[100000];
int main()
{
    double T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            double c,f,x;
            cin>>c>>f>>x;
            g[0]=0;h[0]=x/2;
            int j=1;
            for(;j<=100000;j++)
            {
                   g[j]=g[j-1]+c/((j-1)*f+2);
                   h[j]=g[j]+x/(j*f+2);
                   if(h[j]>=h[j-1]) break;
            }
            cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<h[j-1]<<endl;
    }
    return 0;
} 
