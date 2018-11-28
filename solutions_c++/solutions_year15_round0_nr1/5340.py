#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        int s_max;
        string input;
        cin >> s_max >> input;
        int sum=0, y=0;
        if(s_max != 0)
        {
            for(int j=0; j<s_max+1; j++)
            {
                if(j>=1 && sum<j)
                {
                    y += j-sum;
                    sum++;
                }
                sum += input[j]-'0';
            }
        }

        cout << "Case #" << i+1 << ": " << y << endl;
    }
    return 0;
}
