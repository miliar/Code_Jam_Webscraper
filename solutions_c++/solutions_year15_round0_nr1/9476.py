#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    uint16_t T;
    uint32_t Sm;
    uint16_t S[1001];
    uint32_t r;
    uint32_t x;
    string   t = string();

    cin >> T;

    for (int k=0;k<T;++k)
    {
        t.clear();
        cin >> t;

        Sm = atoi(t.c_str());
        cin >> t;
        for (int i=0;i<t.size();++i)
            S[i]=atoi(t.substr(i,1).c_str());

        r=x=0;
        for (int i=0;i<=Sm,x<Sm;++i)
        {
            //cout << x << "+=" << S[i] << endl;
            x+=S[i];
            //cout << "if (" << x << " < " << i+1 << ")" << endl;
            if (x < i+1)
            {
                //cout << r << "+=(" << i + 1 << ")-" << x << endl;
                r+=(i+1)-x;
                //cout << x << "=" << i+1 << endl;
                x=i+1;
            }
        }

        cout << "Case #" << k+1 << ": " << r << endl;
    }
    return 0;
}
