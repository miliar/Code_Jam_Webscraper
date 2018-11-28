#include<bits/stdc++.h>
#define loop(i, a, b)  for(int i=a;i<b;i++)
using namespace std;
double c, f, x;
double tim(double rate)
{
    if(c/rate + x/(rate+f) > x/rate)
        return x/rate;
    return min(x/rate, c/rate + tim(rate+f));
}
int main()
{
    ios_base::sync_with_stdio(false);
    cout<<setprecision(7)<<fixed;
    int t;
    cin>>t;
    loop(te, 0, t)
    {
        cin>>c>>f>>x;
        cout<<"Case #"<<te+1<<": ";
        cout<<tim(2.0)<<endl;
    }
    return 0;
}
