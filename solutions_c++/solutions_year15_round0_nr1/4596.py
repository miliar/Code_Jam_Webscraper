#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int round;
    cin >> round;
    for (int i=1; i<=round; i++)
    {
        int max;
        string people;
        cin >> max;
        cin >> people;
        
        int ans = 0;
        int tmp = (int)people[0]-48;
        if (tmp < max)
        {
            for (int j=1; j<max+1; j++)
            {
                if (tmp>max)
                    break;
                if (j>tmp)
                {
                    ans++;
                    tmp++;
                }
                tmp += (int)people[j]-48;
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
