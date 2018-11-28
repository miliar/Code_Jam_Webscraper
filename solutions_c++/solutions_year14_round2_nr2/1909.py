#include <iostream>
#include <stdint.h>

using namespace std;
int main()
{
    int round;
    cin >> round;
    int count =1;
    int64_t a,b,k;
    int64_t result;
    int64_t num;
    int64_t i,j;
    while  (count <= round)
    {
        num = 0;
        cin >> a >> b >> k;
        for(i=0; i< a; i++)
        {
            for(j=0; j<b;j++)
            {
                //cout << i << j<< endl;
                result = i & j;
                //cout << result << endl;
                if(result < k)
                {
                    num++;
                }
            }
        }

        cout << "Case #" << count << ": " << num <<endl;
        count++;
    }
}

