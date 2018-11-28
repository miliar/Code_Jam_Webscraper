#include<fstream>
#include<algorithm>
using namespace std;
int u, i, j, v, t, n, a1, a2;
double a[1010], b[1010];
int main()
{
    ifstream cin("D-small-attempt0.in");
    ofstream cout("output.txt");
    cin>>t;
    for (u = 1; u <= t; u++)
        {
             cout<<"Case #"<<u;
             cout<<": ";
             cin>>n;
             for (i = 1; i <= n; i++)
                 cin>>a[i];
             for (i = 1; i <= n ; i++)
                 cin>>b[i];
             sort(a + 1, a + (n + 1));
             reverse(a + 1, a + (n + 1));
             sort(b + 1, b + (n + 1));
             reverse(b + 1, b + (n + 1));
             a2 = n;
             a1 = 0;
             j = 1;
             for (i = 1; i <= n; i++)
                 {
                    if (a[i] < b[j])
                       {
                             a2--;
                             j++;
                             } 
                  }
             j = 1;
             v = 1;
             for (i = 1; i <= n; i++)
                 {
                      if (a[j] > b[v])
                         {
                               a1++;
                               j++;
                               v++;
                               }
                      else
                          v++;
                  }
             cout<<a1<<" "<<a2<<endl;
         }
    return 0;
}
