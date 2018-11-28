#include <iostream>
#include <iomanip>

using namespace std;

int T, n;
long double c,f,x,oldans,ans,t;

int main() 
{
    cin>>T;
    for (int ii = 0; ii < T; ++ii)
    {
        cin>>c>>f>>x;
        oldans = x/2;
        n = 1;
        t = c/2;
        ans = t+x/(2+f);
        while (oldans > ans)
        {
            oldans = ans;
            t = t+c/(2+n*f);
            n++;
            ans = t+x/(2+n*f);
        }
        cout<<"Case #"<<ii+1<<": ";
        cout<<setprecision(8)<<oldans<<endl;
    }
    return 0;
}