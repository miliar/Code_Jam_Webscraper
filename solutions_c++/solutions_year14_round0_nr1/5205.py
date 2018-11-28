#include<fstream>
using namespace std;
int i, j, t, x, y, a[20], d, b[20], k, u;
int main()
{
    ifstream cin("A-small-attempt2.in");
    ofstream cout("output.txt");
    cin>>t;

    for (u = 1; u <= t; u++)
        {
             cin>>x;
             for (i = 1; i <= 4; i++)
                 for (j = 1; j <= 4; j++)
                     {
                        cin>>d;
                        a[d] = i;
                        }
             cin>>y;
             for (i = 1; i <= 4; i++)
                  for (j = 1; j <= 4; j++)
                     {
                        cin>>d;
                        b[d] = i;
                        }
             k = 0;
             for (i = 1; i <= 16; i++)
                 {
                      if ((a[i] == x) && (b[i] == y))
                         {
                                k++;
                                d = i;
                                }
                  }
             cout<<"Case #"<<u;
             if (k == 0)
                cout<<": Volunteer cheated!"<<endl;
             if (k > 1)
                cout<<": Bad magician!"<<endl;
             if (k == 1)
                cout<<": "<<d<<endl;
         }
    return 0;
}
