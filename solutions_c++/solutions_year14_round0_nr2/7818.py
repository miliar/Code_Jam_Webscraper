#include <fstream>
#include <iomanip>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

int n,t;double c,f,x,T,sum;

void solve();

int main()
{
    int i;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>c>>f>>x;
        solve();
        cout<<fixed;
        cout<<"Case #"<<i<<": "<<setprecision(7)<<sum<<'\n';
    }
    cin.close();cout.close();
    return 0;
}

void solve()
{
    sum=0;int n=0;
    while (x/(2+n*f)>c/(2+n*f)+x/(2+(n+1)*f))
        {sum+=c/(2+n*f);n++;}
    sum+=x/(2+n*f);

}
