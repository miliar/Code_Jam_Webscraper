#include <iostream>

using namespace std;

int main()
{
    int times;
    cin >> times;
    for (int t = 1; t <= times; t++)
    {
        int smax;
        cin >> smax;
        string s;
        cin>>s;
        int sum[10000]={0};
        int count = 0;
        sum[0] = s[0]-'0';
        int diff = 0;
        for (int j = 1; j <= smax; j++)
        {
            if (sum[j-1] < j)
            {

                if (diff < (j - sum[j-1]) )
                {
                    diff = (j - sum[j-1]);
                    count = diff;
                }

            }

            sum[j] = sum[j-1] + (s[j]-'0');
        }

        cout<<"Case #"<<t<<": "<<count<<endl;
    }

    return 0;
}

