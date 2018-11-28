#include <iostream>

using namespace std;

void print_doubled_mask(int k, int msk)
{
    for(int i=k-1;i>=0;--i)
    {
        char c = (msk & (1 << i)) ? '1' : '0';
        cout << c << c;
    }
}

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        cout << "Case #" << lp << ":\n";
        int n,j;
        cin >> n >> j;
        int k = (n-4)/2;
        for(int msk=0;msk<(1<<k);++msk)
        {
            if(j-- == 0)
            {
                break;
            }

            cout << "11";
            print_doubled_mask(k, msk);
            cout << "11";
            for(int i=2;i<=10;++i)
            {
                cout << " " << i + 1;
            }
            cout << "\n";
        }
    }

    return 0;
}
