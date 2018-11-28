#include<iostream>
using namespace std;
int main()
{
    int t , k , y , sum;
    char sl[1000];
    cin >> t;
    for(int i = 1 ; i <= t ; i++)
    {
        y = 0;
        sum = 0;
        cin >> k;
        cin >> sl;
        for(int j = 0 ; j <= k ; j++)
        {
            if(sl[j] > '0' && sl[j] <= '9')
            {
                if(sum < j)
                {
                    y += j - sum;
                    sum = j;
                }
            }
            sum += sl[j] - '0';
        }
        cout << "Case #" << i << ": " << y << endl;
    }
}
