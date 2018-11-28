#include<iostream>
#include<iomanip>

using namespace std;

int main(void)
{
    int T;
    double F,ans,R;
	long double C, X;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        R=2;
        ans=0;
        cin>>C>>F>>X;
        while(C/R+X/(R+F)<X/R)
        {
            ans=ans+C/R;
            R=R+F;
        }
        ans=ans+X/R;
        cout<<"Case #"<<t+1<<": "<< setprecision (7) << fixed <<ans<<endl;
    }
    return 0;
}
