#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        int a;
        int b;
        int k;
        cin >> a;
        cin >> b;
        cin >> k;
        int N=0;
        for (int i=0; i<a; i++)
        {
            for (int j=0; j<b; j++)
            {
               //cout << (i&j) << endl;
                int c = i&j;
                if (c<k)
                    N++;
            }
        }
        cout << "Case #" << t << ": " <<N << endl;;
    }
}
