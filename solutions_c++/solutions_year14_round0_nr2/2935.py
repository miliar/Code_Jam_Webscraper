#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<fstream>
#include<list>
#include<cctype>
#include<algorithm>
#include<queue>
#include<stack>
#include<cmath>
#include<sstream>
#include<map>
#define long long LL

using namespace std;

int main ()
{
    ifstream cin("B-large.in");
    ofstream cout("Cookie.out");
    int cas;
    cin>>cas;
    cout.precision(7);
    for(int i=0;i<cas;i++)
    {
        double C,F,X,time=0,cumul=2;
        cin>>C>>F>>X;
        double temp=X/cumul;
        while(true)
        {
            time+=C/cumul;
            cumul+=F;
            double cost=X/cumul;
            if(time+cost>temp)
            {
                cout<<"Case #"<<i+1<<": "<<fixed<<temp<<"\n";
                break;
            }
            else
                temp=time+cost;
        }
    }

    return 0;
}

