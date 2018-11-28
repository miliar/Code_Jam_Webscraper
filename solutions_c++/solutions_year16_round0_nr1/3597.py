#include <iostream>
#include <vector>
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    cin >> n;

    for (int i=1; i<=n; i++)
    {
        unsigned long long int y;
        cin >> y;

        if (y==0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        unsigned long long int w=0;
        vector<int> ret(10,0);
        while (ret[0]+ret[1]+ret[2]+ret[3]+ret[4]+ret[5]+ret[6]+ret[7]+ret[8]+ret[9]<10)
        {
        w+=y;
            int sa=w;
            while (sa>0)
            {
                ret[sa%10]=1;
                sa/=10;
            }

        }
         cout << "Case #" << i << ": " << w << endl;
        }
        return 0;
    }
