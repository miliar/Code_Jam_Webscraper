#include <iostream>
using namespace std;

int main()
{
    int t, n, x;
    int counts[2501];
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>n;
        memset(counts, 0, 4 * 2501);
        for (int j = 1; j < 2 * n; j++)
        {
            for(int k = 0; k < n; k++)
            {
                cin>>x;
                counts[x]++;
            }
        }

        cout<<"Case #"<<i<<": ";
        int count = 0;
        for(int j = 1; j <= 2500; j++)
        {
            if(counts[j] != 0 && counts[j] % 2 == 1)
            {
                cout<<j<<" ";
                count++;
            }
            if(count == n)
                break;
        }
        cout<<"\n";
    }

    return 0;
}
