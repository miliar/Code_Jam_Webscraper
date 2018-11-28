#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

// time using N farms
double helper(double R, double C, double F, double X, int N)
{
    double time = 0;
    for(int i=0;i<=N-1;i++)
    {
        time += C/(R+1.0*i*F);
    }
    time += X/(R+1.0*N*F);
    return time;
}

int main()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        double C,F,X;
        double R = 2.0;
        cin>>C>>F>>X;
        double baseline = helper(R,C,F,X,0);
        int i=1;
        while(1)
        {
            double time = helper(R,C,F,X,i);
            if(time>baseline)
                break;
            else
            {
                baseline = time;
                i++;
            }
        }
        printf("%.7f\n",baseline);
    }
    return 0;
}

