#include<fstream>
#include<math.h>
using namespace std;
int k, i, u, t;
double ans, c, f, x, d;
int main()
{
    ifstream cin("B-large.in");
    ofstream cout("output.txt");
    cin>>t;
    cout.precision(7);
    for (u = 1; u <= t; u++)
        {
             cin>>c>>f>>x;
             d = x * f - 2 * c - f * c;
             if (d < 0)
                d = 0;
             k = ceil(d / (f * c));
             ans = x / (k * f + 2);
             for (i = 0; i < k; i++)
                  {
                      ans = ans + (c / (i * f + 2));
                  }
             cout<<"Case #"<<u;
             cout<<": "<<ans<<fixed<<endl;
         }
    return 0;
}
