#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	int t;
    long double c, f, x, n, l, lt, m, d;
	cin >> t;
	for(int i = 0 ; i < t ; i++)
	{
         cin >> c >> f >> x;
         m = x / 2;
         n = 0.0;
         for(int j = 0 ; ; j++)
         {
              d = 2 + (j * f);
              n += c / d;
              d = 2 + ((j + 1) * f);
              l = x / d;
              lt = n + l;
              if(lt == m)
              {
                  cout << "Case #" << i+1 << ": " << setprecision(7) << fixed << lt;
                  if(i != t-1)
                       cout << endl;
                  break;
              }
              else if(lt > m)
              {
                  cout << "Case #" << i+1 << ": " << setprecision(7) << fixed << m;
                  if(i != t-1)
                       cout << endl;
                  break;
              }
              m = lt;
         }
    }
    return 0;
}
